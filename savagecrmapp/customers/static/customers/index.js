$(document).ready(function(){
    console.log('Jquery is working');
    $('#search').keyup(function(){
        if($('#search').val()){
            let search =$('#search').val();
            $.ajax({
                url: 'consulta/',
                type: 'POST',
                dataType: 'json',
                data: {
                search:search,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function(response){
                    let jsonfile = response;
                    console.log(jsonfile);
            }
        })
        console.log(search);
        }
    })
});