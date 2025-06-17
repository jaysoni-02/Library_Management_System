-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book_issued`
--

DROP TABLE IF EXISTS `book_issued`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_issued` (
  `ISSUE_ID` int NOT NULL,
  `USER_ID` int NOT NULL,
  `BOOK_ID` int NOT NULL,
  `BOOK_TITLE` varchar(255) DEFAULT NULL,
  `NUMBER_OF_COPIES_ISSUED` int NOT NULL,
  `ISSUE_DATE` date NOT NULL,
  `RETURN_DATE` date DEFAULT NULL,
  `FINE` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ISSUE_ID`,`USER_ID`,`BOOK_ID`,`ISSUE_DATE`),
  KEY `book_issued_ibfk_1` (`BOOK_ID`),
  CONSTRAINT `book_issued_ibfk_1` FOREIGN KEY (`BOOK_ID`) REFERENCES `library_books` (`BOOK_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_issued`
--

LOCK TABLES `book_issued` WRITE;
/*!40000 ALTER TABLE `book_issued` DISABLE KEYS */;
INSERT INTO `book_issued` VALUES (1,101,3,'The Great Gatsby',2,'2025-05-01','2025-06-10',20.00),(2,102,5,'The Catcher in the Rye',4,'2025-05-02','2025-05-16',0.00),(3,103,7,'Fahrenheit 451',2,'2025-05-03','2025-05-17',0.00),(4,104,2,'1948',1,'2025-05-04','2025-06-18',15.00),(5,105,1,'TO KILL A MOCKING BIRD',3,'2025-05-05','2025-05-19',0.00),(6,106,8,'Jane Eyre',1,'2025-05-06','2025-05-20',0.00),(7,107,10,'The Lord of the Rings',1,'2025-05-07','2025-06-26',20.00),(8,108,4,'Pride and Prejudice',1,'2025-05-08','2025-05-22',0.00),(9,109,6,'The Hobbit',2,'2025-05-09','2025-05-23',0.00),(10,110,9,'Animal Farm',5,'2025-05-10','2025-05-24',0.00);
/*!40000 ALTER TABLE `book_issued` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `library_books`
--

DROP TABLE IF EXISTS `library_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library_books` (
  `BOOK_ID` int NOT NULL AUTO_INCREMENT,
  `BOOK_TITLE` varchar(255) DEFAULT NULL,
  `BOOK_AUTHOR` varchar(255) DEFAULT NULL,
  `NUMBER_OF_COPIES_AVAILABLE` int DEFAULT NULL,
  PRIMARY KEY (`BOOK_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library_books`
--

LOCK TABLES `library_books` WRITE;
/*!40000 ALTER TABLE `library_books` DISABLE KEYS */;
INSERT INTO `library_books` VALUES (1,'TO KILL A MOCKING BIRD','HARPER LEE',5),(2,'1948','GEORGE ORWELL',3),(3,'The Great Gatsby','F. Scott Fitzgerald',4),(4,'Pride and Prejudice','Jane Austen',2),(5,'The Catcher in the Rye','J.D. Salinger',6),(6,'The Hobbit','J.R.R. Tolkien',5),(7,'Fahrenheit 451','Ray Bradbury',3),(8,'Jane Eyre','Charlotte Brontë',2),(9,'Animal Farm','George Orwell',7),(10,'The Lord of the Rings','J.R.R. Tolkien',1),(11,'Brave New World','Aldous Huxley',3),(12,'Wuthering Heights','Emily Brontë',4),(13,'The Chronicles of Narnia','C.S. Lewis',6),(14,'Crime and Punishment','Fyodor Dostoevsky',2),(15,'The Alchemist','Paulo Coelho',5),(16,'The Picture of Dorian Gray','Oscar Wilde',3),(17,'Moby Dick','Herman Melville',2),(18,'The Adventures of Huckleberry Finn','Mark Twain',4),(19,'A Tale of Two Cities','Charles Dickens',3),(20,'The Little Prince','Antoine de Saint-Exupéry',5);
/*!40000 ALTER TABLE `library_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `returned_books`
--

DROP TABLE IF EXISTS `returned_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `returned_books` (
  `ISSUE_ID` int NOT NULL,
  `USER_ID` int NOT NULL,
  `BOOK_ID` int NOT NULL,
  `BOOK_TITLE` varchar(255) DEFAULT NULL,
  `NUMBER_OF_COPIES_RETURNED` int NOT NULL DEFAULT '0',
  `ISSUE_DATE` date NOT NULL,
  `RETURN_DATE` date DEFAULT NULL,
  `FINE` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ISSUE_ID`,`USER_ID`,`BOOK_ID`,`ISSUE_DATE`),
  KEY `book_issued_ibfk_1` (`BOOK_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `returned_books`
--

LOCK TABLES `returned_books` WRITE;
/*!40000 ALTER TABLE `returned_books` DISABLE KEYS */;
/*!40000 ALTER TABLE `returned_books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-03 23:49:01
