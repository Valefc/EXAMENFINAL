// Función para cargar los datos del curso seleccionada en la modal de edición
function editarCurso(idcurso,nombrecurso,descripcioncurso,cantidadcreditos) {
    document.getElementById('editaridcurso').value = idcurso;
    document.getElementById('editarnombrecurso').value = nombrecurso;
    document.getElementById('editardescripcioncurso').value = descripcioncurso;
    document.getElementById('editarcantidadcreditos').value = cantidadcreditos;

    // Modificar el atributo 'action' del formulario con la URL adecuada
    var editarEstudianteForm = document.getElementById('editarCursoForm');
    editarCursoForm.action = '/curso/editar/' + idcurso;

    // Abrir la modal de edición
    var myModal = new bootstrap.Modal(document.getElementById('modalEditarCurso'), {
        keyboard: false
    });
    myModal.show();
}