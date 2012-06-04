-- MySQL dump 10.13  Distrib 5.5.15, for osx10.7 (i386)
--
-- Host: localhost    Database: ccbn
-- ------------------------------------------------------
-- Server version	5.5.15

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
-- Table structure for table `atencionintegral_becaprimaria`
--

DROP TABLE IF EXISTS `atencionintegral_becaprimaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `atencionintegral_becaprimaria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atencionintegral_becaprimaria`
--

LOCK TABLES `atencionintegral_becaprimaria` WRITE;
/*!40000 ALTER TABLE `atencionintegral_becaprimaria` DISABLE KEYS */;
INSERT INTO `atencionintegral_becaprimaria` VALUES (1,2012);
/*!40000 ALTER TABLE `atencionintegral_becaprimaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `atencionintegral_becasecundaria`
--

DROP TABLE IF EXISTS `atencionintegral_becasecundaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `atencionintegral_becasecundaria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atencionintegral_becasecundaria`
--

LOCK TABLES `atencionintegral_becasecundaria` WRITE;
/*!40000 ALTER TABLE `atencionintegral_becasecundaria` DISABLE KEYS */;
INSERT INTO `atencionintegral_becasecundaria` VALUES (1,2012);
/*!40000 ALTER TABLE `atencionintegral_becasecundaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `atencionintegral_becauniversitaria`
--

DROP TABLE IF EXISTS `atencionintegral_becauniversitaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `atencionintegral_becauniversitaria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atencionintegral_becauniversitaria`
--

LOCK TABLES `atencionintegral_becauniversitaria` WRITE;
/*!40000 ALTER TABLE `atencionintegral_becauniversitaria` DISABLE KEYS */;
INSERT INTO `atencionintegral_becauniversitaria` VALUES (1,2012);
/*!40000 ALTER TABLE `atencionintegral_becauniversitaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `permission_id_refs_id_a7792de1` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add Colegio/Centro de estudio',8,'add_colegio'),(23,'Can change Colegio/Centro de estudio',8,'change_colegio'),(24,'Can delete Colegio/Centro de estudio',8,'delete_colegio'),(25,'Can add Oficio/Profesión',9,'add_oficio'),(26,'Can change Oficio/Profesión',9,'change_oficio'),(27,'Can delete Oficio/Profesión',9,'delete_oficio'),(28,'Can add pariente',10,'add_pariente'),(29,'Can change pariente',10,'change_pariente'),(30,'Can delete pariente',10,'delete_pariente'),(31,'Can add persona',11,'add_persona'),(32,'Can change persona',11,'change_persona'),(33,'Can delete persona',11,'delete_persona'),(34,'Can add migration history',12,'add_migrationhistory'),(35,'Can change migration history',12,'change_migrationhistory'),(36,'Can delete migration history',12,'delete_migrationhistory'),(37,'Can add departamento',13,'add_departamento'),(38,'Can change departamento',13,'change_departamento'),(39,'Can delete departamento',13,'delete_departamento'),(40,'Can add municipio',14,'add_municipio'),(41,'Can change municipio',14,'change_municipio'),(42,'Can delete municipio',14,'delete_municipio'),(43,'Can add Ciudad/Comunidad',15,'add_ciudad'),(44,'Can change Ciudad/Comunidad',15,'change_ciudad'),(45,'Can delete Ciudad/Comunidad',15,'delete_ciudad'),(46,'Can add Barrio/Comarca',16,'add_barrio'),(47,'Can change Barrio/Comarca',16,'change_barrio'),(48,'Can delete Barrio/Comarca',16,'delete_barrio'),(49,'Can add Relación',17,'add_relacion'),(50,'Can change Relación',17,'change_relacion'),(51,'Can delete Relación',17,'delete_relacion'),(64,'Can add modulo persona',22,'add_modulopersona'),(65,'Can change modulo persona',22,'change_modulopersona'),(66,'Can delete modulo persona',22,'delete_modulopersona'),(67,'Can add modulo',23,'add_modulo'),(68,'Can change modulo',23,'change_modulo'),(69,'Can delete modulo',23,'delete_modulo'),(70,'Can add sub modulo',24,'add_submodulo'),(71,'Can change sub modulo',24,'change_submodulo'),(72,'Can delete sub modulo',24,'delete_submodulo'),(73,'Can add frecuencia',25,'add_frecuencia'),(74,'Can change frecuencia',25,'change_frecuencia'),(75,'Can delete frecuencia',25,'delete_frecuencia'),(76,'Can add curso',26,'add_curso'),(77,'Can change curso',26,'change_curso'),(78,'Can delete curso',26,'delete_curso'),(79,'Can add inscripcion curso',27,'add_inscripcioncurso'),(80,'Can change inscripcion curso',27,'change_inscripcioncurso'),(81,'Can delete inscripcion curso',27,'delete_inscripcioncurso'),(82,'Can add registro biblioteca',28,'add_registrobiblioteca'),(83,'Can change registro biblioteca',28,'change_registrobiblioteca'),(84,'Can delete registro biblioteca',28,'delete_registrobiblioteca'),(85,'Can add registro beca primaria',29,'add_registrobecaprimaria'),(86,'Can change registro beca primaria',29,'change_registrobecaprimaria'),(87,'Can delete registro beca primaria',29,'delete_registrobecaprimaria'),(88,'Can add registro beca secundaria',30,'add_registrobecasecundaria'),(89,'Can change registro beca secundaria',30,'change_registrobecasecundaria'),(90,'Can delete registro beca secundaria',30,'delete_registrobecasecundaria'),(91,'Can add registro beca universitaria',31,'add_registrobecauniversitaria'),(92,'Can change registro beca universitaria',31,'change_registrobecauniversitaria'),(93,'Can delete registro beca universitaria',31,'delete_registrobecauniversitaria'),(94,'Can add registro musica',32,'add_registromusica'),(95,'Can change registro musica',32,'change_registromusica'),(96,'Can delete registro musica',32,'delete_registromusica'),(97,'Can add registro teatro',33,'add_registroteatro'),(98,'Can change registro teatro',33,'change_registroteatro'),(99,'Can delete registro teatro',33,'delete_registroteatro'),(100,'Can add registro danza',34,'add_registrodanza'),(101,'Can change registro danza',34,'change_registrodanza'),(102,'Can delete registro danza',34,'delete_registrodanza'),(103,'Can add registro coro',35,'add_registrocoro'),(104,'Can change registro coro',35,'change_registrocoro'),(105,'Can delete registro coro',35,'delete_registrocoro'),(106,'Can add registro pintura',36,'add_registropintura'),(107,'Can change registro pintura',36,'change_registropintura'),(108,'Can delete registro pintura',36,'delete_registropintura'),(109,'Can add beca primaria',37,'add_becaprimaria'),(110,'Can change beca primaria',37,'change_becaprimaria'),(111,'Can delete beca primaria',37,'delete_becaprimaria'),(112,'Can add beca secundaria',38,'add_becasecundaria'),(113,'Can change beca secundaria',38,'change_becasecundaria'),(114,'Can delete beca secundaria',38,'delete_becasecundaria'),(115,'Can add beca universitaria',39,'add_becauniversitaria'),(116,'Can change beca universitaria',39,'change_becauniversitaria'),(117,'Can delete beca universitaria',39,'delete_becauniversitaria'),(118,'Can add actividad individual',40,'add_actividadindividual'),(119,'Can change actividad individual',40,'change_actividadindividual'),(120,'Can delete actividad individual',40,'delete_actividadindividual'),(121,'Can add consulta',41,'add_consulta'),(122,'Can change consulta',41,'change_consulta'),(123,'Can delete consulta',41,'delete_consulta'),(124,'Can add prestamo',42,'add_prestamo'),(125,'Can change prestamo',42,'change_prestamo'),(126,'Can delete prestamo',42,'delete_prestamo'),(127,'Can add retorno',43,'add_retorno'),(128,'Can change retorno',43,'change_retorno'),(129,'Can delete retorno',43,'delete_retorno'),(130,'Can add Servicio Bibliotecario',44,'add_servicio'),(131,'Can change Servicio Bibliotecario',44,'change_servicio'),(132,'Can delete Servicio Bibliotecario',44,'delete_servicio'),(133,'Can add actividad colectiva',45,'add_actividadcolectiva'),(134,'Can change actividad colectiva',45,'change_actividadcolectiva'),(135,'Can delete actividad colectiva',45,'delete_actividadcolectiva'),(136,'Can add Grupo de música',46,'add_musica'),(137,'Can change Grupo de música',46,'change_musica'),(138,'Can delete Grupo de música',46,'delete_musica'),(139,'Can add Grupo de teatro',47,'add_teatro'),(140,'Can change Grupo de teatro',47,'change_teatro'),(141,'Can delete Grupo de teatro',47,'delete_teatro'),(142,'Can add Grupo de danza',48,'add_danza'),(143,'Can change Grupo de danza',48,'change_danza'),(144,'Can delete Grupo de danza',48,'delete_danza'),(145,'Can add Grupo de coro',49,'add_coro'),(146,'Can change Grupo de coro',49,'change_coro'),(147,'Can delete Grupo de coro',49,'delete_coro'),(148,'Can add Grupo de pintura',50,'add_pintura'),(149,'Can change Grupo de pintura',50,'change_pintura'),(150,'Can delete Grupo de pintura',50,'delete_pintura'),(151,'Can add evento colectivo',51,'add_eventocolectivo'),(152,'Can change evento colectivo',51,'change_eventocolectivo'),(153,'Can delete evento colectivo',51,'delete_eventocolectivo'),(154,'Can add evento interno',52,'add_eventointerno'),(155,'Can change evento interno',52,'change_eventointerno'),(156,'Can delete evento interno',52,'delete_eventointerno'),(157,'Can add evento externo',53,'add_eventoexterno'),(158,'Can change evento externo',53,'change_eventoexterno'),(159,'Can delete evento externo',53,'delete_eventoexterno'),(160,'Can add salida',54,'add_salida'),(161,'Can change salida',54,'change_salida'),(162,'Can delete salida',54,'delete_salida'),(163,'Can add filter',55,'add_filter'),(164,'Can change filter',55,'change_filter'),(165,'Can delete filter',55,'delete_filter');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','','','h@g.com','pbkdf2_sha256$10000$aF2Gf1UdwEUj$NKhBs8VheBlyA3/YvWTaDuTz2fPhE9UMDODdV57w8+Q=',1,1,1,'2012-06-01 01:38:57','2012-03-27 22:23:45');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `group_id_refs_id_f0ee9890` (`group_id`),
  CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `permission_id_refs_id_67e79cb` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblioteca_actividadcolectiva`
--

DROP TABLE IF EXISTS `biblioteca_actividadcolectiva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `biblioteca_actividadcolectiva` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `actividad` int(11) NOT NULL,
  `ninos` int(11) NOT NULL DEFAULT '0',
  `ninas` int(11) NOT NULL DEFAULT '0',
  `jovenes_hombres` int(11) NOT NULL DEFAULT '0',
  `jovenes_mujeres` int(11) NOT NULL DEFAULT '0',
  `adultos_hombres` int(11) NOT NULL DEFAULT '0',
  `adultos_mujeres` int(11) NOT NULL DEFAULT '0',
  `evaluacion_rapida` longtext NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `comentarios` longtext NOT NULL,
  `acuerdos` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblioteca_actividadcolectiva`
--

LOCK TABLES `biblioteca_actividadcolectiva` WRITE;
/*!40000 ALTER TABLE `biblioteca_actividadcolectiva` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblioteca_actividadcolectiva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblioteca_actividadindividual`
--

