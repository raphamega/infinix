$("#id_cep").blur(function() {
    // Remove tudo o que não é número para fazer a pesquisa
    var cep = this.value.replace(/[^0-9]/, "");

    // Validação do CEP; caso o CEP não possua 8 números, então cancela
    // a consulta
    if (cep.length != 8) {
        return false;
    }

    // A url de pesquisa consiste no endereço do webservice + o cep que
    // o usuário informou + o tipo de retorno desejado (entre "json",
    // "jsonp", "xml", "piped" ou "querty")
    var url = "https://viacep.com.br/ws/" + cep + "/json/";

    // Faz a pesquisa do CEP, tratando o retorno com try/catch para que
    // caso ocorra algum erro (o cep pode não existir, por exemplo) a
    // usabilidade não seja afetada, assim o usuário pode continuar//
    // preenchendo os campos normalmente
    $.getJSON(url, function(dadosRetorno) {
        try {
            // Preenche os campos de acordo com o retorno da pesquisa
            $("#id_endereco").val(dadosRetorno.logradouro);
            $("#id_bairro").val(dadosRetorno.bairro);
            $("#id_municipio").val(dadosRetorno.localidade);
            $("#id_UF").val(dadosRetorno.uf);

        } catch (ex) {}
    });
});

$('#id_cnpj').remove('required')

$(function() {
    $('#id_image').change(function() {
        const file = $(this)[0].files[0];
        const fileReader = new FileReader();
        fileReader.onloadend = function() {
            $('#id_img').attr('src', fileReader.result)
        }
        fileReader.readAsDataURL(file)
    });
});

var piscando = document.getElementById('id_do_elemento');
var interval = window.setInterval(function() {
    if (piscando.style.visibility == 'hidden') {
        piscando.style.visibility = 'visible';
    } else {
        piscando.style.visibility = 'hidden';
    }
}, 5000);

function marcaDesmarca(caller) {
    var checks = document.querySelectorAll('input[type="checkbox"]');
    for (let i = 0; i < checks.length; i++) {
        checks[i].checked = checks[i] == caller;
    }
}