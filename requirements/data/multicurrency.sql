-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.5.8-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for multicurrency
CREATE DATABASE IF NOT EXISTS `multicurrency` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `multicurrency`;

-- Dumping structure for table multicurrency.exchange_rate
CREATE TABLE IF NOT EXISTS `exchange_rate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `base_currency` varchar(3) NOT NULL,
  `exchange_currency` varchar(3) NOT NULL,
  `rate` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Dumping data for table multicurrency.exchange_rate: ~11 rows (approximately)
/*!40000 ALTER TABLE `exchange_rate` DISABLE KEYS */;
INSERT INTO `exchange_rate` (`id`, `base_currency`, `exchange_currency`, `rate`) VALUES
	(1, 'SGD', 'CAD', 0.9255),
	(2, 'SGD', 'CNH', 4.7868),
	(3, 'SGD', 'EUR', 0.7086),
	(4, 'SGD', 'HKD', 5.5830),
	(5, 'SGD', 'JPY', 97.5303),
	(6, 'SGD', 'NZD', 1.1612),
	(7, 'SGD', 'NOK', 7.2912),
	(8, 'SGD', 'GBP', 0.5974),
	(9, 'SGD', 'SEK', 7.5168),
	(10, 'SGD', 'THB', 25.7275),
	(11, 'SGD', 'USD', 0.7113);
/*!40000 ALTER TABLE `exchange_rate` ENABLE KEYS */;

-- Dumping structure for table multicurrency.wallet
CREATE TABLE IF NOT EXISTS `wallet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Dumping data for table multicurrency.wallet: ~5 rows (approximately)
/*!40000 ALTER TABLE `wallet` DISABLE KEYS */;
INSERT INTO `wallet` (`id`, `user_id`, `name`) VALUES
	(1, 1, "Multi-Currency Account"),
	(2, 1, "Travel Account"),
	(3, 2, "Trading Account"),
	(4, 3, "Multi-Currency Account"),
	(5, 4, "Trip to Japan");
/*!40000 ALTER TABLE `wallet` ENABLE KEYS */;

-- Dumping structure for table multicurrency.currency
CREATE TABLE IF NOT EXISTS `currency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wallet_id` int(11) NOT NULL,
  `currency` varchar(3) NOT NULL,
  `amount` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_currency_wallet` (`wallet_id`),
  CONSTRAINT `FK_currency_wallet` FOREIGN KEY (`wallet_id`) REFERENCES `wallet` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Dumping data for table multicurrency.currency: ~24 rows (approximately)
/*!40000 ALTER TABLE `currency` DISABLE KEYS */;
INSERT INTO `currency` (`id`, `wallet_id`, `currency`, `amount`) VALUES
	(1, 1, 'SGD', 4294.50),
	(2, 1, 'CAD', 5687.65),
	(3, 1, 'CNH', 6063.14),
	(4, 1, 'EUR', 8089.82),
	(5, 1, 'HKD', 7862.36),
	(6, 1, 'JPY', 5759.15),
	(7, 1, 'NZD', 6943.26),
	(8, 1, 'NOK', 4038.10),
	(9, 1, 'GBP', 8287.33),
	(10, 1, 'SEK', 5126.40),
	(11, 1, 'THB', 147.62),
	(12, 1, 'USD', 7331.77),
	(13, 2, 'SGD', 485.19),
  (14, 2, 'CAD', 2634.58),
	(15, 2, 'CNH', 3893.29),
	(16, 2, 'EUR', 3887.15),
	(17, 2, 'HKD', 4065.34),
	(18, 2, 'JPY', 1702.47),
	(19, 2, 'NZD', 3299.38),
	(20, 2, 'NOK', 7681.32),
	(21, 2, 'GBP', 3720.37),
	(22, 2, 'SEK', 4511.50),
	(23, 2, 'THB', 6216.60),
	(24, 2, 'USD', 9103.66);
/*!40000 ALTER TABLE `currency` ENABLE KEYS */;

-- Dumping structure for table multicurrency.transaction
CREATE TABLE IF NOT EXISTS `transaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wallet_id` int(11) NOT NULL,
  `debit_id` int(11) NOT NULL,
  `debit_currency` varchar(3) NOT NULL,
  `debit_amount` float NOT NULL,
  `credit_id` int(11) NOT NULL,
  `credit_currency` varchar(3) NOT NULL,
  `credit_amount` float NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `created_by` varchar(50) DEFAULT NULL,
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `updated_by` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_transaction_wallet` (`wallet_id`),
  KEY `FK_transaction_debit` (`debit_id`),
  KEY `FK_transaction_credit` (`credit_id`),
  CONSTRAINT `FK_transaction_wallet` FOREIGN KEY (`wallet_id`) REFERENCES `wallet` (`id`),
  CONSTRAINT `FK_transaction_debit` FOREIGN KEY (`debit_id`) REFERENCES `currency` (`id`),
  CONSTRAINT `FK_transaction_credit` FOREIGN KEY (`credit_id`) REFERENCES `currency` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- TODO: REPLACE WITH MULTICURRENCY.TRANSACTION
-- Dumping data for table multicurrency.transaction: ~4 rows (approximately)
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` (`id`, `wallet_id`, `debit_id`, `debit_currency`, `debit_amount`, `credit_id`, `credit_currency`, `credit_amount`, `description`, `created_at`, `created_by`, `updated_at`, `updated_by`) VALUES
	(1, 1, 4, 'EUR', 97.19, 8, 'NOK', 1000.00, '', '2021-11-04 16:00:00', 'Jacky', '2021-11-06 16:00:00', 'Jacky'),
	(2, 2, 13, 'SGD', 102.53, 18, 'JPY', 10000.00, 'allowance for winter school', '2021-11-05 16:00:00', 'Jane', '2021-11-05 16:00:00', NULL),
	(3, 2, 20, 'NOK', 250.00, 15, 'CNH', 164.13, 'trip to china', '2021-11-05 16:00:00', 'Jane', '2021-11-06 16:00:00', 'Jane'),
	(4, 1, 6, 'JPY', 685577.82, 12, 'USD', 5000.00, 'to transfer to securities account wallet', '2021-11-06 16:00:00', 'Jacky', '2021-11-06 16:00:00', null);
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;

-- Dumping structure for table multicurrency.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Dumping data for table multicurrency.user: ~5 rows (approximately)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `username`, `password`, `name`) VALUES
	(1, 'user101', '123456', 'Jacky'),
	(2, 'user102', '123456', 'Jane'),
	(3, 'user103', '123456', 'Tom'),
	(4, 'user104', '123456', 'Helen'),
	(5, 'user105', '123456', 'Mark');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
