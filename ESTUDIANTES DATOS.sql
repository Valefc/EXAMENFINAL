INSERT INTO estudiante (nombreestudiante, apellidopaterno, apellidomaterno, edadestudiante, direccionestudiante)
VALUES
  ('Juan', 'Perez', 'Gomez', 20, 'Calle Principal 123'),
  ('María', 'Lopez', 'Garcia', 22, 'Avenida Central 456'),
  ('Pedro', 'Gonzalez', 'Martinez', 21, 'Plaza Mayor 789'),
  ('Laura', 'Rodriguez', 'Fernandez', 19, 'Paseo del Sol 567'),
  ('Carlos', 'Sanchez', 'Diaz', 23, 'Carrera Secundaria 321'),
  ('Ana', 'Gutierrez', 'Hernandez', 20, 'Camino Real 234'),
  ('Jorge', 'Torres', 'Jimenez', 22, 'Avenida del Norte 890'),
  ('Sofia', 'Ramirez', 'Alvarez', 21, 'Callejón del Sur 432');

-- Insertar datos de ejemplo en la tabla 'curso'
INSERT INTO curso (nombrecurso, descripcioncurso, cantidadcreditos)
VALUES
  ('Matemáticas', 'Curso introductorio a las matemáticas', 4),
  ('Historia', 'Curso de historia mundial', 3),
  ('Programación', 'Curso básico de programación', 5),
  ('Literatura', 'Curso de literatura universal', 3),
  ('Economía', 'Curso de fundamentos de economía', 4),
  ('Inglés', 'Curso de inglés avanzado', 5),
  ('Biología', 'Curso de biología celular', 4),
  ('Arte', 'Curso de historia del arte', 3);

-- Obtener los ids de los estudiantes y cursos insertados
SELECT idestudiante, idcurso FROM estudiante, curso;

-- Insertar datos de ejemplo en la tabla 'matricula'
INSERT INTO matricula (fechamatriculacion, idestudiante, idcurso)
VALUES
  ('2023-01-15', 1, 3),  
  ('2023-01-16', 2, 1),  
  ('2023-01-17', 3, 2),  
  ('2023-01-18', 4, 4), 
  ('2023-01-19', 5, 6), 
  ('2023-01-20', 6, 5),  
  ('2023-01-21', 7, 7),  
  ('2023-01-22', 8, 8);  