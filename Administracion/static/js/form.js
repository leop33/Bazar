rows = document.querySelectorAll('tbody>tr')
add = document.getElementById('add')
upd = document.getElementById('upd')
del = document.getElementById('del')

rows.forEach((element) => {
    element.onclick = () => {
        let actives = document.querySelectorAll('tbody>tr.active')
        if (element.classList.contains('active')) {
            actives.forEach((active) => {
                active.classList.remove('active')
            })
        } else {
            actives.forEach((active) => {
                active.classList.remove('active')
            })
            element.classList.add('active')
        }
        active_buttons()
    }
})

function active_buttons() {
    let actives = document.querySelectorAll('tbody>tr.active')
    if (actives.length > 0) {
        upd.disabled = false
        del.disabled = false
    } else {
        upd.disabled = true
        del.disabled = true
    }
}

upd.onclick = () => {
    let url_ = add.children[0].getAttribute('href')
    let active = document.querySelector('tbody>tr.active')
    upd.children[0].setAttribute("href", url_+"update/" + active.getAttribute('row-id'))
}

del.onclick = () => {
    let url_ = add.children[0].getAttribute('href')
    let active = document.querySelector('tbody>tr.active')
    del.children[0].setAttribute("href", url_+"delete/" + active.getAttribute('row-id'))
}