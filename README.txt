Este es un administrador de contaseñas creada con python y MySQL

La base de datos creada en MySQL seria la siguiente:

CREATE DATABASE password_manager;

CREATE TABLE `manager`(
    `app_name` varchar(20) PRIMARY KEY NOT NULL,
    `email` varchar(100) NOT NULL,
    `username` varchar(20) DEFAULT 'N/A',
    `password` varchar(50) NOT NULL,
    `url` varchar(100) NOT NULL
);


