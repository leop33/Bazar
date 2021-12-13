botones = document.querySelectorAll('button.toggle-button')
botones.forEach((boton) => {
    boton.onclick = () => {
        let div = document.querySelector('div.sidebar')
        if (div.classList.contains('show-custom')) {
            div.classList.remove('show-custom')
        } else {
            div.classList.add('show-custom')
        }
    }
})