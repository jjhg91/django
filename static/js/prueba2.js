$('#deporte').on('change',inicio);
function inicio(){
    var id = $(this).val();
    $.ajax({
        data:{'id_deporte':id},
        url:'/perfil/busqueda/',
        type:'GET',
        success: function(data){
            var html = ""
            for (var i = 0; i < data.length ; i++){
                html += '<option value="'+data[i].pk+'">'+data[i].fields.ligas+' - '+data[i].pk+'</option>'
               // html += '<p><b>'+data[i].fields.ligas+'</b></p>'
            }
            $('#liga').html(html);
        }
    });
}


$('#liga').on('change',despues);
function despues(){
    var id = $(this).val();
    $.ajax({
        data:{'id_liga':id},
        url:'/perfil/busqueda/',
        type:'GET',
        success: function(data){
            var html = ""
            for (var i = 0; i < data.length ; i++){
                html += '<p>'+data[i].fields.equipos+' - '+data[i].fields.ligas1+'</p>'
               // html += '<p><b>'+data[i].fields.ligas+'</b></p>'
            }
            $('#equipos').html(html);
        }
    });
} 