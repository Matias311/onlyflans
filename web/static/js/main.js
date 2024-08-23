// Capturar el evento de enviar al cerrar sesion
const form = document.querySelector("#logout-form");

function cerrar_sesion(event) {
  event.preventDefault();
  form.submit();
}
