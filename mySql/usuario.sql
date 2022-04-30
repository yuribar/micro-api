create database if not exists microservice;
use microservice;
create table if not exists usuario (id INTEGER PRIMARY KEY, nome VARCHAR(50) NOT NULL, email VARCHAR(100));

INSERT INTO usuario (id, nome, email ) VALUES (1234, "Yuri", "yuribarbosa@hotmail.com");
