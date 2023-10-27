-- MySQL dump 10.13  Distrib 5.7.28, for Win32 (AMD64)
--
-- Host: localhost    Database: confidential
-- ------------------------------------------------------
-- Server version	5.7.28-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `code` int(11) DEFAULT NULL,
  `gender` char(10) DEFAULT NULL,
  `designation` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1001,'male','vice principal'),(1009,'female','coordinator'),(1203,'female','coordinator'),(1045,'male','hod'),(1123,'male','senior teacher'),(1167,'male','senior teacher'),(1215,'male','hod');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `C_ID` int(11) DEFAULT NULL,
  `CLIENTNAME` varchar(20) DEFAULT NULL,
  `CITY` varchar(10) DEFAULT NULL,
  `P_ID` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'COSMETIC SHOP','DELHI','FW05'),(6,'TOTAL HEALTH','MUMBAI','BS01'),(12,'LIVE LIFE','DELHI','SH06'),(15,'PRETTY WOMAN','DELHI','FW12'),(16,'DREAMS','BANGALORE','TP01');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `id` int(11) DEFAULT NULL,
  `cname` char(20) DEFAULT NULL,
  `activation_date` date DEFAULT NULL,
  `validity` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `connection` char(10) DEFAULT NULL,
  KEY `customer_index` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (101,'preeti','2009-06-04',365,330,'hutch'),(102,'sumit','2008-02-12',60,180,'airtel'),(103,'aamir','2009-05-14',180,150,'aircel'),(104,'mukul','2008-01-30',30,100,'bsnl'),(105,'ambani','2007-03-08',365,310,'reliance'),(106,'rani','2009-04-02',90,210,'airtel'),(107,'vijay','2009-09-12',60,150,'bsnl');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `ID` int(11) DEFAULT NULL,
  `NAME` char(20) DEFAULT NULL,
  `DOJ` date DEFAULT NULL,
  `DEPT` char(20) DEFAULT NULL,
  `SEX` char(1) DEFAULT NULL,
  `QUALF` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (101,'Siddharth','2002-01-12','Sales','M','MBA'),(104,'Raghav','1988-05-08','Finance','M','CA'),(107,'Naman','1988-03-15','Research','M','MTECH'),(114,'Nupur','2003-02-01','Sales','F','MBA'),(109,'Janvi','2004-07-18','Finance','F','ICWA'),(105,'Rama','2007-04-14','Research','M','BTECH'),(117,'Jace','1987-06-27','Sales','F','MTECH'),(111,'Binoy','1990-01-12','Finance','M','CA'),(130,'Samuel','1999-01-20','Sales','M','MBA'),(112,'Shyam','2000-02-11','Research','M','MTECH');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fare`
--

DROP TABLE IF EXISTS `fare`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fare` (
  `fl_no` char(10) DEFAULT NULL,
  `airlines` char(20) DEFAULT NULL,
  `fare` int(11) DEFAULT NULL,
  `tax` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fare`
--

LOCK TABLES `fare` WRITE;
/*!40000 ALTER TABLE `fare` DISABLE KEYS */;
INSERT INTO `fare` VALUES ('IC701','indian airlines',6500,10),('MU499','sahara',9400,5),('AM501','jet airways',13450,8),('IC899','indian airlines',8300,4),('IC302','indian airlines',4300,9),('IC799','indian airlines',10500,10),('MC101','deccan airlines',3500,4);
/*!40000 ALTER TABLE `fare` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flight` (
  `fl_no` int(11) DEFAULT NULL,
  `departure` char(20) DEFAULT NULL,
  `arrival` char(20) DEFAULT NULL,
  `no_flights` int(11) DEFAULT NULL,
  `noofstops` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight1`
--

DROP TABLE IF EXISTS `flight1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flight1` (
  `fl_no` char(20) DEFAULT NULL,
  `departure` char(20) DEFAULT NULL,
  `arrival` char(20) DEFAULT NULL,
  `no_flights` int(11) DEFAULT NULL,
  `noofstops` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight1`
--

LOCK TABLES `flight1` WRITE;
/*!40000 ALTER TABLE `flight1` DISABLE KEYS */;
INSERT INTO `flight1` VALUES ('IC301','mumbai','delhi',8,0),('IC799','bangalore','delhi',2,1),('MC101','indore','mumbai',3,0),('IC302','delhi','mumbai',8,0),('AM812','kanpur','bangalore',3,1),('IC899','mumbai','kochi',1,4),('AM501','delhi','trivandrum',1,5),('MU499','mumbai','madras',3,3),('IC701','delhi','ahmedabad',4,0);
/*!40000 ALTER TABLE `flight1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobile`
--

DROP TABLE IF EXISTS `mobile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mobile` (
  `id` int(11) DEFAULT NULL,
  `make` char(10) DEFAULT NULL,
  `model_no` char(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobile`
--

LOCK TABLES `mobile` WRITE;
/*!40000 ALTER TABLE `mobile` DISABLE KEYS */;
INSERT INTO `mobile` VALUES (101,'nokia','N76'),(102,'LG','RD3500'),(104,'nokia','E61'),(105,'sony','K310i'),(107,'motorola','W756i');
/*!40000 ALTER TABLE `mobile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `P_ID` char(5) DEFAULT NULL,
  `PRODUCTNAME` varchar(15) DEFAULT NULL,
  `MANUFACTURER` varchar(4) DEFAULT NULL,
  `PRICE` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('TP01','TALCOM POWDER','LAK',50),('FW05','FACE WASH','ABC',55),('BS01','BATH SOAP','ABC',65),('SH06','SHAMPOO','XYZ',130),('FW12','FACE WASH','XYZ',105);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase`
--

DROP TABLE IF EXISTS `purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `purchase` (
  `bill_no` int(11) DEFAULT NULL,
  `name` varchar(25) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase`
--

LOCK TABLES `purchase` WRITE;
/*!40000 ALTER TABLE `purchase` DISABLE KEYS */;
INSERT INTO `purchase` VALUES (1111,'rajeev','2020-12-11',3568),(1160,'rajeev','2020-12-22',11685),(1005,'New India','2021-03-07',7500);
/*!40000 ALTER TABLE `purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `salary` (
  `ID` int(11) DEFAULT NULL,
  `BASIC` int(11) DEFAULT NULL,
  `ALLOWANCE` int(11) DEFAULT NULL,
  `COMM_PERC` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
INSERT INTO `salary` VALUES (101,15240,5400,3),(104,23000,1452,4),(107,14870,2451,3),(114,21000,3451,14),(109,24500,1452,10),(105,17000,1250,2),(117,12450,1400,3),(111,13541,3652,9),(130,25000,4785,15),(187,14823,5862,2);
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sales` (
  `c_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (0,'2020-12-19',9585),(0,'2020-12-20',2255),(101,'2020-12-22',1000),(101,'2020-12-22',5000),(0,'2020-12-22',530),(102,'2021-04-04',2000);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school`
--

DROP TABLE IF EXISTS `school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `school` (
  `code` int(11) DEFAULT NULL,
  `teachername` char(15) DEFAULT NULL,
  `subject` char(15) DEFAULT NULL,
  `DOJ` date DEFAULT NULL,
  `periods` int(11) DEFAULT NULL,
  `experience` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school`
--

LOCK TABLES `school` WRITE;
/*!40000 ALTER TABLE `school` DISABLE KEYS */;
INSERT INTO `school` VALUES (1001,'Ravi Shankar','english','2000-03-12',24,10),(1009,'priya rai','physics','1998-09-03',26,12),(1203,'lisa anand','english','2000-04-09',27,5),(1045,'yashraj','maths','2000-08-24',24,15),(1123,'gagan','physics','1999-07-16',28,3),(1167,'harish b','chemistry','1999-10-19',27,5),(1215,'umesh','physics','1998-05-11',22,16);
/*!40000 ALTER TABLE `school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff` (
  `ID` int(11) DEFAULT NULL,
  `NAME` char(20) DEFAULT NULL,
  `DOJ` date DEFAULT NULL,
  `DEPT` char(20) DEFAULT NULL,
  `SEX` char(1) DEFAULT NULL,
  `QUALF` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (101,'Siddharth','2002-01-12','Sales','M','MBA'),(104,'Raghav','1988-05-08','Finance','M','CA'),(107,'Naman','1988-05-14','Research','M','MTECH'),(114,'Nupur','2003-02-01','Sales','F','MBA'),(109,'Janvi','2004-07-18','Finance','F','ICWA'),(105,'Rama','2007-04-14','Research','M','BTECH'),(117,'Jace','1987-06-27','Sales','F','MTECH'),(111,'Binoy','1990-01-12','Finance','M','CA'),(130,'Samuel','1999-03-07','Sales','M','MBA'),(187,'Ragini','2002-12-12','Research','F','BTECH');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stock` (
  `item_code` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `quantity` decimal(9,4) DEFAULT NULL,
  `cost_price` int(11) DEFAULT NULL,
  `selling_price` int(11) DEFAULT NULL,
  `gst` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
INSERT INTO `stock` VALUES (1,'red gg',36.0000,500,700,18),(2,'black tkr',30.0000,625,910,18),(3,'navy blue',24.9000,250,460,12),(4,'yellow 5gll',38.0000,712,885,18),(6,'magenta mb',8.0000,250,500,12),(5,'red 5b',21.5000,225,400,18),(7,'brown mr',30.0000,140,200,18),(8,'orange bdc',28.0000,140,200,18),(9,'navy blue bt',25.0000,140,200,18),(10,'t blue h7g',22.0000,300,400,18),(11,'white lmps',40.0000,150,175,12),(12,'fluoroscent pink',32.0000,850,1077,12),(13,'violet bb',20.0000,350,450,18),(14,'golden yellow r',27.5000,225,300,18),(15,'t blue h2gp',34.0000,250,300,18),(16,'orange 3r',25.0000,250,300,18),(17,'congo red',22.0000,160,220,18),(18,'black e',28.0000,140,200,18),(19,'orange se',24.5000,200,300,18),(20,'yellow mgr',26.0000,600,800,18);
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `store` (
  `StoreID` char(5) DEFAULT NULL,
  `Name` char(15) DEFAULT NULL,
  `Location` char(15) DEFAULT NULL,
  `City` char(10) DEFAULT NULL,
  `No_Of_Employees` int(11) DEFAULT NULL,
  `Date_Opened` date DEFAULT NULL,
  `Sales_Amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store`
--

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES ('S101','Planetfashion','Karol Bagh','Delhi',7,'2015-10-16',300000),('S102','Trends','Nehru Nagar','Mumbai',11,'2015-08-09',400000),('S103','Vogue','Vikas Vihar','Delhi',10,'2015-06-27',200000),('S104','Superfashion','Defence Colony','Delhi',8,'2015-02-18',450000),('S105','Rage','Bandra','Mumbai',5,'2015-09-22',600000);
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `Roll_no` int(11) DEFAULT NULL,
  `Name` varchar(25) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Marks` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Ashutosh Rana',18,94),(2,'Bhanu Pratap',17,89),(3,'Bhavna Chaturvedi',17,95),(4,'Charan Singh',18,97),(5,'Dharmendra Gupta',17,98),(6,'Girish Chandra',18,96),(7,'Harshvardan Shringla',17,92),(8,'Ishan Kishan',17,88),(9,'Kishore Kumar',19,82),(10,'Manohar Parrikar',18,97),(11,'Naveen Patnaik',18,95);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-05  1:53:25
