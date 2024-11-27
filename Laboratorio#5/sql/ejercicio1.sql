CREATE TABLE estudiante (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

INSERT INTO estudiante (nombre, edad, ciudad) VALUES ('Juan', 20, 'Bogotá');
INSERT INTO estudiante (nombre, edad, ciudad) VALUES ('Ana', 22, 'Medellín');
INSERT INTO estudiante (nombre, edad, ciudad) VALUES ('Luis', 19, 'Cali');

SELECT * FROM estudiante;

SELECT * FROM estudiante WHERE ciudad = 'Bogotá';

SELECT * FROM estudiante WHERE edad > 20;