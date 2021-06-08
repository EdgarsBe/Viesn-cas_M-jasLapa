const POP_UP3 = document.getElementById('rezervacijasRedigesana')
const POP_UP4 = document.getElementById('statistikasEksportesana')

document.querySelectorAll('#redigesanasIkona').forEach(item => {
    item.addEventListener('click', event => {
        POP_UP3.style.display = 'block'
    })
  })

document.getElementById('datumaRedigesanaButton').addEventListener('click', () => {
    POP_UP3.style.display = 'none'
})

document.getElementById('eksportetStatistika').addEventListener('click', () => {
    POP_UP4.style.display = 'block'
})

document.getElementById('atceltStatistika').addEventListener('click', () => {
    POP_UP4.style.display = 'none'
})