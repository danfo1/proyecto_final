let reiniciar = document.querySelector("#rc");

reiniciar.addEventListener("click", () => {

    localStorage.removeItem("posicion");

    window.open("http://127.0.0.1:5500/segumiento.html");
});

let finalizar = document.querySelector("#fn");

finalizar.addEventListener("click", () => {

    localStorage.setItem("posicion", "4");

    window.open("http://127.0.0.1:5500/segumiento.html");
}); 