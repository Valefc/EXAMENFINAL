// Función para cargar los datos de la oficina seleccionada en la modal de edición
function editarEstudiante(idEstudiante, nombreEstudiante, apellidoPaterno,apellidoMaterno, edadEstudiante, direccionEstudiante) {
    document.getElementById('editarIdEstudiante').value = idEstudiante;
    document.getElementById('editarnombreestudiante').value = nombreEstudiante;
    document.getElementById('editarapellidopaterno').value = apellidoPaterno;
    document.getElementById('editarapellidomaterno').value = apellidoMaterno;
    document.getElementById('editaredadestudiante').value = edadEstudiante;
    document.getElementById('editardireccionestudiante').value = direccionEstudiante;

    // Modificar el atributo 'action' del formulario con la URL adecuada
    var editarEstudianteForm = document.getElementById('editarEstudianteForm');
    editarEstudianteForm.action = '/estudiante/editar/' + idEstudiante;

    // Abrir la modal de edición
    var myModal = new bootstrap.Modal(document.getElementById('modalEditarEstudiante'), {
        keyboard: false
    });
    myModal.show();
}