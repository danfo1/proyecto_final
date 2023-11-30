let giroLogo1 = "off"
const logInicio = document.querySelector("#car")

let giroLogo2 = "off"
const logSerch = document.querySelector("#serch")

let giroLogo3 = "off"
const logSenting = document.querySelector("#senting")

let giroLogo4 = "off"
const logFinish = document.querySelector("#finish")

document.addEventListener("DOMContentLoaded", function () {
    var objeto = document.getElementById("valeria");
    var posicion = parseInt(localStorage.getItem("posicion")) || 1;
    var tiempoInicio = parseInt(localStorage.getItem("tiempoInicio")) || Date.now();
    var intervalo;

    function actualizarPosicion() {
        var div1 = document.querySelector(".elemento1");
        var div2 = document.querySelector(".elemento2");
        var div3 = document.querySelector(".elemento3");
        var div4 = document.querySelector(".elemento4");

        if (posicion <= 4) {
            /* PRIMER ELEMENTO */
            if (posicion === 1) {
                logInicio.classList.add("fa-spin");
                div1.classList.add("vs1");
                console.log("posicion Actual: " + posicion);
            } else {
                logInicio.classList.remove("fa-spin");
                div1.classList.remove("vs1");
            }

            /* SEGUNDO ELEMENTO */
            if (posicion === 2) {
                logSerch.classList.add("fa-spin");
                div2.classList.add("vs2");
                objeto.style.left = (posicion * 155) + "px";
                console.log("posicion Actual: " + posicion);
            } else {
                logSerch.classList.remove("fa-spin");
                div2.classList.remove("vs2");
            }

            /* TERCER ELEMENTO */
            if (posicion === 3) {
                logSenting.classList.add("fa-spin");
                div3.classList.add("vs3");
                objeto.style.left = (posicion * 200) + "px";
                console.log("posicion Actual: " + posicion);
            } else {
                logSenting.classList.remove("fa-spin");
                div3.classList.remove("vs3");
            }

            /* ELEMENTO FINAL */
            if (posicion === 4) {
                div4.classList.add("vs4");
                objeto.style.left = (posicion * 222) + "px";
                console.log("posicion Actual: " + posicion);
            } else {
                div4.classList.remove("vs4");
            }

            localStorage.setItem("posicion", posicion);
            posicion++;
        } else {
            // Reiniciar posición a 1 cuando alcanza la posición 4
            posicion = 1;
            localStorage.setItem("posicion", posicion);
        }

        // Calcula el tiempo transcurrido desde el inicio
        var tiempoTranscurrido = Date.now() - tiempoInicio;

        // Calcula el tiempo restante antes de la próxima ejecución
        var tiempoRestante = 6000 - (tiempoTranscurrido % 6000);

        // Vuelve a llamar a la función con el nuevo tiempo
        setTimeout(actualizarPosicion, tiempoRestante);
    }

    actualizarPosicion();
});
