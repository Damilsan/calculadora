let pantalla = document.getElementById("pantalla");
let operacion = "";

function agregarNumero(numero){
    operacion += numero;
    actualizarpantalla();
}

function agregarOperador(operador){
    if(operacion !== "" && !/[\+\-\*\/]$/.test(operacion)){
        operacion += operador;
        actualizarpantalla();
    }
}

function calcularResultado() {
    try{
        operacion = eval(operacion).toString();   
    } catch (error){
        operacion = "Error";
    }
    actualizarpantalla();
}

function limpiarPantalla(){
    operacion = "";
    actualizarpantalla();
}

function actualizarpantalla(){
    pantalla.value = operacion;
}