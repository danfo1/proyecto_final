const nombres = document.querySelector('#nombres');
const appellidos = document.querySelector('#apellidos');
const documento = document.querySelector('#documento');
const telefono = document.querySelector('#telefono');
const usuario = document.querySelector('#usuario');
const contrasena = document.querySelector('#contrasena');
const rol = document.querySelector('#rol');
const btn = document.querySelector('#btn');




nombres.addEventListener('input', verificar);
appellidos.addEventListener('input', verificar);
documento.addEventListener('input', verificar);
telefono.addEventListener('input', verificar);
usuario.addEventListener('input', verificar);
contrasena.addEventListener('input', verificar);
rol.addEventListener('input', verificar);

function verificar(){
    if(nombres.value === '' || appellidos.value === '' || documento.value === '' || correo.value === '' || telefono.value === '' || usuario.value === '' || contrasena.value === '' || rol.value === ''){
        btn.setAttribute('disabled', 'disabled');
        btn.style.cursor = 'not-allowed';
    }else{
        btn.removeAttribute('disabled');
        btn.style.cursor = 'pointer';
    }
};

document.addEventListener("DOMContentLoaded", verificar)
