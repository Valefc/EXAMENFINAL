from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine,desc
from sqlalchemy.orm import sessionmaker, joinedload
from flask import jsonify
from Entity import Estudiante,Curso,Matricula ,Base
from sqlalchemy.exc import IntegrityError
from datetime import date
app= Flask(__name__)

app.secret_key='123456'


# Crear conexión a la base de datos
engine = create_engine('postgresql://postgres:valerito@localhost/ExamenProga')
Base.metadata.bind = engine

# Crear sesión de base de datos
DBSession = sessionmaker(bind=engine)

#Ruta Principal
@app.route('/')
def home():
    return render_template('index.html')

#Listar Estudiantes
@app.route('/estudiante')
def listar_estudiante():
    session= DBSession()
    estudiantes=session.query(Estudiante).all()
    session.close()
    return render_template('estudiante.html',estudiantes=estudiantes)


### Agregar Estudiante
@app.route('/estudiante/agregar', methods=['GET', 'POST'])
def agregar_estudiante():
    if request.method == 'POST':
        session = DBSession()
        Estudiante.agregarEstudiante(session,
                               request.form['nombreestudiante'],
                               request.form['apellidopaterno'],
                               request.form['apellidomaterno'],
                               request.form['edadestudiante'],
                               request.form['direccionestudiante'])  # Puede ser None
        session.close()
        return redirect(url_for('listar_estudiante'))
    else:
        return render_template('agregar_estudiante.html')


### Editar Estudiante
@app.route('/estudiante/editar/<int:id_estudiante>', methods=['GET', 'POST'])
def editar_estudiante(id_estudiante):
    session = DBSession()
    if request.method == 'POST':
        # Modificar estudiante con los datos del formulario
        Estudiante.modificarEstudiante(session, id_estudiante,
                                 nombreestudiante=request.form['nombreestudiante'],
                                 apellidopaterno=request.form['apellidopaterno'],
                                 apellidomaterno=request.form['apellidomaterno'],
                                 edadestudiante=request.form['edadestudiante'],
                                 direccionestudiante=request.form['direccionestudiante'])  # Puede ser None
        session.close()
        return redirect(url_for('listar_estudiante'))
    else:
        # Obtener los datos del estudiante a editar
        estudiante = session.query(Estudiante).filter_by(idestudiante=id_estudiante).first()
        session.close()
        return render_template('index.html', estudiante=estudiante, editar=True)  # Pasar la bandera "editar" a la plantilla


###Eliminar Estudiante
@app.route('/estudiante/eliminar/<int:id_estudiante>')
def eliminar_estudiante(id_estudiante):
    session = DBSession()
    Estudiante.eliminarEstudiante(session, id_estudiante)
    session.close()
    return redirect(url_for('listar_estudiante'))

##Listar Curso
@app.route('/curso')
def listar_curso():
    session= DBSession()
    curso =session.query(Curso).all()
    session.close()
    return render_template('curso.html',curso=curso)

# Agregar Curso
@app.route('/curso/agregar', methods=['GET', 'POST'])
def agregar_curso():
    if request.method == 'POST':
        session = DBSession()
        Curso.agregarCurso(session,
                               request.form['nombrecurso'],
                               request.form['descripcioncurso'],
                               request.form['cantidadcreditos'])  # Puede ser None
        session.close()
        return redirect(url_for('listar_curso'))
    else:
        return render_template('agregar_curso.html')

# Editar curso
@app.route('/curso/editar/<int:id_curso>', methods=['GET', 'POST'])
def editar_curso(id_curso):
    session = DBSession()
    if request.method == 'POST':
        # Modificar la Curso con los datos del formulario
        Curso.modificarCurso(session, id_curso,
                                 nombrecurso=request.form['nombrecurso'],
                                 descripcioncurso=request.form['descripcioncurso'],
                                 cantidadcreditos=request.form['cantidadcreditos'])  # Puede ser None
        session.close()
        return redirect(url_for('listar_curso'))
    else:
        # Obtener los datos del curso a editar
        curso= session.query(Curso).filter_by(idcurso=id_curso).first()
        session.close()
        return render_template('index.html', curso=curso, editar=True)  # Pasar la bandera "editar" a la plantilla

# Eliminar Curso
@app.route('/curso/eliminar/<int:id_curso>')
def eliminar_curso(id_curso):
    session = DBSession()
    Curso.eliminarCurso(session, id_curso)
    session.close()
    return redirect(url_for('listar_curso'))

#Listar Matriculas
@app.route('/matricula')
def listar_matricula():
    session= DBSession()
    matriculas =session.query(Matricula).all()
    session.close()
    return render_template('matricula.html',matriculas=matriculas)

### Agregar Matricula
@app.route('/matricula/agregar', methods=['GET', 'POST'])
def agregar_matricula():
    if request.method == 'POST':
        session = DBSession()
        Matricula.agregarMatricula(session,
                               request.form['fechamatriculacion'],
                               request.form['idestudiante'],
                               request.form['idcurso'])  # Puede ser None
        session.close()
        return redirect(url_for('listar_matricula'))
    else:
        return render_template('agregar_matricula.html')


### Editar Matrícula
@app.route('/matricula/editar/<int:id_matricula>', methods=['GET', 'POST'])
def editar_matricula(id_matricula):
    session = DBSession()
    if request.method == 'POST':
        # Modificar la matricula con los datos del formulario
        Matricula.modificarMatricula(session, id_matricula,
                                 fechamatriculacion=request.form['fechamatriculacion'],
                                 idestudiante=request.form['idestudiante'],
                                 idcurso=request.form['idcurso'])  # Puede ser None
        session.close()
        return redirect(url_for('listar_matricula'))
    else:
        # Obtener los datos de la matrícula a editar
        matricula = session.query(Matricula).filter_by(idmatricula=id_matricula).first()
        session.close()
        return render_template('index.html', matricula=matricula, editar=True)  # Pasar la bandera "editar" a la plantilla

###Eliminar matrícula
@app.route('/matricula/eliminar/<int:id_matricula>')
def eliminar_matricula(id_matricula):
    session = DBSession()
    Matricula.eliminarMatricula(session, id_matricula)
    session.close()
    return redirect(url_for('listar_matricula'))















if __name__=='__main__':
    app.run(debug=True)
