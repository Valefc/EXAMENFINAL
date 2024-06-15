CREATE TABLE estudiante (
  idestudiante SERIAL PRIMARY KEY,
  nombreestudiante VARCHAR(45) NOT NULL,
  apellidopaterno VARCHAR(45) NOT NULL,
  apellidomaterno VARCHAR(45) NOT NULL,
  edadestudiante INTEGER NOT NULL,
  direccionestudiante VARCHAR(50) NOT NULL
);

-- Crear la tabla 'curso'
CREATE TABLE curso (
  idcurso SERIAL PRIMARY KEY,
  nombrecurso VARCHAR(45) NOT NULL,
  descripcioncurso VARCHAR(45) NOT NULL,
  cantidadcreditos INTEGER NOT NULL
);

-- Crear la tabla 'matricula'
CREATE TABLE matricula (
  idmatricula SERIAL PRIMARY KEY,
  fechamatriculacion DATE NOT NULL,
  idestudiante INTEGER REFERENCES estudiante(idestudiante),
  idcurso INTEGER REFERENCES curso(idcurso)
);