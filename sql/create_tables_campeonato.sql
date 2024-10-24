-- MySQL Workbench Synchronization
-- Generated: 2024-10-23 00:06
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: souza

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `campeonato_de_futebol` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;

CREATE TABLE IF NOT EXISTS `campeonato_de_futebol`.`estadios` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `cidade` VARCHAR(100) NOT NULL,
  `estado` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `campeonato_de_futebol`.`jogadores` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `posicao` VARCHAR(50) NOT NULL,
  `numero` INT(11) NOT NULL,
  `time_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `time_id` (`time_id` ASC) VISIBLE,
  CONSTRAINT `jogadores_ibfk_1`
    FOREIGN KEY (`time_id`)
    REFERENCES `campeonato_de_futebol`.`times` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `campeonato_de_futebol`.`partidas` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `data` DATE NOT NULL,
  `horario` TIME NOT NULL,
  `time_casa_id` INT(11) NOT NULL,
  `time_visitante_id` INT(11) NOT NULL,
  `estadio_id` INT(11) NOT NULL,
  `gols_time_casa` INT(11) NOT NULL,
  `gols_time_visitante` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `time_casa_id` (`time_casa_id` ASC) VISIBLE,
  INDEX `time_visitante_id` (`time_visitante_id` ASC) VISIBLE,
  INDEX `estadio_id` (`estadio_id` ASC) VISIBLE,
  CONSTRAINT `partidas_ibfk_1`
    FOREIGN KEY (`time_casa_id`)
    REFERENCES `campeonato_de_futebol`.`times` (`id`),
  CONSTRAINT `partidas_ibfk_2`
    FOREIGN KEY (`time_visitante_id`)
    REFERENCES `campeonato_de_futebol`.`times` (`id`),
  CONSTRAINT `partidas_ibfk_3`
    FOREIGN KEY (`estadio_id`)
    REFERENCES `campeonato_de_futebol`.`estadios` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 14
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `campeonato_de_futebol`.`times` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `cidade` VARCHAR(100) NOT NULL,
  `estado` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
