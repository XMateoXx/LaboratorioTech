const form = document.getElementById('contactForm');

function validarFormulario(event) {
    event.preventDefault();

    const nombre = document.getElementById('nombre').value.trim();
    const motivo = document.getElementById('motivo').value;
    const correo = document.getElementById('correo').value.trim();
    const mensaje = document.getElementById('mensaje').value.trim();

    if (!nombre || !motivo || !correo || !mensaje) {
        alert('Todos los campos son obligatorios.');
        return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(correo)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return;
    }

    alert('Formulario enviado con éxito.');
    form.reset(); 
}

form.addEventListener('submit', validarFormulario);
