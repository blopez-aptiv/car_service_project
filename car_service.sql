-- -----------------------------------------------------
-- Schema servicio_carro
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `servicio_carro` DEFAULT CHARACTER SET utf8 ;
USE `servicio_carro` ;

-- Table `servicio_carro`.`estado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`estado` (
  `id_estado` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_estado`))
ENGINE = InnoDB;

REPLACE INTO `servicio_carro`.`estado` (`id_estado`, `descripcion`) VALUES
	(1, 'San Luis Potosi'),
	(2, 'Queretaro');

-- Table `servicio_carro`.`sucursal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`sucursal` (
  `id_sucursal` INT NOT NULL AUTO_INCREMENT,
  `id_estado` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  `codigo_postal` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_sucursal`),
  CONSTRAINT `id_estado`
    FOREIGN KEY (`id_estado`)
    REFERENCES `servicio_carro`.`estado` (`id_estado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `servicio_carro`.`tipo_servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`tipo_servicio` (
  `id_tipo` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NOT NULL,
  `costo` INT NOT NULL,
  PRIMARY KEY (`id_tipo`))
ENGINE = InnoDB;

REPLACE INTO `servicio_carro`.`tipo_servicio` (`id_tipo`, `descripcion`, `costo`) VALUES
	(1, '5000km o 3 meses', 1690),
	(2, '10,000km o 6 meses', 1860),
	(3, '20,000km o 12 meses', 2680),
	(4, '200,000km o 120 meses', 3830);

-- -----------------------------------------------------
-- Table `servicio_carro`.`tipo_vehiculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`tipo_vehiculo` (
  `id_tipo` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_tipo`))
ENGINE = InnoDB;

REPLACE INTO `servicio_carro`.`tipo_vehiculo` (`id_tipo`, `descripcion`) VALUES
	(1, 'carro'),
	(2, 'motocicleta'),
	(3, 'automovil de 3 ruedas');

-- -----------------------------------------------------
-- Table `servicio_carro`.`estado_servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`estado_servicio` (
  `id_estado_servicio` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_estado_servicio`))
ENGINE = InnoDB;

REPLACE INTO `servicio_carro`.`estado_servicio` (`id_estado_servicio`, `descripcion`) VALUES
	(1, 'recibido'),
	(2, 'en procceso'),
	(3, 'suspendido'),
	(4, 'listo');

-- -----------------------------------------------------
-- Table `servicio_carro`.`vehiculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`vehiculo` (
  `id_vehiculo` INT NOT NULL AUTO_INCREMENT,
  `id_tipo` INT NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `ruedas` INT NOT NULL,
  `modelo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_vehiculo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `servicio_carro`.`motor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`motor` (
  `id_motor` INT NOT NULL,
  `tipo_motor` VARCHAR(45) NOT NULL,
  `cilindro` INT NOT NULL,
  PRIMARY KEY (`id_motor`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `servicio_carro`.`carro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`carro` (
  `id_carro` INT NOT NULL,
  `modelo` VARCHAR(45) NOT NULL,
  `id_motor` INT NOT NULL,
  PRIMARY KEY (`id_carro`),
  CONSTRAINT `id_motor_1`
    FOREIGN KEY (`id_motor`)
    REFERENCES `servicio_carro`.`motor` (`id_motor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `servicio_carro`.`moto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`moto` (
  `id_moto` INT NOT NULL AUTO_INCREMENT,
  `modelo` VARCHAR(45) NOT NULL,
  `id_motor` INT NOT NULL,
  PRIMARY KEY (`id_moto`),
  CONSTRAINT `id_motor_2`
    FOREIGN KEY (`id_motor`)
    REFERENCES `servicio_carro`.`motor` (`id_motor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `servicio_carro`.`role`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`role` (
  `id_role` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_role`))
ENGINE = InnoDB;

REPLACE INTO `servicio_carro`.`role` (`id_role`, `descripcion`) VALUES
	(1, 'empleado'),
	(2, 'cliente');

-- -----------------------------------------------------
-- Table `servicio_carro`.`persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`persona` (
  `id_persona` INT NOT NULL AUTO_INCREMENT,
  `id_role` INT NOT NULL,
  `contrasena` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  `correo` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_persona`),
  CONSTRAINT `id_role`
    FOREIGN KEY (`id_role`)
    REFERENCES `servicio_carro`.`role` (`id_role`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `servicio_carro`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`cliente` (
  `id_cliente` INT NOT NULL,
  `id_vehiculo` INT NOT NULL,
  `ultimo_servicio` DATETIME NOT NULL,
  PRIMARY KEY (`id_cliente`),
  CONSTRAINT `id_vehiculo`
    FOREIGN KEY (`id_vehiculo`)
    REFERENCES `servicio_carro`.`vehiculo` (`id_vehiculo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `servicio_carro`.`empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`empleado` (
  `id_empleado` INT NOT NULL,
  `id_sucursal` INT NOT NULL,
  `salario` INT,
  `puesto` VARCHAR(45),
  PRIMARY KEY (`id_empleado`),
  CONSTRAINT `id_sucursal_1`
    FOREIGN KEY (`id_sucursal`)
    REFERENCES `servicio_carro`.`sucursal` (`id_sucursal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `servicio_carro`.`session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`session` (
  `id_session` INT NOT NULL AUTO_INCREMENT,
  `id_persona` INT NOT NULL,
  `token` VARCHAR(45) NOT NULL,
  `activa` BOOL NOT NULL DEFAULT false,
  PRIMARY KEY (`id_session`),
  CONSTRAINT `id_persona`
    FOREIGN KEY (`id_persona`)
    REFERENCES `servicio_carro`.`persona` (`id_persona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `servicio_carro`.`servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`servicio` (
  `id_servicio` INT NOT NULL AUTO_INCREMENT,
  `id_vehiculo` INT NOT NULL,
  `id_estado_servicio` INT NOT NULL,
  `id_tipo_servicio` INT NOT NULL,
  PRIMARY KEY (`id_servicio`),
  CONSTRAINT `id_estado_servicio`
    FOREIGN KEY (`id_estado_servicio`)
    REFERENCES `servicio_carro`.`estado_servicio` (`id_estado_servicio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_tipo_servicio`
    FOREIGN KEY (`id_tipo_servicio`)
    REFERENCES `servicio_carro`.`tipo_servicio` (`id_tipo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `servicio_carro`.`cita`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio_carro`.`cita` (
  `id_cita` INT NOT NULL AUTO_INCREMENT,
  `id_servicio` INT NOT NULL,
  `id_cliente` INT NOT NULL,
  `id_sucursal` INT NOT NULL,
  `fecha` DATETIME NOT NULL,
  PRIMARY KEY (`id_cita`),
  CONSTRAINT `id_servicio`
    FOREIGN KEY (`id_servicio`)
    REFERENCES `servicio_carro`.`servicio` (`id_servicio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_cliente`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `servicio_carro`.`cliente` (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_sucursal_2`
    FOREIGN KEY (`id_sucursal`)
    REFERENCES `servicio_carro`.`sucursal` (`id_sucursal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