DROP TABLE IF EXISTS `biblioteca_actividadindividual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `biblioteca_actividadindividual` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `persona_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `actividad` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `biblioteca_actividadindividual_e27cbd6d` (`persona_id`),
  CONSTRAINT `persona_id_refs_id_387c45e69be8b5fa` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblioteca_actividadindividual`
--

LOCK TABLES `biblioteca_actividadindividual` WRITE;
/*!40000 ALTER TABLE `biblioteca_actividadindividual` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblioteca_actividadindividual` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblioteca_consulta`
--

DROP TABLE IF EXISTS `biblioteca_consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `biblioteca_consulta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actividad_id` int(11) NOT NULL,
  `categoria` int(11) NOT NULL,
  `proposito` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `biblioteca_consulta_761ba4b0` (`actividad_id`),
  CONSTRAINT `actividad_id_refs_id_77d50960f4dbcd1d` FOREIGN KEY (`actividad_id`) REFERENCES `biblioteca_actividadindividual` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblioteca_consulta`
--

LOCK TABLES `biblioteca_consulta` WRITE;
/*!40000 ALTER TABLE `biblioteca_consulta` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblioteca_consulta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblioteca_prestamo`
--

DROP TABLE IF EXISTS `biblioteca_prestamo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `biblioteca_prestamo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actividad_id` int(11) NOT NULL,
  `registro_libro_prestar` varchar(50) NOT NULL,
  `dias` int(11) NOT NULL,
  `fecha_retorno` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `biblioteca_prestamo_761ba4b0` (`actividad_id`),
  CONSTRAINT `actividad_id_refs_id_127d8fba16d30bb1` FOREIGN KEY (`actividad_id`) REFERENCES `biblioteca_actividadindividual` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblioteca_prestamo`
--

