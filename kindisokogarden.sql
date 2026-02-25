-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2026 at 09:20 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kindisokogarden`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_description` text NOT NULL,
  `product_cost` int(11) NOT NULL,
  `product_photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES
(1, 'Airmax', 'White blue stripes sizes 43', 5300, 'Airmax w&b.jpg'),
(2, 'Pattler', ' black   sizes 43', 5300, 'black.jpg'),
(3, 'Black Pattler', ' White and black size 41', 5400, 'black.jpg'),
(4, 'Skechers', 'blue and white double sole size 43', 3500, 'blue.jpg'),
(5, 'NikeAirmax', '  wholly black   sizes 43', 2300, 'extremely black.jpg'),
(6, 'NikeAirmax', ' White with green stripes  sizes 43', 2600, 'green.jpg'),
(7, 'Nike Jordan v-1', ' Black and Red sizes 39', 2600, 'red jordan.jpg'),
(8, 'Nike Jordan v-1 low heel', ' Green and Black White sizes 39', 2500, '3bc9be98f985003a5b0ec95e8b009c9d.jpg'),
(9, 'Nike Jordan v-1', ' Grey and White sizes 39', 2500, 'grey.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `phone`) VALUES
(1, 'Mikaela Esther', '123456', 'MikaelaEsther@gmail.com', '0720347988'),
(2, 'LishanMaya', '456789', 'LishanMaya@gmail.com', '0726208259'),
(3, 'EstherMaya', '345627', 'EstherMaya@gmail.com', '0721666951'),
(5, 'jay', '123pass', 'jay@gmail.com', '0712213443'),
(6, 'Tulon', '5y67u8', 'Tulon@gmail.com', '0712567739'),
(7, 'Talia', '456y77', 'Taliachieng@gmail.com', '0712567739'),
(8, 'Tulil', '45y67', 'Taliachieng@gmail.com', '0712567739'),
(9, 'James', '3r5t66', 'Tjames@gmail.com', '0712567739');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
