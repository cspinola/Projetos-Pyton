document.body.addEventListener('keyup', pegaTrecla)

function pegaTrecla(event) {
    //tocaSom(event.composed.tolowercase)
    let codeMinusculo = event.code.toLowerCase();
    tocaSom(codeMinusculo);//toLowerCaSE PARA DEIXAR O CODIGO DA TECLA MINUSCULA;
}

function tocaSom(som) {
    let audioSelecionado = document.querySelector(`#som_${som}`)

    if (audioSelecionado) {
        //audioSelecionado.currentTime = 0;
        audioSelecionado.play();
    }

    let letraSelecionada = document.querySelector(`#tecla_${som}`)

    if (letraSelecionada) {
        letraSelecionada.classList.add('ativa');

        setTimeout(() => {
            letraSelecionada.classList.remove('ativa');
        }, 300) // 300 milissegundos
    }

}


