CREATE DATABASE IF NOT EXISTS Estoque;

USE Estoque;

CREATE TABLE IF NOT EXISTS produto(
 codigo INT NOT NULL UNIQUE,
 descricao VARCHAR(50),
quantidade INT,
valor FLOAT,
est_minimo INT,
 PRIMARY KEY (codigo));
 
CREATE TABLE IF NOT EXISTS cliente(
 cpf VARCHAR(14) NOT NULL UNIQUE,
 nome VARCHAR(50),
endereco VARCHAR(100),
telefone VARCHAR(14),
sexo VARCHAR(1),
 PRIMARY KEY (cpf));
 
 CREATE TABLE IF NOT EXISTS compra(
 numero INT NOT NULL UNIQUE,
 cpf VARCHAR(14) NOT NULL,
 codigo INT NOT NULL,
 data VARCHAR(10),
 qtd_compra INT,
 PRIMARY KEY (numero),
FOREIGN KEY (cpf) REFERENCES cliente(cpf),
FOREIGN KEY (codigo) REFERENCES produto(codigo));

INSERT INTO produto VALUES(101,'tablet',10,1200,2);
INSERT INTO produto VALUES(102,'pendrive',50,20,10);
INSERT INTO produto VALUES(103,'notebook',15,1800,3);
INSERT INTO produto VALUES(104,'impressora',20,200,5);
INSERT INTO produto VALUES(105,'monitor',50,300,10);

INSERT INTO cliente VALUES(1010,'João','Rua XYZ','988778877','M');
INSERT INTO cliente VALUES(1020,'Antônio','Rua ABC','922336655','M');
INSERT INTO cliente VALUES(1030,'Pedro','Rua sem saída','966558899','M');
INSERT INTO cliente VALUES(1040,'Maria','Rua do alfabeto','977885566','F');
INSERT INTO cliente VALUES(1050,'Joaquina','Rua dos prazeres','911223344','F');

INSERT INTO compra VALUES(1,1020,101, "10/05/2023",5);
INSERT INTO compra VALUES(2,1010,101, "11/05/2023",5);
INSERT INTO compra VALUES(3,1030,105, "15/05/2023",5);
INSERT INTO compra VALUES(4,1030,101, "10/05/2023",1);
INSERT INTO compra VALUES(5,1010,105, "11/05/2023",5);
INSERT INTO compra VALUES(6,1040,104, "12/05/2023",2);
INSERT INTO compra VALUES(7,1040,103, "15/05/2023",1);