LOCK TABLES `biblioteca_prestamo` WRITE;
/*!40000 ALTER TABLE `biblioteca_prestamo` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblioteca_prestamo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblioteca_retorno`
--

DROP TABLE IF EXISTS `biblioteca_retorno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `biblioteca_retorno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actividad_id` int(11) NOT NULL,
  `registro_libro_retorno` varchar(50) NOT NULL,
  `dias_mora` int(11) NOT NULL,
  `fecha_retorno` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `biblioteca_retorno_761ba4b0` (`actividad_id`),
  CONSTRAINT `actividad_id_refs_id_42ce2102392dcce2` FOREIGN KEY (`actividad_id`) REFERENCES `biblioteca_actividadindividual` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblioteca_retorno`
--

LOCK TABLES `biblioteca_retorno` WRITE;
/*!40000 ALTER TABLE `biblioteca_retorno` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblioteca_retorno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblioteca_servicio`
--

DROP TABLE IF EXISTS `biblioteca_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `biblioteca_servicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actividad_id` int(11) NOT NULL,
  `capacidad_tecnica` int(11) NOT NULL,
  `compromiso_social` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `biblioteca_servicio_761ba4b0` (`actividad_id`),
  CONSTRAINT `actividad_id_refs_id_2c1a9abd11a63cc6` FOREIGN KEY (`actividad_id`) REFERENCES `biblioteca_actividadindividual` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblioteca_servicio`
--

LOCK TABLES `biblioteca_servicio` WRITE;
/*!40000 ALTER TABLE `biblioteca_servicio` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblioteca_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `content_type_id_refs_id_288599e6` (`content_type_id`),
  KEY `user_id_refs_id_c8665aa` (`user_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=207 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2012-04-11 15:28:32',1,10,'1','Papa',1,''),(2,'2012-04-11 15:28:37',1,10,'2','Mama',1,''),(3,'2012-04-11 15:28:40',1,10,'3','Abuelo',1,''),(4,'2012-04-11 15:28:44',1,10,'4','Abuela',1,''),(5,'2012-04-11 22:59:17',1,15,'1','Cualquiera',1,''),(6,'2012-04-11 22:59:31',1,16,'1','La concha',1,''),(7,'2012-04-11 23:00:48',1,9,'1','Carpintero',1,''),(8,'2012-04-11 23:01:02',1,11,'1','Persona object',1,''),(9,'2012-04-11 23:03:34',1,11,'2','Persona object',1,''),(10,'2012-04-12 15:39:41',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Changed cedula.'),(11,'2012-04-12 15:49:06',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Changed cedula. Added Relación \"Relacion object\".'),(12,'2012-04-12 15:49:19',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Changed parentesco for Relación \"Relacion object\".'),(13,'2012-04-12 15:50:22',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Deleted Relación \"None\".'),(14,'2012-04-12 15:50:35',1,11,'2','Mariana Lucia Blanco ',2,'Added Relación \"14\".'),(15,'2012-04-12 15:54:18',1,11,'2','Mariana Lucia Blanco ',2,'Changed parentesco for Relación \"14\".'),(16,'2012-04-12 16:10:26',1,11,'2','Mariana Lucia Blanco ',2,'Changed parentesco for Relación \"14\".'),(17,'2012-04-12 16:11:05',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Deleted Relación \"None\".'),(18,'2012-04-12 16:11:11',1,11,'2','Mariana Lucia Blanco ',2,'Deleted Relación \"None\".'),(19,'2012-04-12 16:40:31',1,11,'2','Mariana Lucia Blanco ',2,'Added Relación \"831\".'),(20,'2012-04-12 16:41:16',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Changed parentesco for Relación \"832\".'),(21,'2012-04-12 16:42:59',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Changed parentesco for Relación \"832\".'),(22,'2012-04-12 16:43:14',1,11,'2','Mariana Lucia Blanco ',2,'Changed parentesco for Relación \"831\".'),(23,'2012-04-12 16:44:49',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Changed parentesco for Relación \"832\".'),(24,'2012-04-12 16:46:40',1,11,'2','Mariana Lucia Blanco ',2,'Changed parentesco for Relación \"831\".'),(25,'2012-04-12 16:46:50',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Changed parentesco for Relación \"832\".'),(26,'2012-04-12 16:48:17',1,11,'2','Mariana Lucia Blanco ',2,'Changed parentesco for Relación \"831\".'),(27,'2012-04-12 16:52:22',1,11,'3','Madian Tatiana Giacoman ',1,''),(28,'2012-04-12 16:52:37',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Changed parentesco for Relación \"832\".'),(41,'2012-04-13 22:31:31',1,23,'1','Formación',1,''),(42,'2012-04-13 22:31:39',1,23,'2','Formación Artística',1,''),(43,'2012-04-13 22:31:43',1,23,'3','Biblioteca',1,''),(44,'2012-04-13 22:31:48',1,23,'4','Promoción Artística',1,''),(45,'2012-04-13 22:31:53',1,23,'5','Prevencion de Violencia Interna',1,''),(46,'2012-04-13 22:31:56',1,23,'6','Prevención de Violencia Externa',1,''),(47,'2012-04-13 22:32:09',1,24,'1','Formación Educación Básica',1,''),(48,'2012-04-13 22:32:17',1,24,'2','Formación Formación Técnica Vocacional',1,''),(49,'2012-04-13 22:32:25',1,24,'3','Formación Formación Artística',1,''),(50,'2012-04-13 22:32:46',1,23,'2','Atención Integral',2,'Changed nombre.'),(51,'2012-04-13 22:33:18',1,24,'4','Atención Integral Beca Primaria',1,''),(52,'2012-04-13 22:33:35',1,24,'5','Atención Integral Beca Secundaria',1,''),(53,'2012-04-13 22:33:40',1,24,'6','Atención Integral Beca Universitaria',1,''),(54,'2012-04-13 22:33:45',1,24,'7','Atención Integral Familia',1,''),(55,'2012-04-13 22:33:52',1,24,'8','Biblioteca Biblioteca',1,''),(56,'2012-04-13 22:34:03',1,24,'9','Promoción Artística Música',1,''),(57,'2012-04-13 22:34:09',1,24,'10','Promoción Artística Teatro',1,''),(58,'2012-04-13 22:34:14',1,24,'11','Promoción Artística Danza',1,''),(59,'2012-04-13 22:34:22',1,24,'12','Promoción Artística Coro',1,''),(60,'2012-04-13 22:34:30',1,24,'13','Promoción Artística Pintura',1,''),(61,'2012-04-13 22:54:04',1,23,'1','Formación',2,'Changed code.'),(62,'2012-04-13 22:54:17',1,23,'2','Atención Integral',2,'Changed code.'),(63,'2012-04-13 22:55:10',1,23,'1','Formación',2,'Changed code.'),(64,'2012-04-13 22:55:15',1,23,'2','Atención Integral',2,'Changed code.'),(65,'2012-04-13 22:55:23',1,23,'3','Biblioteca',2,'Changed code.'),(66,'2012-04-13 22:55:30',1,23,'4','Promoción Artística',2,'Changed code.'),(67,'2012-04-13 22:55:36',1,23,'5','Prevencion de Violencia Interna',2,'Changed code.'),(68,'2012-04-13 22:55:43',1,23,'6','Prevención de Violencia Externa',2,'Changed code.'),(69,'2012-04-16 23:09:54',1,25,'1','Lunes a Viernes',1,''),(70,'2012-04-16 23:10:04',1,25,'2','Sabado y Domingo',1,''),(71,'2012-04-17 16:31:21',1,26,'1','Belleza General',1,''),(72,'2012-04-17 16:46:02',1,26,'2','Carpinteria',1,''),(73,'2012-04-17 16:48:23',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Added inscripcion curso \"1\".'),(74,'2012-04-17 16:50:26',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Changed curso for inscripcion curso \"1\".'),(75,'2012-04-17 17:18:45',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"2\" inscripcion curso.'),(76,'2012-04-17 17:19:31',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Eliminado/a \"None\" inscripcion curso.'),(77,'2012-04-17 17:27:39',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"3\" inscripcion curso.'),(78,'2012-04-17 17:36:25',1,11,'1','Helmy Roberto Giacoman Blanco',2,'No ha cambiado ningún campo.'),(79,'2012-04-17 17:50:15',1,24,'1','Educación Básica',2,'Modificado/a code.'),(80,'2012-04-17 17:50:24',1,24,'2','Formación Técnica Vocacional',2,'Modificado/a code.'),(81,'2012-04-17 17:50:33',1,24,'3','Formación Artística',2,'Modificado/a code.'),(82,'2012-04-17 17:52:14',1,26,'1','Belleza General - 17/04/2012 - Lunes a Viernes - Matutino',2,'Modificado/a submodulo.'),(83,'2012-04-17 17:54:44',1,26,'1','Belleza General - 17/04/2012 - Lunes a Viernes - Matutino',2,'Modificado/a submodulo.'),(84,'2012-04-17 17:58:29',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"4\" inscripcion curso.'),(85,'2012-04-17 17:59:06',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Eliminado/a \"None\" inscripcion curso.'),(86,'2012-04-18 16:36:49',1,23,'1','Formación',2,'Modificados inline para \"Educación Básica\" sub modulo. Modificados inline para \"Formación Técnica Vocacional\" sub modulo. Modificados inline para \"Formación Artística\" sub modulo.'),(87,'2012-04-18 21:59:44',1,24,'1','Educación Básica',2,'Modificado/a inline.'),(88,'2012-04-18 21:59:49',1,24,'2','Formación Técnica Vocacional',2,'Modificado/a inline.'),(89,'2012-04-18 22:37:25',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"<bound method Persona.__unicode__ of <Persona: Helmy Roberto Giacoman Blanco>>\" modulo persona.'),(90,'2012-04-19 16:51:35',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(91,'2012-04-19 16:51:44',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(92,'2012-04-19 16:52:02',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(93,'2012-04-19 16:52:10',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(94,'2012-04-19 16:53:18',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(95,'2012-04-19 19:27:41',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Eliminado/a \"None\" inscripcion curso.'),(96,'2012-04-19 19:29:10',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"4\" inscripcion curso.'),(97,'2012-04-19 19:29:26',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Eliminado/a \"None\" inscripcion curso.'),(98,'2012-04-19 19:29:36',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"5\" inscripcion curso.'),(99,'2012-04-19 20:24:16',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Eliminado/a \"None\" inscripcion curso.'),(100,'2012-04-19 20:43:58',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(101,'2012-04-19 20:44:17',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(102,'2012-04-19 20:44:45',1,26,'2','Curso Tecnico - Carpinteria - 17/04/2012 - Sabado y Domingo - Vespertino',2,'Modificado/a nombre.'),(103,'2012-04-19 20:44:56',1,26,'1','Curso Basicp - Belleza General - 17/04/2012 - Lunes a Viernes - Matutino',2,'Modificado/a nombre.'),(104,'2012-04-19 21:21:06',1,11,'4','Testin  This ',1,''),(105,'2012-04-19 21:24:13',1,11,'4','Testin  This ',2,'Modificados formacion para \"2\" modulo persona.'),(106,'2012-04-19 21:27:40',1,11,'4','Testin  This ',3,''),(107,'2012-04-19 21:27:54',1,11,'5','Testin  This ',1,''),(108,'2012-04-19 21:36:46',1,11,'5','Testin  This ',2,'Modificados formacion para \"3\" modulo persona.'),(109,'2012-04-19 21:38:27',1,11,'5','Testin  This ',2,'Modificados formacion para \"3\" modulo persona.'),(110,'2012-04-19 21:39:04',1,11,'5','Testin  This ',2,'Modificados formacion para \"3\" modulo persona.'),(111,'2012-04-19 21:40:07',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados parentesco para \"832\" Relación.'),(112,'2012-04-19 21:41:59',1,11,'2','Mariana Lucia Blanco ',2,'Añadido/a \"4\" modulo persona.'),(113,'2012-04-19 21:42:19',1,11,'2','Mariana Lucia Blanco ',2,'Modificados parentesco para \"831\" Relación.'),(114,'2012-04-19 21:45:00',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"837\" Relación.'),(115,'2012-04-19 21:48:14',1,11,'5','Testin  This ',3,''),(116,'2012-04-19 21:50:08',1,11,'1','Helmy Roberto Giacoman Blanco',2,'No ha cambiado ningún campo.'),(117,'2012-04-19 21:50:27',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(118,'2012-04-19 21:50:38',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(119,'2012-04-19 21:51:33',1,11,'1','Helmy Roberto Giacoman Blanco',2,'No ha cambiado ningún campo.'),(120,'2012-04-19 21:51:50',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(121,'2012-04-19 21:52:05',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(122,'2012-04-19 22:00:33',1,11,'2','Mariana Lucia Blanco ',2,'Modificados formacion para \"4\" modulo persona.'),(123,'2012-04-19 22:00:45',1,11,'2','Mariana Lucia Blanco ',2,'Añadido/a \"6\" inscripcion curso.'),(124,'2012-04-19 22:18:17',1,26,'2','Curso Tecnico - Carpinteria - 17/04/2012 - Sabado y Domingo - Vespertino',2,'No ha cambiado ningún campo.'),(125,'2012-04-19 22:18:26',1,26,'1','Curso Basico - Belleza General - 17/04/2012 - Lunes a Viernes - Matutino',2,'Modificado/a nombre.'),(126,'2012-04-19 22:23:46',1,26,'2','Curso Tecnico - Carpinteria - 17/04/2012 - Sabado y Domingo - Vespertino',2,'Eliminado/a \"\" inscripcion curso.'),(127,'2012-04-19 22:24:04',1,11,'2','Mariana Lucia Blanco ',2,'Añadido/a \"\" inscripcion curso.'),(128,'2012-04-20 22:00:49',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion para \"1\" modulo persona.'),(129,'2012-04-20 22:01:07',1,24,'3','Formación Artística',2,'Modificado/a inline.'),(130,'2012-04-27 02:13:53',1,24,'8','Biblioteca',2,'Modificado/a code y inline.'),(131,'2012-04-27 02:14:14',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados biblioteca para \"1\" modulo persona.'),(132,'2012-04-27 02:51:05',1,24,'4','Beca Primaria',2,'Modificado/a code y inline.'),(133,'2012-04-27 02:51:15',1,24,'5','Beca Secundaria',2,'Modificado/a code y inline.'),(134,'2012-04-27 02:51:28',1,24,'6','Beca Universitaria',2,'Modificado/a code y inline.'),(135,'2012-04-27 02:51:56',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados atencion_integral para \"1\" modulo persona.'),(136,'2012-04-27 03:07:59',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados atencion_integral para \"1\" modulo persona.'),(137,'2012-04-27 03:11:29',1,11,'1','Helmy Roberto Giacoman Blanco',2,'No ha cambiado ningún campo.'),(138,'2012-04-27 03:17:08',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados atencion_integral y promocion_artistica para \"1\" modulo persona.'),(139,'2012-04-27 03:18:54',1,24,'9','Música',2,'Modificado/a code y inline.'),(140,'2012-04-27 03:21:33',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados atencion_integral para \"1\" modulo persona.'),(141,'2012-04-27 03:28:03',1,24,'10','Teatro',2,'Modificado/a code y inline.'),(142,'2012-04-27 03:28:10',1,24,'11','Danza',2,'Modificado/a code y inline.'),(143,'2012-04-27 03:29:42',1,24,'12','Coro',2,'Modificado/a code y inline.'),(144,'2012-04-27 03:29:50',1,24,'13','Pintura',2,'Modificado/a code y inline.'),(145,'2012-04-27 03:51:20',1,37,'1','Beca del año 2012',1,''),(146,'2012-04-27 03:51:57',1,38,'1','Becados del 2012',1,''),(147,'2012-04-27 03:52:05',1,39,'1','Becados del 2012',1,''),(148,'2012-04-27 04:04:57',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"2012\" registro beca primaria.'),(149,'2012-04-27 04:39:19',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"\" registro beca secundaria. Añadido/a \"\" registro beca universitaria.'),(150,'2012-04-27 17:38:19',1,40,'1','Registro el 2012-04-27 11:38:16-05:00',1,''),(151,'2012-04-27 17:41:48',1,40,'1','Registro el 2012-04-27 11:38:16-05:00',2,'Modificado/a actividad.'),(152,'2012-04-27 17:41:57',1,40,'1','Registro el 2012-04-27 11:38:16-05:00',2,'Modificado/a actividad.'),(153,'2012-04-27 17:42:06',1,40,'1','Registro el 2012-04-27 11:38:16-05:00',2,'Modificado/a actividad.'),(154,'2012-04-27 17:42:09',1,40,'1','Registro el 2012-04-27 11:38:16-05:00',2,'Modificado/a actividad.'),(155,'2012-04-27 21:04:32',1,40,'1','Registro el 2012-04-27 11:38:16-05:00',2,'Modificado/a actividad.'),(156,'2012-04-30 20:49:40',1,46,'2','Musica 1 2012',1,''),(157,'2012-04-30 20:50:01',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"\" registro musica.'),(158,'2012-04-30 20:50:17',1,11,'1','Helmy Roberto Giacoman Blanco',2,'No ha cambiado ningún campo.'),(159,'2012-04-30 21:13:23',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados promocion_artistica para \"1\" modulo persona.'),(160,'2012-05-02 21:10:13',1,24,'14','Prevencion de Violencia Interna',1,''),(161,'2012-05-02 21:10:29',1,24,'15','Prevención de Violencia Externa',1,''),(162,'2012-05-02 21:10:38',1,24,'14','Prevencion de Violencia Interna',2,'Modificado/a code.'),(163,'2012-05-02 21:10:53',1,24,'15','Prevención de Violencia Externa',2,'Modificado/a code.'),(164,'2012-05-02 21:11:04',1,24,'14','Prevención de Violencia Interna',2,'Modificado/a nombre.'),(165,'2012-05-03 15:29:27',1,15,'2','Managua',1,''),(166,'2012-05-03 15:29:58',1,16,'2','Bosque de Altamira',1,''),(167,'2012-05-03 15:31:27',1,9,'2','Asalriado ONG',1,''),(168,'2012-05-03 15:31:59',1,9,'3','Asalariado ONG',1,''),(169,'2012-05-03 15:32:03',1,9,'3','Asalariado ONG',2,'No ha cambiado ningún campo.'),(170,'2012-05-03 15:32:12',1,9,'3','Asalariado ONG',3,''),(171,'2012-05-03 15:33:57',1,10,'5','Hijos',1,''),(172,'2012-05-03 15:34:34',1,10,'6','Esposo/a',1,''),(173,'2012-05-03 15:36:44',1,11,'4','Falguni  Guharay ',1,''),(174,'2012-05-03 15:37:01',1,11,'4','Falguni  Guharay ',2,'No ha cambiado ningún campo.'),(175,'2012-05-03 15:38:52',1,40,'2','Registro el 2012-05-03 09:39:31-05:00',1,''),(176,'2012-05-03 15:42:40',1,40,'2','Registro el 2012-05-03 09:39:31-05:00',2,'Añadido/a \"1\" prestamo.'),(177,'2012-05-03 15:46:45',1,40,'3','Registro el 2012-05-03 09:46:46-05:00',1,''),(178,'2012-05-03 15:50:14',1,40,'3','Registro el 2012-05-03 09:46:46-05:00',2,'Añadido/a \"1\" retorno.'),(179,'2012-05-03 15:53:26',1,11,'4','Falguni  Guharay ',2,'Modificados promocion_artistica para \"5\" modulo persona.'),(180,'2012-05-03 15:55:20',1,46,'3','Musica 2 2012',1,''),(181,'2012-05-03 15:55:29',1,11,'4','Falguni  Guharay ',2,'Añadido/a \"\" registro musica.'),(182,'2012-05-03 16:02:01',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Añadido/a \"\" registro musica.'),(183,'2012-06-01 03:24:15',1,54,'1','1',1,''),(184,'2012-06-01 03:56:24',1,54,'1','1',2,'Modificado/a model.'),(185,'2012-06-02 15:59:35',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados formacion, atencion_integral y promocion_artistica para \"1\" modulo persona.'),(186,'2012-06-02 16:03:22',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados atencion_integral para \"1\" modulo persona.'),(187,'2012-06-02 16:03:32',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Eliminado/a \"\" registro beca secundaria.'),(188,'2012-06-02 16:04:46',1,40,'4','Registro el 2012-06-02 10:04:38-05:00',1,''),(189,'2012-06-02 16:05:14',1,40,'4','Registro el 2012-06-02 15:04:38+00:00',3,''),(190,'2012-06-02 16:05:38',1,40,'5','Registro el 2012-06-02 10:05:30-05:00',1,''),(191,'2012-06-02 16:05:55',1,40,'5','Registro el 2012-06-02 15:05:30+00:00',3,''),(192,'2012-06-02 16:06:35',1,40,'3','Registro el 2012-05-03 14:46:46+00:00',3,''),(193,'2012-06-02 16:07:33',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados promocion_artistica para \"1\" modulo persona.'),(194,'2012-06-02 16:07:46',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados promocion_artistica para \"1\" modulo persona.'),(195,'2012-06-04 04:36:22',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados atencion_integral para \"1\" modulo persona.'),(196,'2012-06-04 04:36:35',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados atencion_integral, pv_interna y pv_externa para \"1\" modulo persona.'),(197,'2012-06-04 04:36:41',1,11,'1','Helmy Roberto Giacoman Blanco',2,'Modificados pv_interna y pv_externa para \"1\" modulo persona.'),(198,'2012-06-04 04:43:43',1,40,'6','Registro el 2012-06-03 22:43:41-05:00',1,''),(199,'2012-06-04 04:43:48',1,40,'6','Registro el 2012-06-03 22:43:41-05:00',2,'Modificado/a actividad.'),(200,'2012-06-04 04:43:55',1,40,'6','Registro el 2012-06-04 03:43:41+00:00',3,''),(201,'2012-06-04 04:45:10',1,40,'1','Registro el 2012-04-27 11:38:16-05:00',2,'Modificado/a actividad.'),(202,'2012-06-04 04:47:36',1,11,'1','Helmy Roberto Giacoman Blanco',2,'No ha cambiado ningún campo.'),(203,'2012-06-04 04:50:55',1,11,'1','Helmy Roberto Giacoman Blanco',3,''),(204,'2012-06-04 04:50:55',1,11,'2','Mariana Lucia Blanco ',3,''),(205,'2012-06-04 04:50:55',1,11,'3','Madian Tatiana Giacoman ',3,''),(206,'2012-06-04 04:50:55',1,11,'4','Falguni  Guharay ',3,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'Colegio/Centro de estudio','registro','colegio'),(9,'Oficio/Profesión','registro','oficio'),(10,'pariente','registro','pariente'),(11,'persona','registro','persona'),(12,'migration history','south','migrationhistory'),(13,'departamento','lugar','departamento'),(14,'municipio','lugar','municipio'),(15,'Ciudad/Comunidad','lugar','ciudad'),(16,'Barrio/Comarca','lugar','barrio'),(17,'Relación','registro','relacion'),(22,'modulo persona','registro','modulopersona'),(23,'modulo','sistema','modulo'),(24,'sub modulo','sistema','submodulo'),(25,'frecuencia','formacion','frecuencia'),(26,'curso','formacion','curso'),(27,'inscripcion curso','registro','inscripcioncurso'),(28,'registro biblioteca','registro','registrobiblioteca'),(29,'registro beca primaria','registro','registrobecaprimaria'),(30,'registro beca secundaria','registro','registrobecasecundaria'),(31,'registro beca universitaria','registro','registrobecauniversitaria'),(32,'registro musica','registro','registromusica'),(33,'registro teatro','registro','registroteatro'),(34,'registro danza','registro','registrodanza'),(35,'registro coro','registro','registrocoro'),(36,'registro pintura','registro','registropintura'),(37,'beca primaria','atencionintegral','becaprimaria'),(38,'beca secundaria','atencionintegral','becasecundaria'),(39,'beca universitaria','atencionintegral','becauniversitaria'),(40,'actividad individual','biblioteca','actividadindividual'),(41,'consulta','biblioteca','consulta'),(42,'prestamo','biblioteca','prestamo'),(43,'retorno','biblioteca','retorno'),(44,'Servicio Bibliotecario','biblioteca','servicio'),(45,'actividad colectiva','biblioteca','actividadcolectiva'),(46,'Grupo de música','promocion','musica'),(47,'Grupo de teatro','promocion','teatro'),(48,'Grupo de danza','promocion','danza'),(49,'Grupo de coro','promocion','coro'),(50,'Grupo de pintura','promocion','pintura'),(51,'evento colectivo','promocion','eventocolectivo'),(52,'evento interno','prevencion','eventointerno'),(53,'evento externo','prevencion','eventoexterno'),(54,'salida','sistema','salida'),(55,'filter','sistema','filter');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('181bedffec3eba6e0c69c2517963bb04','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-06-15 01:38:57'),('1f74df00fedcddea17d75dfd70b78baa','ODk0M2QxMzczMGMzMmFjZjJjYjFiMzAxMjQ3ZDUwMmQ0YzJhNzBjMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-05-11 23:04:30'),('21eb6629a1414cba912117c24168ce1e','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-11 02:23:15'),('3089311b3ed1c6adc0b3976786ef2ead','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-03 19:42:18'),('5ea3aca7461ce48931491f44f001ae4d','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-01 17:26:24'),('71db8b3b134d1d1fc152e5232af8ad52','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-08 18:03:15'),('734f8090cb0df52f6ab87f0ade565ae8','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-04-26 15:18:14'),('7b4e0af0409cf4df41a1806a1dc55c90','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-03 20:16:52'),('8096ea5d32ed7e23de8ca621146884bd','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-14 15:39:16'),('88a767d00dace80775019eed90cbc170','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-04-10 22:24:03'),('8bc4eefb28af9d061e07146f1b43f6ad','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-11 02:08:24'),('93948d61d7afc538955cee176aff6aa4','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-04-25 15:04:36'),('cd51eb22980be65cb7d01bb538eabdc1','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-04-27 21:35:32'),('dca9b5254d5cbd78285d633eeaf18c8a','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-17 15:15:46'),('ef16b7ebcf9ec594a8b3ee11e6e47a2f','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-04 21:01:19'),('f15a0f7abc3246133e72ae80ea6a0615','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-11 21:03:37'),('f15b6660055a7773ce39687bfa00f04f','MmZlNWVmOTA5MTAxODMyZGNjYzcyOWNiOWNlYTc4MzdiMjIzNTQ5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-05-11 16:46:32');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formacion_curso`
--

DROP TABLE IF EXISTS `formacion_curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `formacion_curso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `frecuencia_id` int(11) NOT NULL,
  `horario` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `submodulo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `formacion_curso_5a6c447` (`frecuencia_id`),
  KEY `formacion_curso_d8372a81` (`submodulo_id`),
  CONSTRAINT `frecuencia_id_refs_id_1ee61a59ade1d085` FOREIGN KEY (`frecuencia_id`) REFERENCES `formacion_frecuencia` (`id`),
  CONSTRAINT `submodulo_id_refs_id_5adb14fba8c8cecf` FOREIGN KEY (`submodulo_id`) REFERENCES `sistema_submodulo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formacion_curso`
--

LOCK TABLES `formacion_curso` WRITE;
/*!40000 ALTER TABLE `formacion_curso` DISABLE KEYS */;
INSERT INTO `formacion_curso` VALUES (1,'Curso Basico - Belleza General',1,1,'2012-04-17','2012-04-17',1),(2,'Curso Tecnico - Carpinteria',2,2,'2012-04-17','2012-04-17',2);
/*!40000 ALTER TABLE `formacion_curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formacion_frecuencia`
--

DROP TABLE IF EXISTS `formacion_frecuencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `formacion_frecuencia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(300) NOT NULL,
  `cantidad` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formacion_frecuencia`
--

LOCK TABLES `formacion_frecuencia` WRITE;
/*!40000 ALTER TABLE `formacion_frecuencia` DISABLE KEYS */;
INSERT INTO `formacion_frecuencia` VALUES (1,'Lunes a Viernes',5),(2,'Sabado y Domingo',2);
/*!40000 ALTER TABLE `formacion_frecuencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_barrio`
--

DROP TABLE IF EXISTS `lugar_barrio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_barrio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ciudad_id` int(11) NOT NULL,
  `tipo` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lugar_barrio_4e8eecfa` (`ciudad_id`),
  CONSTRAINT `ciudad_id_refs_id_13a8404ca948bf24` FOREIGN KEY (`ciudad_id`) REFERENCES `lugar_ciudad` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_barrio`
--

LOCK TABLES `lugar_barrio` WRITE;
/*!40000 ALTER TABLE `lugar_barrio` DISABLE KEYS */;
INSERT INTO `lugar_barrio` VALUES (1,1,1,'La concha'),(2,2,1,'Bosque de Altamira');
/*!40000 ALTER TABLE `lugar_barrio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_ciudad`
--

DROP TABLE IF EXISTS `lugar_ciudad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_ciudad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `municipio_id` int(11) NOT NULL,
  `tipo` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lugar_ciudad_f3143aaa` (`municipio_id`),
  CONSTRAINT `municipio_id_refs_id_a7c34c01bdcac0d` FOREIGN KEY (`municipio_id`) REFERENCES `lugar_municipio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_ciudad`
--

LOCK TABLES `lugar_ciudad` WRITE;
/*!40000 ALTER TABLE `lugar_ciudad` DISABLE KEYS */;
INSERT INTO `lugar_ciudad` VALUES (1,5010,1,'Cualquiera'),(2,5525,1,'Managua');
/*!40000 ALTER TABLE `lugar_ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_departamento`
--

DROP TABLE IF EXISTS `lugar_departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_departamento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_departamento`
--

LOCK TABLES `lugar_departamento` WRITE;
/*!40000 ALTER TABLE `lugar_departamento` DISABLE KEYS */;
INSERT INTO `lugar_departamento` VALUES (5,'Nueva Segovia','Nueva-segovia',3491.28),(10,'Jinotega','jinotega',9222.40),(20,'Madriz','madriz',1708.23),(25,'Estelí','esteli',2229.69),(30,'Chinandega','chinandega',4822.46),(35,'León','leon',5138.03),(40,'Matagalpa','matagalpa',6803.86),(50,'Boaco','boaco',4176.68),(55,'Managua','managua',3465.10),(60,'Masaya','masaya',610.78),(65,'Chontales','chontales',6481.27),(70,'Granada','granada',1039.68),(75,'Carazo','carazo',1081.40),(80,'Rivas','rivas',2161.82),(85,'Rí­o San Juan','Rio-san-juan',7540.90),(91,'RAAN','RAAN',32819.68),(93,'RAAS','RAAS',27546.32),(99,'Cobertura Nacional','cobertura-nacional',333333.00);
/*!40000 ALTER TABLE `lugar_departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_municipio`
--

DROP TABLE IF EXISTS `lugar_municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_municipio` (
  `id` int(11) NOT NULL,
  `departamento_id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  `latitud` decimal(8,5) DEFAULT NULL,
  `longitud` decimal(8,5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`),
  KEY `lugar_municipio_8865b15a` (`departamento_id`),
  CONSTRAINT `departamento_id_refs_id_12587f4246f972f5` FOREIGN KEY (`departamento_id`) REFERENCES `lugar_departamento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_municipio`
--

LOCK TABLES `lugar_municipio` WRITE;
/*!40000 ALTER TABLE `lugar_municipio` DISABLE KEYS */;
INSERT INTO `lugar_municipio` VALUES (505,5,'Jalapa','jalapa',0.00,13.92286,-86.12520),(510,5,'Murra','murra',0.00,13.75900,-86.01799),(515,5,'El Jí­caro','El-jicaro',0.00,13.72326,-86.13705),(520,5,'San Fernando','San-fernando',0.00,13.67729,-86.31484),(525,5,'Mozonte','mozonte',0.00,13.66168,-86.43706),(530,5,'Dipilto','dipilto',0.00,13.72243,-86.50720),(535,5,'Macuelizo','macuelizo',0.00,13.65239,-86.61380),(540,5,'Santa Marí­a','santamaria',0.00,13.74753,-86.71077),(545,5,'Ocotal','ocotal',0.00,13.63432,-86.47745),(550,5,'Ciudad Antigua','Ciudad-antigua',0.00,13.64217,-86.30893),(555,5,'Quilalí','quilali',0.00,13.56675,-86.02952),(560,5,'Wiwili de Nueva Segovia','Wiwili-nuevasegovia',0.00,13.62667,-85.82369),(1005,10,'Wiwilí','Wiwili',0.00,13.62130,-85.81864),(1010,10,'El Cúa','El-cua',0.00,13.36764,-85.67330),(1012,10,'San José Bocay','San-jose-bocay',0.00,13.61976,-85.50080),(1015,10,'Sta. María de Pantasma','Santa-maria-pantasma',0.00,13.36667,-85.95000),(1020,10,'San Rafael del Norte','San-rafael-del-norte',0.00,13.21391,-86.11043),(1025,10,'San Sebastian de Yalí','yali',0.00,13.30500,-86.18636),(1030,10,'La Concordia','La-concordia',0.00,13.19535,-86.16693),(1035,10,'Jinotega','jinotega',0.00,13.09165,-86.00121),(1040,10,'Altowangky','altowanky',0.00,NULL,NULL),(2005,20,'Somoto','somoto',0.00,13.48129,-86.58337),(2010,20,'Totogalpa','totogalpa',0.00,13.56336,-86.49281),(2015,20,'Telpaneca','telpaneca',0.00,13.53131,-86.28693),(2020,20,'San Juan de Río Coco','San-juan-rio-coco',0.00,13.54458,-86.16537),(2025,20,'Palacaguina','palacaguina',0.00,13.45597,-86.40710),(2030,20,'Yalaguina','yalaguina',0.00,13.48351,-86.49344),(2035,20,'San Lucas','San-lucas',0.00,13.41358,-86.61176),(2040,20,'Las Sabanas','Las-sabanas',0.00,13.34324,-86.62194),(2045,20,'San José de Cusmapa','San-jose-cusmapa',0.00,13.28847,-86.65489),(2505,25,'Pueblo Nuevo','Pueblo-nuevo',0.00,13.37937,-86.48077),(2510,25,'Condega','condega',0.00,13.36213,-86.39789),(2515,25,'Estelí','esteli',0.00,13.08948,-86.35551),(2520,25,'San Juan de Limay','Sanjuan-limay',0.00,13.17489,-86.61234),(2525,25,'La Trinidad','trinidad',0.00,12.96823,-86.23604),(2530,25,'San Nicolás','San-nicolas',0.00,12.93312,-86.34700),(3005,30,'San Pedro del Norte','San-pedro-del-norte',0.00,13.27596,-86.87777),(3010,30,'San Francisco del Norte','San-francisco-del-norte',0.00,13.20016,-86.77192),(3015,30,'Cinco Pinos','Cinco-pinos',0.00,13.23036,-86.86719),(3020,30,'Santo Tomás del Norte','Santo-tomas-del-norte',0.00,13.18701,-86.92352),(3025,30,'El Viejo','El-viejo',0.00,12.66228,-87.16541),(3030,30,'Pto. Morazán','Puerto-morazan',0.00,12.76721,-87.13388),(3035,30,'Somotillo','somotillo',0.00,13.04495,-86.90499),(3040,30,'Villanueva','villanueva',0.00,12.96391,-86.81468),(3045,30,'Chinandega','chinandega',0.00,12.62872,-87.13149),(3050,30,'El Realejo','El-realejo',0.00,12.54551,-87.16736),(3055,30,'Corinto','corinto',0.00,12.48461,-87.17122),(3060,30,'Chichigalpa','chichigalpa',0.00,12.57224,-87.02849),(3065,30,'Posoltega','posotelga',0.00,12.54410,-86.98010),(3505,35,'Achuapa','achuapa',0.00,13.05433,-86.59070),(3510,35,'El Sauce','El-sauce',0.00,12.88694,-86.53952),(3515,35,'Santa Rosa del Peñon','Santa-rosa-del-penon',0.00,12.80142,-86.37144),(3520,35,'El Jicaral','El-jicaral',0.00,12.72672,-86.38134),(3525,35,'Larreynaga','larreynaga',0.00,12.59311,-86.68015),(3530,35,'Telica','telica',0.00,12.52152,-86.86030),(3535,35,'Quezalguaque','quezalguaque',0.00,12.50614,-86.90366),(3540,35,'León','leon',0.00,12.43481,-86.88174),(3545,35,'La Paz Centro','La-paz-centro',0.00,12.34011,-86.67625),(3550,35,'Nagarote','nagarote',0.00,12.26531,-86.56812),(4005,40,'Rancho Grande','Rancho-grande',0.00,13.25352,-85.55268),(4010,40,'Rí­o Blanco','Rio-blanco',0.00,12.93044,-85.22610),(4015,40,'El Tuma - La Dalia','El-tuma',0.00,13.13735,-85.73788),(4020,40,'San Isidro','San-isidro',0.00,12.92937,-86.19550),(4025,40,'Sébaco','sebaco',0.00,12.85190,-86.09696),(4030,40,'Matagalpa','matagalpa',0.00,12.92709,-85.91747),(4035,40,'San Ramón','San-ramon',0.00,12.92254,-85.83968),(4040,40,'Matiguás','matiguas',0.00,12.83710,-85.46079),(4045,40,'Muy Muy','muymuy',0.00,12.76125,-85.63123),(4050,40,'Esquipulas','esquipulas',0.00,12.66446,-85.78909),(4055,40,'San Dionisio','San-dionisio',0.00,12.76190,-85.85091),(4060,40,'Terrabona','terrabona',0.00,12.73009,-85.96487),(4065,40,'Ciudad Darí­o','Ciudad-dario',0.00,12.73000,-86.12457),(5005,50,'San José de los Remates','San-jose-de-los-remates',0.00,12.59748,-85.76253),(5010,50,'Boaco','boaco',0.00,12.47160,-85.65952),(5015,50,'Camoapa','camoapa',0.00,12.38377,-85.51465),(5020,50,'Santa Lucía','Santa-lucia',0.00,12.53226,-85.71156),(5025,50,'Teustepe','teustepe',0.00,12.41979,-85.79922),(5030,50,'San  Lorenzo','San-lorenzo',0.00,12.37789,-85.66718),(5505,55,'San Francisco Libre','San-francisco-libre',0.00,12.50458,-86.30105),(5510,55,'Tipitapa','tipitapa',0.00,12.19662,-86.09682),(5515,55,'Mateare','mateare',0.00,12.23536,-86.43013),(5520,55,'Villa Carlos Fonseca','Villa-carlos-fonseca',0.00,11.97924,-86.50809),(5522,55,'Ciudad Sandino','Ciudad-sandino',0.00,12.16082,-86.35004),(5525,55,'Managua','managua',0.00,12.14746,-86.27339),(5530,55,'Ticuantepe','ticuantepe',0.00,12.02125,-86.20288),(5532,55,'El Crucero','El-crucero',0.00,11.97865,-86.31076),(5535,55,'San Rafael del Sur','San-rafael-del-sur',0.00,11.84681,-86.43977),(6005,60,'Nindirí','nindiri',0.00,12.00243,-86.12067),(6010,60,'Masaya','masaya',0.00,11.97735,-86.09606),(6015,60,'Tisma','tisma',0.00,12.08133,-86.01921),(6020,60,'La Concepción','La-concepcion',0.00,11.93615,-86.19220),(6025,60,'Masatepe','masatepe',0.00,11.91344,-86.14475),(6030,60,'Nandasmo','nandasmo',0.00,11.90933,-86.13055),(6035,60,'Catarina','catarina',0.00,11.91078,-86.07407),(6040,60,'San Juan de Oriente','San-juan-de-oriente',0.00,11.90479,-86.07311),(6045,60,'Niquinohomo','niquinomo',0.00,11.90408,-86.09472),(6505,65,'Comalapa','comalapa',0.00,12.28340,-85.51142),(6507,65,'San Francisco Cuapa','San-francisco-cuapa',0.00,12.26671,-85.38308),(6510,65,'Juigalpa','juigalpa',0.00,12.10580,-85.36842),(6515,65,'La Libertad','La-libertad',0.00,12.21539,-85.16549),(6520,65,'Santo Domingo','Santo-domingo',0.00,12.26301,-85.08232),(6525,65,'Santo Tomás','Santo-tomas',0.00,12.06902,-85.09340),(6530,65,'San Pedro de Lóvago','San-pedro-de-lovago',0.00,12.12852,-85.11572),(6535,65,'Acoyapa','acoyapa',0.00,11.96764,-85.17044),(6540,65,'Villa Sandino','Villa-sandino',0.00,12.04779,-84.99334),(6545,65,'El Coral','El-coral',0.00,11.91576,-84.65041),(7005,70,'Diriá','diria',0.00,11.88416,-86.05565),(7010,70,'Diriomo','diriomo',0.00,11.87494,-86.05110),(7015,70,'Granada','granada',0.00,11.93095,-85.95696),(7020,70,'Nandaime','nandaime',0.00,11.75630,-86.05345),(7505,75,'San Marcos','San-marcos',0.00,11.90651,-86.20314),(7510,75,'Jinotepe','jinotepe',0.00,11.84831,-86.19846),(7515,75,'Dolores','dolores',0.00,11.85565,-86.21535),(7520,75,'Diriamba','diriamba',0.00,11.85572,-86.24074),(7525,75,'El Rosario','El-rosario',0.00,11.83224,-86.16484),(7530,75,'La Paz de Carazo','La-paz-de-carazo',0.00,11.82206,-86.12750),(7535,75,'Santa Teresa','Santa-tereza',0.00,11.80272,-86.16281),(7540,75,'La Conquista','La-conquista',0.00,11.73336,-86.19297),(8005,80,'Tola','tola',0.00,11.43868,-85.93907),(8010,80,'Belén','belen',0.00,11.50081,-85.89014),(8015,80,'Potosí','potosi',0.00,11.49320,-85.85709),(8020,80,'Buenos Aires','Buenos-aires',0.00,11.46923,-85.81701),(8025,80,'Moyogalpa','moyogalpa',0.00,11.53947,-85.69746),(8030,80,'Altagracia','altagracia',0.00,11.56547,-85.57793),(8035,80,'San Jorge','San-jorge',0.00,11.45532,-85.80074),(8040,80,'Rivas','rivas',0.00,11.43975,-85.82880),(8045,80,'San Juan del Sur','San-juan-del-sur',0.00,11.25384,-85.87177),(8050,80,'Cárdenas','cardenas',0.00,11.19521,-85.50886),(8505,85,'Morrito','morrito',0.00,11.62130,-85.08169),(8510,85,'El Almendro','El-almendro',0.00,11.67684,-84.70362),(8515,85,'San Miguelito','San-miguelito',0.00,11.40156,-84.90005),(8520,85,'San Carlos','San-carlos',0.00,11.12088,-84.77837),(8525,85,'El Castillo','El-castillo',0.00,11.03969,-84.47295),(8530,85,'San Juan del Norte','San-juan-del-norte',0.00,10.94671,-83.73479),(9105,91,'Waspán','waspan',0.00,14.74386,-83.96885),(9110,91,'Puerto Cabezas','Puerto-cabezas',0.00,14.03313,-83.38223),(9115,91,'Rosita','rosita',0.00,13.91060,-84.39153),(9120,91,'Bonanza','bonanza',0.00,14.02584,-84.62088),(9125,91,'Waslala','waslala',0.00,13.33465,-85.37099),(9127,91,'Mulukuku','mulukuku',0.00,13.15000,-84.96667),(9130,91,'Siuna','siuna',0.00,13.73857,-84.78491),(9135,91,'Prinzapolka','prinzapolka',0.00,13.40611,-83.56229),(9305,93,'Paiwas','paiwas',0.00,12.78548,-85.12402),(9310,93,'La Cruz de Río Grande','La-cruz-rio-grande',0.00,13.11145,-84.18835),(9312,93,'Desembocadura de Río Grande','Desembocadura-rio-grande',0.00,12.93208,-83.57697),(9315,93,'Laguna de Perlas','Laguna-de-perlas',0.00,12.34096,-83.67052),(9316,93,'El Tortuguero','El-tortuguero',0.00,12.82085,-84.19906),(9320,93,'Rama','rama',0.00,12.16004,-84.21913),(9323,93,'El Ayote','El-ayote',0.00,12.49486,-84.81943),(9325,93,'Muelle de los Bueyes','Muelle-de-los-bueyes',0.00,12.06764,-84.53749),(9330,93,'Kukra - Hill','Kukra-hill',0.00,12.24163,-83.74532),(9335,93,'Corn Island','Corn-island',0.00,12.18017,-83.05975),(9340,93,'Bluefields','bluefields',0.00,12.01144,-83.76388),(9345,93,'Nueva Guinea','Nueva-guinea',0.00,11.68827,-84.45794);
/*!40000 ALTER TABLE `lugar_municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prevencion_eventoexterno`
--

DROP TABLE IF EXISTS `prevencion_eventoexterno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prevencion_eventoexterno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `lugar` varchar(200) NOT NULL,
  `actividad` int(11) NOT NULL,
  `facilitadores` int(11) NOT NULL DEFAULT '0',
  `ninos` int(11) NOT NULL DEFAULT '0',
  `ninas` int(11) NOT NULL DEFAULT '0',
  `jovenes_hombres` int(11) NOT NULL DEFAULT '0',
  `jovenes_mujeres` int(11) NOT NULL DEFAULT '0',
  `adultos_hombres` int(11) NOT NULL DEFAULT '0',
  `adultos_mujeres` int(11) NOT NULL DEFAULT '0',
  `tematica` int(11) NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `comentarios` longtext NOT NULL,
  `acuerdos` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prevencion_eventoexterno`
--

LOCK TABLES `prevencion_eventoexterno` WRITE;
/*!40000 ALTER TABLE `prevencion_eventoexterno` DISABLE KEYS */;
/*!40000 ALTER TABLE `prevencion_eventoexterno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prevencion_eventointerno`
--

DROP TABLE IF EXISTS `prevencion_eventointerno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prevencion_eventointerno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `lugar` varchar(200) NOT NULL,
  `actividad` int(11) NOT NULL,
  `participantes` int(11) NOT NULL DEFAULT '0',
  `tematica` int(11) NOT NULL,
  `metodologia` int(11) NOT NULL,
  `apropiacion` int(11) NOT NULL,
  `aprendizaje` int(11) NOT NULL,
  `participacion` int(11) NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `comentarios` longtext NOT NULL,
  `acuerdos` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prevencion_eventointerno`
--

LOCK TABLES `prevencion_eventointerno` WRITE;
/*!40000 ALTER TABLE `prevencion_eventointerno` DISABLE KEYS */;
/*!40000 ALTER TABLE `prevencion_eventointerno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_coro`
--

DROP TABLE IF EXISTS `promocion_coro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_coro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `semestre` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_coro`
--

LOCK TABLES `promocion_coro` WRITE;
/*!40000 ALTER TABLE `promocion_coro` DISABLE KEYS */;
/*!40000 ALTER TABLE `promocion_coro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_danza`
--

DROP TABLE IF EXISTS `promocion_danza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_danza` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `semestre` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_danza`
--

LOCK TABLES `promocion_danza` WRITE;
/*!40000 ALTER TABLE `promocion_danza` DISABLE KEYS */;
/*!40000 ALTER TABLE `promocion_danza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_eventocolectivo`
--

DROP TABLE IF EXISTS `promocion_eventocolectivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_eventocolectivo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `lugar` varchar(200) NOT NULL,
  `actividad` int(11) NOT NULL,
  `participantes` int(11) NOT NULL DEFAULT '0',
  `ninos` int(11) NOT NULL DEFAULT '0',
  `ninas` int(11) NOT NULL DEFAULT '0',
  `jovenes_hombres` int(11) NOT NULL DEFAULT '0',
  `jovenes_mujeres` int(11) NOT NULL DEFAULT '0',
  `adultos_hombres` int(11) NOT NULL DEFAULT '0',
  `adultos_mujeres` int(11) NOT NULL DEFAULT '0',
  `sensibilizacion` int(11) NOT NULL,
  `apropiacion` int(11) NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `comentarios` longtext NOT NULL,
  `acuerdos` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_eventocolectivo`
--

LOCK TABLES `promocion_eventocolectivo` WRITE;
/*!40000 ALTER TABLE `promocion_eventocolectivo` DISABLE KEYS */;
/*!40000 ALTER TABLE `promocion_eventocolectivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_musica`
--

DROP TABLE IF EXISTS `promocion_musica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_musica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `semestre` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_musica`
--

LOCK TABLES `promocion_musica` WRITE;
/*!40000 ALTER TABLE `promocion_musica` DISABLE KEYS */;
INSERT INTO `promocion_musica` VALUES (2,'Musica',1,2012),(3,'Musica',2,2012);
/*!40000 ALTER TABLE `promocion_musica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_pintura`
--

DROP TABLE IF EXISTS `promocion_pintura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_pintura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `semestre` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_pintura`
--

LOCK TABLES `promocion_pintura` WRITE;
/*!40000 ALTER TABLE `promocion_pintura` DISABLE KEYS */;
/*!40000 ALTER TABLE `promocion_pintura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_teatro`
--

DROP TABLE IF EXISTS `promocion_teatro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_teatro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `semestre` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_teatro`
--

LOCK TABLES `promocion_teatro` WRITE;
/*!40000 ALTER TABLE `promocion_teatro` DISABLE KEYS */;
/*!40000 ALTER TABLE `promocion_teatro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_autor`
--

DROP TABLE IF EXISTS `registro_autor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_autor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_autor`
--

LOCK TABLES `registro_autor` WRITE;
/*!40000 ALTER TABLE `registro_autor` DISABLE KEYS */;
INSERT INTO `registro_autor` VALUES (1,'Helmy'),(2,'Carlos');
/*!40000 ALTER TABLE `registro_autor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_colegio`
--

DROP TABLE IF EXISTS `registro_colegio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_colegio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_colegio`
--

LOCK TABLES `registro_colegio` WRITE;
/*!40000 ALTER TABLE `registro_colegio` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_colegio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_inscripcioncurso`
--

DROP TABLE IF EXISTS `registro_inscripcioncurso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_inscripcioncurso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `persona_id` int(11) NOT NULL,
  `curso_id` int(11) NOT NULL,
  `becado` int(11) NOT NULL,
  `estado` int(11),
  `xq_no_termino` int(11) DEFAULT NULL,
  `calificacion` int(11) DEFAULT NULL,
  `mejora_autoestima` int(11) DEFAULT NULL,
  `mejora_vida` int(11) DEFAULT NULL,
  `calidad_contenido` int(11) DEFAULT NULL,
  `metodologia` int(11) DEFAULT NULL,
  `fecha` date NOT NULL,
  `date_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `registro_inscripcioncurso_e27cbd6d` (`persona_id`),
  KEY `registro_inscripcioncurso_17e2b2af` (`curso_id`),
  CONSTRAINT `curso_id_refs_id_1e5746de0bc0ce51` FOREIGN KEY (`curso_id`) REFERENCES `formacion_curso` (`id`),
  CONSTRAINT `persona_id_refs_id_11bcbf5fcd560b59` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_inscripcioncurso`
--

LOCK TABLES `registro_inscripcioncurso` WRITE;
/*!40000 ALTER TABLE `registro_inscripcioncurso` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_inscripcioncurso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_libro`
--

DROP TABLE IF EXISTS `registro_libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_libro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `registro_libro_e4470c6e` (`content_type_id`),
  KEY `registro_libro_829e37fd` (`object_id`),
  CONSTRAINT `content_type_id_refs_id_3a7e8067e82d9a3c` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_libro`
--

LOCK TABLES `registro_libro` WRITE;
/*!40000 ALTER TABLE `registro_libro` DISABLE KEYS */;
INSERT INTO `registro_libro` VALUES (1,19,1,'Libro1'),(8,19,2,'Libro del negro');
/*!40000 ALTER TABLE `registro_libro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_modulopersona`
--

DROP TABLE IF EXISTS `registro_modulopersona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_modulopersona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `persona_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `persona_id` (`persona_id`),
  CONSTRAINT `persona_id_refs_id_4a585a0dc005332b` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_modulopersona`
--

LOCK TABLES `registro_modulopersona` WRITE;
/*!40000 ALTER TABLE `registro_modulopersona` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_modulopersona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_modulopersona_atencion_integral`
--

DROP TABLE IF EXISTS `registro_modulopersona_atencion_integral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_modulopersona_atencion_integral` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modulopersona_id` int(11) NOT NULL,
  `submodulo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `registro_modulopersona_a_modulopersona_id_1c2d4ae80f363fb5_uniq` (`modulopersona_id`,`submodulo_id`),
  KEY `registro_modulopersona_atencion_integral_2ec110b1` (`modulopersona_id`),
  KEY `registro_modulopersona_atencion_integral_d8372a81` (`submodulo_id`),
  CONSTRAINT `modulopersona_id_refs_id_77a479d5e43678c8` FOREIGN KEY (`modulopersona_id`) REFERENCES `registro_modulopersona` (`id`),
  CONSTRAINT `submodulo_id_refs_id_ecf239158aa81de` FOREIGN KEY (`submodulo_id`) REFERENCES `sistema_submodulo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_modulopersona_atencion_integral`
--

LOCK TABLES `registro_modulopersona_atencion_integral` WRITE;
/*!40000 ALTER TABLE `registro_modulopersona_atencion_integral` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_modulopersona_atencion_integral` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_modulopersona_biblioteca`
--

DROP TABLE IF EXISTS `registro_modulopersona_biblioteca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_modulopersona_biblioteca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modulopersona_id` int(11) NOT NULL,
  `submodulo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `registro_modulopersona_b_modulopersona_id_3d46463e30ad03a8_uniq` (`modulopersona_id`,`submodulo_id`),
  KEY `registro_modulopersona_biblioteca_2ec110b1` (`modulopersona_id`),
  KEY `registro_modulopersona_biblioteca_d8372a81` (`submodulo_id`),
  CONSTRAINT `modulopersona_id_refs_id_15911219dbb42ee5` FOREIGN KEY (`modulopersona_id`) REFERENCES `registro_modulopersona` (`id`),
  CONSTRAINT `submodulo_id_refs_id_7d3a355a24f0f5` FOREIGN KEY (`submodulo_id`) REFERENCES `sistema_submodulo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_modulopersona_biblioteca`
--

LOCK TABLES `registro_modulopersona_biblioteca` WRITE;
/*!40000 ALTER TABLE `registro_modulopersona_biblioteca` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_modulopersona_biblioteca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_modulopersona_formacion`
--

DROP TABLE IF EXISTS `registro_modulopersona_formacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_modulopersona_formacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modulopersona_id` int(11) NOT NULL,
  `submodulo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `registro_modulopersona_f_modulopersona_id_6b70f49b4eb90975_uniq` (`modulopersona_id`,`submodulo_id`),
  KEY `registro_modulopersona_formacion_2ec110b1` (`modulopersona_id`),
  KEY `registro_modulopersona_formacion_d8372a81` (`submodulo_id`),
  CONSTRAINT `modulopersona_id_refs_id_6df6cda8737a9a88` FOREIGN KEY (`modulopersona_id`) REFERENCES `registro_modulopersona` (`id`),
  CONSTRAINT `submodulo_id_refs_id_46d48cea9bee0b9e` FOREIGN KEY (`submodulo_id`) REFERENCES `sistema_submodulo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_modulopersona_formacion`
--

LOCK TABLES `registro_modulopersona_formacion` WRITE;
/*!40000 ALTER TABLE `registro_modulopersona_formacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_modulopersona_formacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_modulopersona_promocion_artistica`
--

DROP TABLE IF EXISTS `registro_modulopersona_promocion_artistica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_modulopersona_promocion_artistica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modulopersona_id` int(11) NOT NULL,
  `submodulo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `registro_modulopersona_p_modulopersona_id_39d892ef8ff32724_uniq` (`modulopersona_id`,`submodulo_id`),
  KEY `registro_modulopersona_promocion_artistica_2ec110b1` (`modulopersona_id`),
  KEY `registro_modulopersona_promocion_artistica_d8372a81` (`submodulo_id`),
  CONSTRAINT `modulopersona_id_refs_id_67ba86dfb1f83f59` FOREIGN KEY (`modulopersona_id`) REFERENCES `registro_modulopersona` (`id`),
  CONSTRAINT `submodulo_id_refs_id_5d88d596b4c17bc1` FOREIGN KEY (`submodulo_id`) REFERENCES `sistema_submodulo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_modulopersona_promocion_artistica`
--

LOCK TABLES `registro_modulopersona_promocion_artistica` WRITE;
/*!40000 ALTER TABLE `registro_modulopersona_promocion_artistica` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_modulopersona_promocion_artistica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_modulopersona_pv_externa`
--

DROP TABLE IF EXISTS `registro_modulopersona_pv_externa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_modulopersona_pv_externa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modulopersona_id` int(11) NOT NULL,
  `submodulo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `registro_modulopersona_p_modulopersona_id_3e15ada3da91a57c_uniq` (`modulopersona_id`,`submodulo_id`),
  KEY `registro_modulopersona_pv_externa_2ec110b1` (`modulopersona_id`),
  KEY `registro_modulopersona_pv_externa_d8372a81` (`submodulo_id`),
  CONSTRAINT `modulopersona_id_refs_id_1d6b3a5ae4a3f547` FOREIGN KEY (`modulopersona_id`) REFERENCES `registro_modulopersona` (`id`),
  CONSTRAINT `submodulo_id_refs_id_36bbbd99dfb84f21` FOREIGN KEY (`submodulo_id`) REFERENCES `sistema_submodulo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_modulopersona_pv_externa`
--

LOCK TABLES `registro_modulopersona_pv_externa` WRITE;
/*!40000 ALTER TABLE `registro_modulopersona_pv_externa` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_modulopersona_pv_externa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_modulopersona_pv_interna`
--

DROP TABLE IF EXISTS `registro_modulopersona_pv_interna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_modulopersona_pv_interna` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modulopersona_id` int(11) NOT NULL,
  `submodulo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `registro_modulopersona_p_modulopersona_id_7da42bc9a271898a_uniq` (`modulopersona_id`,`submodulo_id`),
  KEY `registro_modulopersona_pv_interna_2ec110b1` (`modulopersona_id`),
  KEY `registro_modulopersona_pv_interna_d8372a81` (`submodulo_id`),
  CONSTRAINT `modulopersona_id_refs_id_362216b78d8f49f9` FOREIGN KEY (`modulopersona_id`) REFERENCES `registro_modulopersona` (`id`),
  CONSTRAINT `submodulo_id_refs_id_775d48d172848761` FOREIGN KEY (`submodulo_id`) REFERENCES `sistema_submodulo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_modulopersona_pv_interna`
--

LOCK TABLES `registro_modulopersona_pv_interna` WRITE;
/*!40000 ALTER TABLE `registro_modulopersona_pv_interna` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_modulopersona_pv_interna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_oficio`
--

DROP TABLE IF EXISTS `registro_oficio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_oficio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_oficio`
--

LOCK TABLES `registro_oficio` WRITE;
/*!40000 ALTER TABLE `registro_oficio` DISABLE KEYS */;
INSERT INTO `registro_oficio` VALUES (2,'Asalriado ONG'),(1,'Carpintero');
/*!40000 ALTER TABLE `registro_oficio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_pariente`
--

DROP TABLE IF EXISTS `registro_pariente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_pariente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_pariente`
--

LOCK TABLES `registro_pariente` WRITE;
/*!40000 ALTER TABLE `registro_pariente` DISABLE KEYS */;
INSERT INTO `registro_pariente` VALUES (4,'Abuela'),(3,'Abuelo'),(6,'Esposo/a'),(5,'Hijos'),(2,'Mama'),(1,'Papa');
/*!40000 ALTER TABLE `registro_pariente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_persona`
--

DROP TABLE IF EXISTS `registro_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_persona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `primer_nombre` varchar(50) NOT NULL,
  `segundo_nombre` varchar(50) NOT NULL,
  `primer_apellido` varchar(50) NOT NULL,
  `segundo_apellido` varchar(50) NOT NULL,
  `codigo` int(11) NOT NULL,
  `sexo` int(11) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `cedula` varchar(20) NOT NULL,
  `personal_ccbn` int(11) NOT NULL,
  `docente_ccbn` int(11) NOT NULL,
  `municipio_id` int(11) NOT NULL,
  `ciudad_id` int(11) NOT NULL,
  `barrio_id` int(11) NOT NULL,
  `distrito` int(11) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `celular` varchar(12) NOT NULL,
  `nivel_academico` int(11) NOT NULL,
  `nivel_estudio` int(11) NOT NULL,
  `centro_actual_id` int(11) DEFAULT NULL,
  `oficio_id` int(11) DEFAULT NULL,
  `tipo_familia` int(11) NOT NULL,
  `jefe_familia` int(11) NOT NULL,
  `j_primer_nombre` varchar(50) NOT NULL,
  `j_segundo_nombre` varchar(50) NOT NULL,
  `j_primer_apellido` varchar(50) NOT NULL,
  `j_segundo_apellido` varchar(50) NOT NULL,
  `j_oficio_id` int(11),
  PRIMARY KEY (`id`),
  KEY `registro_persona_f3143aaa` (`municipio_id`),
  KEY `registro_persona_4e8eecfa` (`ciudad_id`),
  KEY `registro_persona_2239bf4f` (`barrio_id`),
  KEY `registro_persona_65e316cf` (`centro_actual_id`),
  KEY `registro_persona_a64becb5` (`oficio_id`),
  KEY `registro_persona_90fa4532` (`j_oficio_id`),
  CONSTRAINT `centro_actual_id_refs_id_835efa97` FOREIGN KEY (`centro_actual_id`) REFERENCES `registro_colegio` (`id`),
  CONSTRAINT `j_oficio_id_refs_id_59a72bc0cbb8f02d` FOREIGN KEY (`j_oficio_id`) REFERENCES `registro_oficio` (`id`),
  CONSTRAINT `j_oficio_id_refs_id_cbb8f02d` FOREIGN KEY (`j_oficio_id`) REFERENCES `registro_oficio` (`id`),
  CONSTRAINT `oficio_id_refs_id_cbb8f02d` FOREIGN KEY (`oficio_id`) REFERENCES `registro_oficio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_persona`
--

LOCK TABLES `registro_persona` WRITE;
/*!40000 ALTER TABLE `registro_persona` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_persona_con_quien_vive`
--

DROP TABLE IF EXISTS `registro_persona_con_quien_vive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_persona_con_quien_vive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `persona_id` int(11) NOT NULL,
  `pariente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `persona_id` (`persona_id`,`pariente_id`),
  KEY `registro_persona_con_quien_vive_e27cbd6d` (`persona_id`),
  KEY `registro_persona_con_quien_vive_d3b4056a` (`pariente_id`),
  CONSTRAINT `pariente_id_refs_id_3f799100` FOREIGN KEY (`pariente_id`) REFERENCES `registro_pariente` (`id`),
  CONSTRAINT `persona_id_refs_id_60a60efd` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=293 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_persona_con_quien_vive`
--

LOCK TABLES `registro_persona_con_quien_vive` WRITE;
/*!40000 ALTER TABLE `registro_persona_con_quien_vive` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_persona_con_quien_vive` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_registrobecaprimaria`
--

DROP TABLE IF EXISTS `registro_registrobecaprimaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_registrobecaprimaria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT '2012-04-26',
  `persona_id` int(11) NOT NULL,
  `beca_id` int(11) NOT NULL,
  `tutoria` int(11),
  `rendimiento_academico` int(11),
  `recibio_suplemento` int(11),
  `recibio_atencion_psicologica` int(11),
  `mejoro_habilidades` int(11),
  `reconoce_capacidad` int(11),
  `perc_derecho` int(11),
  PRIMARY KEY (`id`),
  KEY `persona_id_refs_id_335d610adc887d47` (`persona_id`),
  KEY `registro_registrobecaprimaria_79ed2dc3` (`beca_id`),
  CONSTRAINT `beca_id_refs_id_44483d34c8c311b8` FOREIGN KEY (`beca_id`) REFERENCES `atencionintegral_becaprimaria` (`id`),
  CONSTRAINT `persona_id_refs_id_335d610adc887d47` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_registrobecaprimaria`
--

LOCK TABLES `registro_registrobecaprimaria` WRITE;
/*!40000 ALTER TABLE `registro_registrobecaprimaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_registrobecaprimaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_registrobecasecundaria`
--

DROP TABLE IF EXISTS `registro_registrobecasecundaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_registrobecasecundaria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT '2012-04-26',
  `persona_id` int(11) NOT NULL,
  `beca_id` int(11) NOT NULL,
  `servicio_social` int(11),
  `esp_propos` int(11),
  `promotor` int(11),
  `solidario_famila` int(11),
  `solidario_centro` int(11),
  `solidario_comunidad` int(11),
  `solidario_sociedad` int(11),
  PRIMARY KEY (`id`),
  KEY `persona_id_refs_id_6670b5a614df4d81` (`persona_id`),
  KEY `registro_registrobecasecundaria_79ed2dc3` (`beca_id`),
  CONSTRAINT `beca_id_refs_id_799ac979129f0c50` FOREIGN KEY (`beca_id`) REFERENCES `atencionintegral_becasecundaria` (`id`),
  CONSTRAINT `persona_id_refs_id_6670b5a614df4d81` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_registrobecasecundaria`
--

LOCK TABLES `registro_registrobecasecundaria` WRITE;
/*!40000 ALTER TABLE `registro_registrobecasecundaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_registrobecasecundaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_registrobecauniversitaria`
--

DROP TABLE IF EXISTS `registro_registrobecauniversitaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_registrobecauniversitaria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT '2012-04-26',
  `persona_id` int(11) NOT NULL,
  `beca_id` int(11) NOT NULL,
  `servicio_social` int(11),
  `esp_propos` int(11),
  `promotor` int(11),
  `solidario_famila` int(11),
  `solidario_centro` int(11),
  `solidario_comunidad` int(11),
  `solidario_sociedad` int(11),
  PRIMARY KEY (`id`),
  KEY `persona_id_refs_id_715b703a3c8203d9` (`persona_id`),
  KEY `registro_registrobecauniversitaria_79ed2dc3` (`beca_id`),
  CONSTRAINT `beca_id_refs_id_637ae20c1f0abc6e` FOREIGN KEY (`beca_id`) REFERENCES `atencionintegral_becauniversitaria` (`id`),
  CONSTRAINT `persona_id_refs_id_715b703a3c8203d9` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_registrobecauniversitaria`
--

LOCK TABLES `registro_registrobecauniversitaria` WRITE;
/*!40000 ALTER TABLE `registro_registrobecauniversitaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_registrobecauniversitaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_registrobiblioteca`
--

DROP TABLE IF EXISTS `registro_registrobiblioteca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_registrobiblioteca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT '2012-04-26',
  `persona_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `persona_id` (`persona_id`),
  CONSTRAINT `persona_id_refs_id_75ab11dd3a6afa8b` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_registrobiblioteca`
--

LOCK TABLES `registro_registrobiblioteca` WRITE;
/*!40000 ALTER TABLE `registro_registrobiblioteca` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_registrobiblioteca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_registrocoro`
--

DROP TABLE IF EXISTS `registro_registrocoro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_registrocoro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT '2012-04-26',
  `persona_id` int(11) NOT NULL,
  `asistencia` int(11),
  `calificacion` int(11),
  `valores_ccbn` int(11),
  `genero` int(11),
  `mejora_capacidad` int(11),
  `utilidad_para_vida` int(11),
  `calidad_creativa` int(11),
  `metodologia` int(11),
  `perspectiva` int(11),
  `grupo_id` int(11) NOT NULL,
  `razon_no_continuar` int(11),
  PRIMARY KEY (`id`),
  KEY `persona_id_refs_id_4e2093463d59762` (`persona_id`),
  KEY `registro_registrocoro_15fb1ffa` (`grupo_id`),
  CONSTRAINT `grupo_id_refs_id_4a5e1107f1ab2b78` FOREIGN KEY (`grupo_id`) REFERENCES `promocion_coro` (`id`),
  CONSTRAINT `persona_id_refs_id_4e2093463d59762` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_registrocoro`
--

LOCK TABLES `registro_registrocoro` WRITE;
/*!40000 ALTER TABLE `registro_registrocoro` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_registrocoro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_registrodanza`
--

DROP TABLE IF EXISTS `registro_registrodanza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_registrodanza` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT '2012-04-26',
  `persona_id` int(11) NOT NULL,
  `asistencia` int(11),
  `calificacion` int(11),
  `valores_ccbn` int(11),
  `genero` int(11),
  `mejora_capacidad` int(11),
  `utilidad_para_vida` int(11),
  `calidad_creativa` int(11),
  `metodologia` int(11),
  `perspectiva` int(11),
  `grupo_id` int(11) NOT NULL,
  `razon_no_continuar` int(11),
  PRIMARY KEY (`id`),
  KEY `persona_id_refs_id_1459eed527d92e2` (`persona_id`),
  KEY `registro_registrodanza_15fb1ffa` (`grupo_id`),
  CONSTRAINT `grupo_id_refs_id_20185353446ca46` FOREIGN KEY (`grupo_id`) REFERENCES `promocion_danza` (`id`),
  CONSTRAINT `persona_id_refs_id_1459eed527d92e2` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_registrodanza`
--

LOCK TABLES `registro_registrodanza` WRITE;
/*!40000 ALTER TABLE `registro_registrodanza` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_registrodanza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_registromusica`
--

DROP TABLE IF EXISTS `registro_registromusica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_registromusica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT '2012-04-26',
  `persona_id` int(11) NOT NULL,
  `asistencia` int(11),
  `calificacion` int(11),
  `valores_ccbn` int(11),
  `genero` int(11),
  `mejora_capacidad` int(11),
  `utilidad_para_vida` int(11),
  `calidad_creativa` int(11),
  `metodologia` int(11),
  `perspectiva` int(11),
  `grupo_id` int(11) NOT NULL,
  `razon_no_continuar` int(11),
  PRIMARY KEY (`id`),
  KEY `persona_id_refs_id_67a37d66aa331b13` (`persona_id`),
  KEY `registro_registromusica_15fb1ffa` (`grupo_id`),
  CONSTRAINT `grupo_id_refs_id_6fff521731bcff9e` FOREIGN KEY (`grupo_id`) REFERENCES `promocion_musica` (`id`),
  CONSTRAINT `persona_id_refs_id_67a37d66aa331b13` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_registromusica`
--

LOCK TABLES `registro_registromusica` WRITE;
/*!40000 ALTER TABLE `registro_registromusica` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_registromusica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_registropintura`
--

DROP TABLE IF EXISTS `registro_registropintura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_registropintura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT '2012-04-26',
  `persona_id` int(11) NOT NULL,
  `asistencia` int(11),
  `calificacion` int(11),
  `valores_ccbn` int(11),
  `genero` int(11),
  `mejora_capacidad` int(11),
  `utilidad_para_vida` int(11),
  `calidad_creativa` int(11),
  `metodologia` int(11),
  `perspectiva` int(11),
  `grupo_id` int(11) NOT NULL,
  `razon_no_continuar` int(11),
  PRIMARY KEY (`id`),
  KEY `persona_id_refs_id_79294d12884b4631` (`persona_id`),
  KEY `registro_registropintura_15fb1ffa` (`grupo_id`),
  CONSTRAINT `grupo_id_refs_id_72fb1ffdaf6d3f70` FOREIGN KEY (`grupo_id`) REFERENCES `promocion_pintura` (`id`),
  CONSTRAINT `persona_id_refs_id_79294d12884b4631` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_registropintura`
--

LOCK TABLES `registro_registropintura` WRITE;
/*!40000 ALTER TABLE `registro_registropintura` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_registropintura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_registroteatro`
--

DROP TABLE IF EXISTS `registro_registroteatro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_registroteatro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT '2012-04-26',
  `persona_id` int(11) NOT NULL,
  `asistencia` int(11),
  `calificacion` int(11),
  `valores_ccbn` int(11),
  `genero` int(11),
  `mejora_capacidad` int(11),
  `utilidad_para_vida` int(11),
  `calidad_creativa` int(11),
  `metodologia` int(11),
  `perspectiva` int(11),
  `grupo_id` int(11) NOT NULL,
  `razon_no_continuar` int(11),
  PRIMARY KEY (`id`),
  KEY `persona_id_refs_id_3c92d9f114da8454` (`persona_id`),
  KEY `registro_registroteatro_15fb1ffa` (`grupo_id`),
  CONSTRAINT `grupo_id_refs_id_475d98e1e555ca94` FOREIGN KEY (`grupo_id`) REFERENCES `promocion_teatro` (`id`),
  CONSTRAINT `persona_id_refs_id_3c92d9f114da8454` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_registroteatro`
--

LOCK TABLES `registro_registroteatro` WRITE;
/*!40000 ALTER TABLE `registro_registroteatro` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_registroteatro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_relacion`
--

DROP TABLE IF EXISTS `registro_relacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_relacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parentesco` varchar(50) NOT NULL,
  `persona_id` int(11) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `registro_relacion_e27cbd6d` (`persona_id`),
  KEY `registro_relacion_5d52dd10` (`owner_id`),
  CONSTRAINT `owner_id_refs_id_2d8c145d68b34bf3` FOREIGN KEY (`owner_id`) REFERENCES `registro_persona` (`id`),
  CONSTRAINT `persona_id_refs_id_2d8c145d68b34bf3` FOREIGN KEY (`persona_id`) REFERENCES `registro_persona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=837 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_relacion`
--

LOCK TABLES `registro_relacion` WRITE;
/*!40000 ALTER TABLE `registro_relacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_relacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_filter`
--

DROP TABLE IF EXISTS `sistema_filter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sistema_filter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `salida_id` int(11) NOT NULL,
  `field` varchar(50) NOT NULL DEFAULT '',
  `criteria` varchar(30) NOT NULL DEFAULT '',
  `value` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `sistema_filter_d89f2daa` (`salida_id`),
  CONSTRAINT `salida_id_refs_id_422e421c9e17cf17` FOREIGN KEY (`salida_id`) REFERENCES `sistema_salida` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_filter`
--

LOCK TABLES `sistema_filter` WRITE;
/*!40000 ALTER TABLE `sistema_filter` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_filter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_modulo`
--

DROP TABLE IF EXISTS `sistema_modulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sistema_modulo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `code` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_modulo`
--

LOCK TABLES `sistema_modulo` WRITE;
/*!40000 ALTER TABLE `sistema_modulo` DISABLE KEYS */;
INSERT INTO `sistema_modulo` VALUES (1,'Formación','module1'),(2,'Atención Integral','module2'),(3,'Biblioteca','module3'),(4,'Promoción Artística','module4'),(5,'Prevencion de Violencia Interna','module5'),(6,'Prevención de Violencia Externa','module6');
/*!40000 ALTER TABLE `sistema_modulo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_salida`
--

DROP TABLE IF EXISTS `sistema_salida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sistema_salida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `meta` int(11) DEFAULT NULL,
  `titulo` longtext NOT NULL,
  `tipo_meta` int(11) DEFAULT NULL,
  `model` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_salida`
--

LOCK TABLES `sistema_salida` WRITE;
/*!40000 ALTER TABLE `sistema_salida` DISABLE KEYS */;
INSERT INTO `sistema_salida` VALUES (1,2012,20,'',2,'formacion,Curso');
/*!40000 ALTER TABLE `sistema_salida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_submodulo`
--

DROP TABLE IF EXISTS `sistema_submodulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sistema_submodulo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `parent_module_id` int(11) NOT NULL,
  `code` varchar(20) NOT NULL,
  `inline` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `registro_submodulo_22b3d46a` (`parent_module_id`),
  CONSTRAINT `parent_module_id_refs_id_e68681d6` FOREIGN KEY (`parent_module_id`) REFERENCES `sistema_modulo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_submodulo`
--

LOCK TABLES `sistema_submodulo` WRITE;
/*!40000 ALTER TABLE `sistema_submodulo` DISABLE KEYS */;
INSERT INTO `sistema_submodulo` VALUES (1,'Educación Básica',1,'educacionbasica','FormacionBasicaInline'),(2,'Formación Técnica Vocacional',1,'formacionvocacional','FormacionVocacionalInline'),(3,'Formación Artística',1,'formacionartistica','FormacionArtisticaInline'),(4,'Beca Primaria',2,'becaprimaria','RegistroBecaPrimariaInline'),(5,'Beca Secundaria',2,'becasecundaria','RegistroBecaSecundariaInline'),(6,'Beca Universitaria',2,'becauniversitaria','RegistroBecaUniversitariaInline'),(7,'Familia',2,'',''),(8,'Biblioteca',3,'biblioteca','RegistroBibliotecaInline'),(9,'Música',4,'grupomusica','RegistroMusicaInline'),(10,'Teatro',4,'teatro','RegistroTeatroInline'),(11,'Danza',4,'danza','RegistroDanzaInline'),(12,'Coro',4,'coro','RegistroCoroInline'),(13,'Pintura',4,'pintura','RegistroPinturaInline'),(14,'Prevención de Violencia Interna',5,'previnterna','RegistroPinturaInline'),(15,'Prevención de Violencia Externa',6,'prevexterna','RegistroPinturaInline');
/*!40000 ALTER TABLE `sistema_submodulo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'lugar','0001_initial','2012-04-11 20:01:27'),(2,'registro','0001_initial','2012-04-11 20:01:46'),(3,'registro','0002_auto__add_relacion','2012-04-12 03:23:50'),(4,'registro','0003_auto__add_field_relacion_persona__add_field_relacion_owner','2012-04-12 03:32:44'),(5,'registro','0004_auto__chg_field_persona_j_oficio','2012-04-12 04:03:28'),(6,'registro','0005_auto__add_autor__add_libro','2012-04-13 01:01:08'),(7,'registro','0005_auto__add_modulopersona__add_submodulo__add_modulo','2012-04-14 03:16:15'),(8,'registro','0006_auto__del_submodulo__del_modulo','2012-04-14 03:24:58'),(9,'sistema','0001_initial','2012-04-14 03:28:08'),(10,'sistema','0002_auto__add_field_modulo_code','2012-04-14 03:53:52'),(11,'formacion','0001_initial','2012-04-17 04:07:33'),(12,'registro','0007_auto__add_inscripcioncurso','2012-04-17 20:48:52'),(13,'registro','0008_auto__chg_field_inscripcioncurso_estado','2012-04-17 21:48:09'),(14,'sistema','0003_auto__add_field_submodulo_code','2012-04-17 22:49:54'),(15,'registro','0009_auto__add_field_inscripcioncurso_fecha','2012-04-17 23:08:03'),(16,'sistema','0004_auto__add_field_submodulo_inline','2012-04-18 02:50:40'),(17,'registro','0010_auto__add_field_inscripcioncurso_date_time__chg_field_inscripcioncurso','2012-04-20 01:24:31'),(18,'registro','0011_auto__add_registrobiblioteca','2012-04-27 02:11:14'),(19,'registro','0012_auto__add_registromusica__add_registrobecauniversitaria__add_registrot','2012-04-27 02:41:09'),(20,'registro','0013_auto__chg_field_registromusica_persona__del_unique_registromusica_pers','2012-04-27 03:02:27'),(21,'atencionintegral','0001_initial','2012-04-27 03:49:18'),(22,'registro','0014_auto__add_field_registrobecauniversitaria_beca__add_field_registrobeca','2012-04-27 03:54:09'),(23,'registro','0015_auto__add_field_registrobecaprimaria_tutoria__add_field_registrobecapr','2012-04-27 04:27:11'),(24,'registro','0016_auto__add_field_registrobecauniversitaria_servicio_social__add_field_r','2012-04-27 04:37:32'),(25,'biblioteca','0001_initial','2012-04-27 17:27:26'),(26,'biblioteca','0002_auto__chg_field_actividadindividual_actividad','2012-04-27 17:37:34'),(27,'promocion','0001_initial','2012-04-30 20:23:30'),(28,'registro','0017_auto__add_field_registromusica_asistencia__add_field_registromusica_re','2012-04-30 20:24:21'),(29,'registro','0018_auto__del_field_registromusica_rezon_no_continuar__add_field_registrom','2012-04-30 20:41:10'),(30,'promocion','0002_auto__add_eventocolectivo','2012-04-30 21:24:23'),(31,'prevencion','0001_initial','2012-05-02 22:10:38'),(32,'sistema','0005_auto__add_salida','2012-06-01 02:08:10'),(33,'sistema','0006_auto__add_filter','2012-06-01 04:37:46');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-06-03 22:51:13
