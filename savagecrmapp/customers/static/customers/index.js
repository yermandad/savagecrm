$(document).ready(function(){
    console.log('Jquery is working');
    $('#search').keyup(function(){
        if($('#search').val()){
            let search =$('#search').val();
            $.ajax({
                url: 'consulta/',
                type: 'POST',
                data: {
                search:search,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken').val(),
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

/* const listaClientes=async()=>{
    try{
        const response = await fetch("./consulta");
        const data = await response.json();

        if(data.message=="Success"){
            let options=``;
            data.cliente.forEach((client) => {
                cName.innerHTML = `<option>${client.c_name}</option>`;
                lName.innerHTML = `<option>${client.c_lastname}</option>`;
                phone.innerHTML = `<option>${client.c_phone}</option>`;
                action.innerHTML = `<option href="{% url 'customers:detail' ${client.id}%}">Revisar | </option><option href="{% url 'customers:schedule' ${client.id}%}">Agendar</option>`;
            });
        }else{
            alert("cliente no encontrado ...")
        }
        console.log(data);
    }catch(error){
        console.log(error);
    }
};

const cargaInicial=async()=>{
    await listaClientes();
};

window.addEventListener("keyup", async () => {
    await cargaInicial();
}); */