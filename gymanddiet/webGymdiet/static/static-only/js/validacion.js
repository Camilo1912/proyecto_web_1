$(document).ready(function () {
    $("#form").validate({
        rules: {
            genero: {
                required: true,
            },
            peso: {
                required: true,
                max: 544,
                min:2.5
            },
            edad: {
                required: true,
                number: true,
                min: 1,
                max: 99
            },
            altura: {
                required: true,
                number: true,
                max: 2.72,
                min:0.45
            },
            ejercicio: {
                required: true,
            }
        },
        messages: {
            genero: {
                required: "Escoga un genero"
            },
            peso: {
                required: "Escriba su peso",
                number: "Escriba su peso en numero",
                max: "No se aceptan más de 544 kg",
                min:"No se aceptan menos de 2,45 kg"
            },
            edad: {
                required: "Escriba su edad",
                number: "Escriba su edad en numero",
                min: "No se aceptan 0 años e inferior",
                max: "No se aceptan 100 años y superior"
            },
            altura: {
                required: "Escriba su altura",
                number: "Escriba su altura en numero",
                max: "No se aceptan 2,73 metros y superior",
                min: "No se aceptan 44 cm e inferior"
            },
            ejercicio: {
                required:"Porfavor seleccione una opcion"
            }
        }


    });
});