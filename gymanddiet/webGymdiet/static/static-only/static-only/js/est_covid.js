$("#covid-regiones-buscar").click(function(event) {
    event.preventDefault();

 // para limpiar el contedor antes de desplegar
    $("#resultado-region").empty();

    /* var region = $(#region).val() */
    var seleccion = $("#cmb-covid").val();

    $.ajax({
        url: 'https://covid-api.mmediagroup.fr/v1/cases?country=Chile',
        data: {
           format: 'json'
        },
        error: function() {
           $('#resultado-region').html('<p>No se pudo detectar el region</p>');
        },
        dataType: 'json',
        success: function(data) {
           console.log(data);
           var $muertesRegion = $('<p>').text(data[seleccion].deaths);
           var $confirmadosRegion = $('<p>').text(data[seleccion].confirmed);
           var $recuperadosRegion = $('<p>').text(data[seleccion].recovered);
           $('#resultado-region').append("Muertes totales")
           $('#resultado-region').append($muertesRegion);
           $('#resultado-region').append("Casos totales confirmados")
           $('#resultado-region').append($confirmadosRegion);
           $('#resultado-region').append("Total recuperados")
           $('#resultado-region').append($recuperadosRegion);
        },
        type: 'GET'
    });

});

$(document).ready(function() {

    // para limpiar el contedor antes de desplegar
    $("#covid-pais").empty();
   
    $.ajax({
        url: 'https://covid-api.mmediagroup.fr/v1/cases?country=Chile',
        data: {
            format: 'json'
        },
        error: function() {
            $('#covid-pais').html('<p>No se pudo obtener las estadisticas</p>');
        },
        dataType: 'json',
        success: function(data) {
            /* console.log(data); */
            var $muertes = $('<p>').text(data.All.deaths);
            var $confirmados = $('<p>').text(data.All.confirmed);
            var $recuperados = $('<p>').text(data.All.recovered);

            $('#covid-pais').append("Muertes totales")
            $('#covid-pais').append($muertes);
            $('#covid-pais').append("Casos totales confirmados")
            $('#covid-pais').append($confirmados);
            $('#covid-pais').append("Total recuperados")
            $('#covid-pais').append($recuperados);
        },
        type: 'GET'
    });
   
});