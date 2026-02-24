from flask import *
import pymysql
import os

# create an instance/create/initiate Flask app

app=Flask(__name__)
#app.config['UPLOAD_FOLDER']ensures that all images uploaded will be saved in the images folder inside the static folder created
app.config['UPLOAD_FOLDER']='static/images'

@app.route("/api/signup",methods=["POST"])
def signup():
    username=request.form["username"]
    password=request.form["password"]
    email=request.form["email"]
    phone=request.form["phone"]

    #print(username,password,email,phone)
    #connecting to DB
    connection=pymysql.connect(host="localhost",user="root",password="" ,database="kindisokogarden")
    #create a cursor that will be used to execute queries with
    cursor=connection.cursor()

    sql="insert into users(username,password,email,phone) values(%s,%s,%s,%s)"
    #prepare for data
    data=(username,password,email,phone)
    cursor.execute(sql,data)
    #commit ensures data is saved in a stable storage
    connection.commit()
    
   
    return jsonify({"message":"Thank You for joining"})

#sign in
@app.route("/api/signin",methods=["POST"])
def signin():
    email=request.form["email"]
    password=request.form["password"]
    print(email,password)
#connection of python file and my sql file
    connection=pymysql.connect(host="localhost",user="root",password="",database="kindisokogarden")
    #cursor is used to execute your query
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    sql="select * from users where email=%s and password=%s"
    data=(email,password)
    cursor.execute(sql,data)
    count=cursor.rowcount
    print("count",count)
    if count==0:
        return jsonify({"message":"invalid credentials"})
    else:
        user=cursor.fetchone()
        print(user)
        return jsonify({"message":"login Success","user":user})
    
# Add Product Details
@app.route("/api/add_product", methods=["POST"])
def add_product():
    product_name=request.form["product_name"]
    product_description=request.form["product_description"]
    product_photo=request.files["product_photo"]
    product_cost=request.form["product_cost"]

    # extract file now
    filename=product_photo.filename
    #specify where our image file will be saved(static)-image path
    photo_path=os.path.join(app.config['UPLOAD_FOLDER'],filename)
    product_photo.save(photo_path)

   # print(product_name,product_description,product_photo,product_cost,photo_path)
    connection=pymysql.connect(host="localhost",user="root",password="",database="kindisokogarden")
    cursor=connection.cursor()

    sql="insert into product_details(product_name,product_description,product_cost,product_photo)values(%s,%s,%s,%s)"
    data=(product_name,product_description,product_cost,filename)

    #using cursor to execute
    cursor.execute(sql,data)

    #commit
    connection.commit()
    


    return jsonify({"message":"Product details added successfully"})

# get products
@app.route("/api/get_product_details")
def get_product_details():
    connection=pymysql.connect(host="localhost",user="root",password="",database="kindisokogarden")
    cursor=connection.cursor(pymysql.cursors.DictCursory)

    sql="select * from product_details"
    cursor.execute(sql)

    product_details=cursor.fetchall()
    return jsonify ({"message":product_details})


# Mpesa Payment Route 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth
 
@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        amount= request.form['amount']
        phone = request.form['phone']
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"
 
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
 
        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']
 
        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')
 
        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }
 
        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }
 
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL
 
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return jsonify({"message": "Please Complete Payment in Your Phone and we will deliver in minutes"})



if __name__=='__main__':
    app.run(debug=True)
