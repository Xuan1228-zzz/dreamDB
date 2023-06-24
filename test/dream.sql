-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2023-06-13 21:21:12
-- 伺服器版本： 10.4.28-MariaDB
-- PHP 版本： 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `dream`
--

-- --------------------------------------------------------

--
-- 資料表結構 `eq`
--

CREATE TABLE `eq` (
  `Nid` int(11) NOT NULL,
  `hash` varchar(255) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `work_max` int(11) DEFAULT NULL,
  `exp` float DEFAULT NULL,
  `lucky` float DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `coupon` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `exercise`
--

CREATE TABLE `exercise` (
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `type` varchar(255) DEFAULT NULL,
  `accuracy` float DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `things`
--

CREATE TABLE `things` (
  `type` int(11) NOT NULL,
  `amount` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `users`
--

CREATE TABLE `users` (
  `Uid` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `birth` date DEFAULT NULL,
  `wallet_addr` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `eq`
--
ALTER TABLE `eq`
  ADD PRIMARY KEY (`Nid`),
  ADD KEY `user_id` (`user_id`);

--
-- 資料表索引 `exercise`
--
ALTER TABLE `exercise`
  ADD PRIMARY KEY (`user_id`,`timestamp`);

--
-- 資料表索引 `things`
--
ALTER TABLE `things`
  ADD PRIMARY KEY (`user_id`,`type`);

--
-- 資料表索引 `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Uid`);

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `eq`
--
ALTER TABLE `eq`
  ADD CONSTRAINT `eq_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`Uid`);

--
-- 資料表的限制式 `exercise`
--
ALTER TABLE `exercise`
  ADD CONSTRAINT `exercise_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`Uid`);

--
-- 資料表的限制式 `things`
--
ALTER TABLE `things`
  ADD CONSTRAINT `things_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`Uid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
