-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 06, 2022 at 10:21 PM
-- Server version: 8.0.27
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `biblioteca`
--

-- --------------------------------------------------------

--
-- Table structure for table `camara`
--

DROP TABLE IF EXISTS `camara`;
CREATE TABLE IF NOT EXISTS `camara` (
  `codigo` varchar(30) NOT NULL,
  `entrada` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `camara`
--

INSERT INTO `camara` (`codigo`, `entrada`) VALUES
('curp', 'ingresarcurp');

-- --------------------------------------------------------

--
-- Table structure for table `gur`
--

DROP TABLE IF EXISTS `gur`;
CREATE TABLE IF NOT EXISTS `gur` (
  `nombre` varchar(30) NOT NULL,
  `apellidoP` varchar(30) NOT NULL,
  `apellidoM` varchar(30) NOT NULL,
  `edad` int NOT NULL,
  `curp` varchar(25) NOT NULL,
  `localidad` varchar(30) NOT NULL,
  `direccion` varchar(35) NOT NULL,
  `telefono` int NOT NULL,
  `mail` varchar(35) NOT NULL,
  `tipo_cuenta` varchar(10) NOT NULL,
  `contrasena` varchar(35) NOT NULL,
  `rep_contra` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `gur`
--

INSERT INTO `gur` (`nombre`, `apellidoP`, `apellidoM`, `edad`, `curp`, `localidad`, `direccion`, `telefono`, `mail`, `tipo_cuenta`, `contrasena`, `rep_contra`) VALUES
('1', '2', '3', 4, '5', '6', '7', 8, '9', '10', '11', '12'),
('eduardo', 'jose', 'chui', 21, 'ingresarcurp', 'san francisco cal', 'hidalgo sur s/n', 8521937, 'direccion@host.com', 'admin', 'sate007', 'sate007'),
('takeshi', 'alaska', 'siveriano', 3, 'notiene', 'nosabe', 'tampoco', 123125423, 'lasdf@fad/cds', 'user', ' ', ' '),
('uno', 'dos', 'tres', 4, 'cinco5', 'seis', 'siete', 8888888, 'nueve@nueve.nueve', 'usuario', ' ', ' '),
('aide', 'gutierrez', 'guadarrama', 20, 'AAPC000607HQRBCRA5', 'tenango del valle', 'siempre viva', 7229653, 'aide_guti@yahoo.com.mx', 'user', ' ', ' '),
('hfadj', 'faadfasd', 'hfadsf', 14, '1234567', 'lkasdfj', 'jfjadlkfasjdlfk', 15466777, 'ldaksjfasdlk@f', 'admin', 'yu', 'yu'),
('Alexa', 'tenorio', 'lopez ', 16, 'sata051022mhjiu', 'san francisco cal', 'siempre activa', 2468157, 'rhftjhgjhgjc6@nosave.kom', 'user', ' ', ' ');

-- --------------------------------------------------------

--
-- Table structure for table `table1`
--

DROP TABLE IF EXISTS `table1`;
CREATE TABLE IF NOT EXISTS `table1` (
  `id` int NOT NULL,
  `nombre` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `table1`
--

INSERT INTO `table1` (`id`, `nombre`) VALUES
(1, 'Eduardo'),
(2, 'chencho'),
(3, 'Alexa'),
(4, 'don');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
