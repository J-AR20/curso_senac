INSERT INTO bebes(matricula,nome,peso,altura,data_nasc,codigo_equipe,cpf) VALUES
	(123,"Novin1",4.5,0.5,"01/02/2023",456,"012.123.654-98"),
    (4321,"Novin2",4.6,0.6,"02/02/2023",456,"014.123.854-00");

INSERT INTO medicos(codigo_equipe,crm,especialidade,nome) VALUES
	(123,"Novin1",4.5,0.5,"01/02/2023",456,"012.123.654-98"),
    (4321,"Novin2",4.6,0.6,"02/02/2023",456,"014.123.854-00");


UPDATE bebes
	SET codigo_equipe = 456
    WHERE cpf = '014.123.854-00'