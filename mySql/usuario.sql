create database if not exists microservice;
use microservice;
create table if not exists usuario (id INTEGER PRIMARY KEY, nome VARCHAR(50) NOT NULL, email VARCHAR(100));
insert into usuario values (1234, "Yuri Barbosa", "yuribarbosa@hotmail.com");
insert into usuario values (5678, "Mayara Anjos", "mayaraanjos@hotmail.com");