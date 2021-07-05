$(function () {
    $("#ingresar").click(function (event) {
        event.preventDefault();

        var genero = $("input:radio[name='genero']:checked").val();
        var peso = $("#peso").val();
        var altura = $("#altura").val();
        var edad = $("#edad").val();
        var ejercicio = $("#ejercicio").val();

        if (genero == 'Masculino') {
            function calcular_deficit(p, a, e) {
                return (10 * p + 6.25 * a - 5 * e) + 5;
            }
            //Formula cuando es hombre
        } else if (genero == 'Femenino') {
            function calcular_deficit(p, a, e) {
                return (10 * p + 6.25 * a - 5 * e) - 161;
            }
            //Formula cuando es mujer
        } else {
            alert("Genero no agregado")
        }

        var deficit = calcular_deficit(peso, altura, edad);
        var deficit = deficit * ejercicio;

        $('.valor-deficit').empty();
        $('.recomendacion').empty();

        if(peso ==""){
            alert("Falta agregar su peso")
        } else if (altura==""){
            alert("Falta agregar su estatura")
        } else if (edad==""){
            alert("Falta agregar su edad")
        } else if (ejercicio=="0"){
            alert("No selecciono cuantas veces hace ejercicio")
        } else if (ejercicio=="1.2"){
            $('.valor-deficit').append('su deficit calorico es de ' + deficit + ' calorias, es decir, deberia comer ' + deficit + ' calorias diarias para mantener su peso actual (' + peso + 'kg)');
            $('.recomendacion').append('¡Se recomienda hacer ejercicio 1 o 2 veces a la semana como minimo!')
        } else {
            $('.valor-deficit').append('su deficit calorico es de ' + deficit + ' calorias, es decir, deberia comer ' + deficit + ' calorias diarias para mantener su peso actual (' + peso + 'kg)');
        }
    });
});