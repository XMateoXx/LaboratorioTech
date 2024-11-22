function realizarOperacion(num1, num2, operacion) {
    if (operacion == "suma") {
        return num1 + num2;
    } 
    else if (operacion == "resta") {
        return num1 - num2;
    } 
    else if (operacion == "multiplicacion") {
        return num1 * num2;
    } 
    else if (operacion == "division") {
        if (num2 !== 0) {
            return num1 / num2;
        } else {
            return "No se puede dividir por cero";
        }
    } 
    else {
        return "Error: esta operación no está disponible";
    }
}

let condition = true;

while (condition) {
    const operacion = prompt("¿Qué operación desea realizar? (suma, resta, multiplicacion, division) o escriba 'salir' para terminar");
    if (operacion === "salir") {
        condition = false;
        console.log("Gracias por usar esta calculadora");
    } else {
        const num1 = Number(prompt("Ingrese el primer número"));
        const num2 = Number(prompt("Ingrese el segundo número"));

        const resultado = realizarOperacion(num1, num2, operacion);
        console.log(`El resultado de la operación '${operacion}' es: ${resultado}`);
    }
}

