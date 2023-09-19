
$(document).ready(function () {
    // Manejar el envío del formulario
    $('#modalCarrito form').submit(function (event) {
        event.preventDefault(); // Evita que se envíe el formulario de forma predeterminada

        // Aquí puedes agregar la lógica para agregar el producto al carrito
        // Por ejemplo, realizar una solicitud AJAX al servidor para agregar el producto

        // Mostrar el mensaje de alerta
        $('#mensajeAlerta').show();

        // Cerrar la modal después de un breve retraso (opcional)
        setTimeout(function () {
            $('#modalCarrito').modal('hide');
        }, 2000); // La modal se cierra después de 2 segundos (puedes ajustar este valor)
    });
});

