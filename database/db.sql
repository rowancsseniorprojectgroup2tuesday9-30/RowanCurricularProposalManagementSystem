-- MySQL dump 10.17  Distrib 10.3.12-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: senior_project
-- ------------------------------------------------------
-- Server version	10.3.12-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `consult_letter`
--

DROP TABLE IF EXISTS `consult_letter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `consult_letter` (
  `consult_letter_id` smallint(6) NOT NULL,
  `employee_id` smallint(6) NOT NULL,
  `proposal_id` smallint(6) NOT NULL,
  PRIMARY KEY (`consult_letter_id`),
  KEY `employee_id` (`employee_id`),
  KEY `proposal_id` (`proposal_id`),
  CONSTRAINT `consult_letter_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`),
  CONSTRAINT `consult_letter_ibfk_2` FOREIGN KEY (`proposal_id`) REFERENCES `proposal` (`proposal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consult_letter`
--

LOCK TABLES `consult_letter` WRITE;
/*!40000 ALTER TABLE `consult_letter` DISABLE KEYS */;
/*!40000 ALTER TABLE `consult_letter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consult_letter_revision`
--

DROP TABLE IF EXISTS `consult_letter_revision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `consult_letter_revision` (
  `consult_letter_id` smallint(6) NOT NULL,
  `consult_letter_file_path` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `consult_letter_date` date NOT NULL,
  KEY `consult_letter_id` (`consult_letter_id`),
  CONSTRAINT `consult_letter_revision_ibfk_1` FOREIGN KEY (`consult_letter_id`) REFERENCES `consult_letter` (`consult_letter_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consult_letter_revision`
--

LOCK TABLES `consult_letter_revision` WRITE;
/*!40000 ALTER TABLE `consult_letter_revision` DISABLE KEYS */;
/*!40000 ALTER TABLE `consult_letter_revision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cover_sheet`
--

DROP TABLE IF EXISTS `cover_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cover_sheet` (
  `cover_sheet_id` smallint(6) NOT NULL,
  PRIMARY KEY (`cover_sheet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cover_sheet`
--

LOCK TABLES `cover_sheet` WRITE;
/*!40000 ALTER TABLE `cover_sheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `cover_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cover_sheet_revision`
--

DROP TABLE IF EXISTS `cover_sheet_revision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cover_sheet_revision` (
  `cover_sheet_id` smallint(6) NOT NULL,
  `cover_sheet_file_path` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cover_sheet_date` date NOT NULL,
  KEY `cover_sheet_id` (`cover_sheet_id`),
  CONSTRAINT `cover_sheet_revision_ibfk_1` FOREIGN KEY (`cover_sheet_id`) REFERENCES `cover_sheet` (`cover_sheet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cover_sheet_revision`
--

LOCK TABLES `cover_sheet_revision` WRITE;
/*!40000 ALTER TABLE `cover_sheet_revision` DISABLE KEYS */;
/*!40000 ALTER TABLE `cover_sheet_revision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `employee_id` smallint(6) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `middle_name` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `department` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `curricular_consultant` tinyint(4) NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `library_form`
--

DROP TABLE IF EXISTS `library_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `library_form` (
  `library_form_id` smallint(6) NOT NULL,
  PRIMARY KEY (`library_form_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library_form`
--

LOCK TABLES `library_form` WRITE;
/*!40000 ALTER TABLE `library_form` DISABLE KEYS */;
/*!40000 ALTER TABLE `library_form` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `library_form_revision`
--

DROP TABLE IF EXISTS `library_form_revision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `library_form_revision` (
  `library_form_id` smallint(6) NOT NULL,
  `library_form_file_path` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `library_form_date` date NOT NULL,
  KEY `library_form_id` (`library_form_id`),
  CONSTRAINT `library_form_revision_ibfk_1` FOREIGN KEY (`library_form_id`) REFERENCES `library_form` (`library_form_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library_form_revision`
--

LOCK TABLES `library_form_revision` WRITE;
/*!40000 ALTER TABLE `library_form_revision` DISABLE KEYS */;
/*!40000 ALTER TABLE `library_form_revision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proposal`
--

DROP TABLE IF EXISTS `proposal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proposal` (
  `proposal_id` smallint(6) NOT NULL AUTO_INCREMENT,
  `cover_sheet_id` smallint(6) DEFAULT NULL,
  `template_id` smallint(6) DEFAULT NULL,
  `library_form_id` smallint(6) DEFAULT NULL,
  `proposal_date` date NOT NULL,
  `revision_note` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `proposal_title` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `proposal_description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `need_library_form` char(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `template_type` char(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`proposal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proposal`
--

LOCK TABLES `proposal` WRITE;
/*!40000 ALTER TABLE `proposal` DISABLE KEYS */;
/*!40000 ALTER TABLE `proposal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sponsor`
--

DROP TABLE IF EXISTS `sponsor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sponsor` (
  `proposal_id` smallint(6) NOT NULL,
  `employee_id` smallint(6) NOT NULL,
  `is_author` tinyint(4) NOT NULL,
  KEY `proposal_id` (`proposal_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `sponsor_ibfk_1` FOREIGN KEY (`proposal_id`) REFERENCES `proposal` (`proposal_id`),
  CONSTRAINT `sponsor_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sponsor`
--

LOCK TABLES `sponsor` WRITE;
/*!40000 ALTER TABLE `sponsor` DISABLE KEYS */;
/*!40000 ALTER TABLE `sponsor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `template`
--

DROP TABLE IF EXISTS `template`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `template` (
  `template_id` smallint(6) NOT NULL,
  PRIMARY KEY (`template_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `template`
--

LOCK TABLES `template` WRITE;
/*!40000 ALTER TABLE `template` DISABLE KEYS */;
/*!40000 ALTER TABLE `template` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `template_revision`
--

DROP TABLE IF EXISTS `template_revision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `template_revision` (
  `template_id` smallint(6) NOT NULL,
  `template_file_path` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `template_date` date NOT NULL,
  KEY `template_id` (`template_id`),
  CONSTRAINT `template_revision_ibfk_1` FOREIGN KEY (`template_id`) REFERENCES `template` (`template_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `template_revision`
--

LOCK TABLES `template_revision` WRITE;
/*!40000 ALTER TABLE `template_revision` DISABLE KEYS */;
/*!40000 ALTER TABLE `template_revision` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-20 20:12:58
