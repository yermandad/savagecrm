$(document).ready(function(){

    console.log('Jquery is working');
    $('#search').keyup(function(){

        if($('#search').val()){
            let search =$('#search').val();
            $('#tCustomer').show();
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
                    let data =$(jsonfile.cliente);
                    let template=``;
                    $.each(data,function(i,client){
                        template += `<tr>
                            <td>${client.c_name}</td>
                            <td>${client.c_lastname}</td>
                            <td>${client.c_phone}</td>
                            <td>
                                <div class="form-group d-flex">
                                <a class="btn btn-outline-info my2 my-sm-0" href="${client.id}/detail" value="Revisar"id="btnDetail"> Revisar </a>
                                | 
                                <a class="btn btn-outline-primary my2 my-sm-0" href="${client.id}/schedule" value="Agendar"id="btnSchedule"> Agendar </a>
                                </div>
                            </td>
                        </tr>`;
                    })
                    $('#tCustomer').html(template);
                } 
            })
        } else{
            $('#tCustomer').hide();
        }})
    console.log(search);
    })


    $(document).ready(function(){
    $('#btnRegister').click(function(){
        console.log('Jquery2 is working');
        if($('#c_name').val()){
            console.log($('#c_name'));
            let c_name =$('#c_name').val();
            let c_lastname= $('#c_lastname').val();
            let c_phone= $('#c_phone').val();
            const send= {c_name:c_name, c_lastname:c_lastname, c_phone:c_phone };
            $.ajax({
                url: 'register/',
                type: 'POST',
                data: {
                    send: send,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function(response){
                    let message= response;
                    $('#messageR').html(message);
                }
            })

        } else{
            console.log('No hay cliente para registrar');
        }


    })
    })
