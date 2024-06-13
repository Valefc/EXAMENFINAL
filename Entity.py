from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
Base= declarative_base()

#Estudiante

class Estudiante(Base):
    __tablename__='estudiante'
    idestudiante=Column(Integer, primary_key=True)
    nombreestudiante=Column(String(45), nullable=False)
    apellidopaterno=Column(String(45), nullable=False)
    apellidomaterno=Column(String(45), nullable=False)
    edadestudiante=Column(Integer, nullable=False)
    direccionestudiante=Column(String(50), nullable=False)
    
    @staticmethod
    def mostrar_todos_los_estudiantes(session):
        estudiantes= session.query(Estudiante).all()
        for est in estudiantes:
            print("ID de estudiante:", est.idestudiante)
            print("Nombre Estudiante:", est.nombreestudiante)
            print("Apellido Paterno:", est.apellidopaterno)
            print("Apelldio Materno:", est.apellidomaterno)
            print("Edad Estudiante:", est.edadestudiante)
            print("Dirección Estudiante:", est.direccionestudiante)
            print("-------------------------------------------")
            
    @staticmethod
    def agregarEstudiante(session, nombreestudiante,apellidopaterno,apellidomaterno,edadestudiante,direccionestudiante):
        nuevoEstudiante=Estudiante(nombreestudiante=nombreestudiante,apellidopaterno=apellidopaterno,apellidomaterno=apellidomaterno,edadestudiante=edadestudiante,direccionestudiante=direccionestudiante)
        session.add(nuevoEstudiante)
        session.commit()
        print('Estudiante agregado correctamente')

    @staticmethod
    def modificarEstudiante(session, id_estudiante, **kwargs):
        estudinate= session.query(Estudiante).filter_by(idestudinate=id_estudiante).first()
        if estudinate:
            for key, value in kwargs.items():
                setattr(estudinate, key, value)
            session.commit()
            print('Estudinate actualizado')
        else:
            print('Estudiante no encontrado')
            
    @staticmethod
    def eliminarEstudiante(session, id_estudiante):
        estudiante= session.query(Estudiante).filter_by(idestudiante=id_estudiante).first()
        if estudiante:
            session.delete(estudiante)
            session.commit()
            print('Estudiante eliminado')
        else:
            print('Estudiante no encontrado')
    
    
#Curso

class Curso(Base):
    __tablename__='curso'
    idcurso=Column(Integer, primary_key=True)
    nombrecurso=Column(String(45), nullable=False)
    descripcioncurso=Column(String(45), nullable=False)
    cantidadcreditos=Column(Integer, nullable=False)
    
    @staticmethod
    def mostrar_todos_los_cursos(session):
        cursos= session.query(Curso).all()
        for cur in cursos:
            print("ID de Curso:", cur.idcurso)
            print("Nombre Curso:", cur.nombrecurso)
            print("Descripción Curso:", cur.descripcioncurso)
            print("Cantidad de Créditos:", cur.cantidadcreditos)
            print("-------------------------------------------")
    
    @staticmethod
    def agregarCurso(session, nombrecurso,descripcioncurso,cantidadcreditos):
        nuevoCurso=Curso(nombrecurso=nombrecurso,descripcioncurso=descripcioncurso,cantidadcreditos=cantidadcreditos)
        session.add(nuevoCurso)
        session.commit()
        print('Curso agregado correctamente')

    @staticmethod
    def modificarCurso(session, id_curso, **kwargs):
        curso= session.query(Curso).filter_by(idcurso=id_curso).first()
        if curso:
            for key, value in kwargs.items():
                setattr(curso, key, value)
            session.commit()
            print('Curso actualizado')
        else:
            print('Curso no encontrado')
            
    @staticmethod
    def eliminarCurso(session, id_curso):
        curso= session.query(Curso).filter_by(idcurso=id_curso).first()
        if curso:
            session.delete(curso)
            session.commit()
            print('Curso eliminado')
        else:
            print('Curso no encontrado')

#Mátricula

class Matricula(Base):
    __tablename__='matricula'
    idmatricula=Column(Integer, primary_key=True)
    fechamatriculacion=Column(Date,nullable=False)
    idestudiante=Column(Integer, ForeignKey('estudiante.idestudiante'))
    idcurso=Column(Integer, ForeignKey('curso.idcurso'))
    estudiante=relationship('Estudiante')
    curso=relationship('Curso')
    
    @staticmethod
    def mostrar_todos_las_matriculas(session):
        matriculas= session.query(Matricula).all()
        for mat in matriculas:
            print("ID de Matrícula:", mat.idmatricula)
            print("Fecha Matriculación:", mat.fechamatriculacion)
            print("ID Estudiante:", mat.idestudiante)
            print("ID Curso:", mat.idcurso)
            print("-------------------------------------------")
    
    @staticmethod
    def agregarMatricula(session, fechamatriculacion,idestudiante,idcurso):
        nuevaMatricula=Matricula(fechamatriculacion=fechamatriculacion,idestudiante=idestudiante,idcurso=idcurso)
        session.add(nuevaMatricula)
        session.commit()
        print('Matricula agregada correctamente')

    @staticmethod
    def modificarMatricula(session, id_matricula, **kwargs):
        matri= session.query(Matricula).filter_by(idmatricula=id_matricula).first()
        if matri:
            for key, value in kwargs.items():
                setattr(matri, key, value)
            session.commit()
            print('Matricula actualizado')
        else:
            print('Matricula no encontrado')
            
    @staticmethod
    def eliminarMatricula(session, id_matricula):
        matricula= session.query(Matricula).filter_by(idmatricula=id_matricula).first()
        if matricula:
            session.delete(matricula)
            session.commit()
            print('Matricula eliminada')
        else:
            print('Matricula no encontrado')