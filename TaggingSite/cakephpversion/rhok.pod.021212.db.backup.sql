-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 02, 2012 at 07:35 PM
-- Server version: 5.5.24-log
-- PHP Version: 5.3.13

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pod`
--

-- --------------------------------------------------------

--
-- Table structure for table `disciplines`
--

CREATE TABLE IF NOT EXISTS `disciplines` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `disciplines`
--

INSERT INTO `disciplines` (`id`, `name`) VALUES
(1, 'Art'),
(2, 'Citizenship'),
(5, 'Science');

-- --------------------------------------------------------

--
-- Table structure for table `indudtries`
--

CREATE TABLE IF NOT EXISTS `indudtries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `indudtries`
--

INSERT INTO `indudtries` (`id`, `name`) VALUES
(11, 'Armed Forces'),
(12, 'Computing, design and IT'),
(8, 'Education, Health and Social Care'),
(9, 'Environment'),
(3, 'IT and Design'),
(1, 'Office'),
(7, 'Random'),
(10, 'Retail and Manufacturing');

-- --------------------------------------------------------

--
-- Table structure for table `resources`
--

CREATE TABLE IF NOT EXISTS `resources` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `url` text NOT NULL,
  `youtubeid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=20 ;

--
-- Dumping data for table `resources`
--

INSERT INTO `resources` (`id`, `title`, `description`, `url`, `youtubeid`) VALUES
(8, 'Senior Scientist', '', 'http://www.youtube.com/watch?feature=player_embedded&v=dLvPrm75HXU#!', 'dLvPrm75HXU'),
(9, 'DJ & Broadcaster', '', 'http://www.youtube.com/watch?feature=player_embedded&v=FbjN9VtZc5s', 'FbjN9VtZc5s'),
(10, 'Maxillo Facial Technician', '', 'http://www.youtube.com/watch?feature=player_embedded&v=gBdiSI8fgpE', 'gBdiSI8fgpE'),
(11, 'Senior Technical Manager', '', 'http://www.youtube.com/watch?feature=player_embedded&v=k4QtSQkRQXA#!', 'k4QtSQkRQXA'),
(12, 'Mortuary Services Manager', '', 'http://www.youtube.com/watch?feature=player_embedded&v=mG9lzLnpi2Q', 'mG9lzLnpi2Q'),
(13, 'Cartographer', '', 'http://www.youtube.com/watch?feature=player_embedded&v=vrhmYiAqp0k#!', 'vrhmYiAqp0k'),
(14, 'Art Buyer', '', 'http://www.youtube.com/watch?feature=player_embedded&v=vv2llRAPjrU', 'vv2llRAPjrU'),
(15, 'Social Media Assistant', '', 'http://www.youtube.com/watch?v=IVTCXWlZuBE&feature=player_embedded#!', 'IVTCXWlZuBE'),
(16, 'Teacher', '', 'http://www.youtube.com/watch?v=mOPQnp2G_v0&feature=player_embedded#!', 'mOPQnp2G_v0'),
(17, 'Graphic designer', '', 'http://www.youtube.com/watch?v=MwgBpNg4ytg&list=PLC29F369F889210CF&index=35&feature=plpp_video', 'MwgBpNg4ytg'),
(18, 'Operations Manager', '', 'http://www.youtube.com/watch?v=RDhprCjdckE', 'RDhprCjdckE'),
(19, 'Judge', '', 'http://www.youtube.com/watch?v=2eUAmTcJKkw&feature=player_embedded', '2eUAmTcJKkw');

-- --------------------------------------------------------

--
-- Table structure for table `resources_disciplines`
--

CREATE TABLE IF NOT EXISTS `resources_disciplines` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resource_id` int(11) NOT NULL,
  `discipline_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resource_id` (`resource_id`,`discipline_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `resources_disciplines`
--

INSERT INTO `resources_disciplines` (`id`, `resource_id`, `discipline_id`) VALUES
(7, 8, 5),
(8, 9, 1),
(9, 10, 1),
(10, 11, 5),
(11, 12, 5),
(12, 13, 5),
(13, 14, 1),
(14, 15, 2),
(15, 16, 2),
(16, 17, 1),
(17, 18, 2),
(18, 19, 2);

-- --------------------------------------------------------

--
-- Table structure for table `resources_indudtries`
--

CREATE TABLE IF NOT EXISTS `resources_indudtries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resource_id` int(11) NOT NULL,
  `indudtry_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resource` (`resource_id`,`indudtry_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 ;

--
-- Dumping data for table `resources_indudtries`
--

INSERT INTO `resources_indudtries` (`id`, `resource_id`, `indudtry_id`) VALUES
(9, 8, 8),
(10, 9, 7),
(11, 10, 8),
(12, 11, 10),
(13, 12, 7),
(21, 13, 3),
(15, 14, 10),
(24, 15, 3),
(23, 16, 8),
(22, 17, 3),
(19, 18, 10),
(20, 19, 7);

-- --------------------------------------------------------

--
-- Table structure for table `resources_tags`
--

CREATE TABLE IF NOT EXISTS `resources_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_id` int(11) NOT NULL,
  `resource_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tag_id` (`tag_id`,`resource_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tags`
--

CREATE TABLE IF NOT EXISTS `tags` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tags`
--

INSERT INTO `tags` (`id`, `name`) VALUES
(1, 'Art');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
