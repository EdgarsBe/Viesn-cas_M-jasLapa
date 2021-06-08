const POP_UP1 = document.getElementById('Pop_up1');
const POP_UP2 = document.getElementById('Pop_up2');
const POP_UP3 = document.getElementById('rezervacijasRedigesana')
const POP_UP4 = document.getElementById('statistikasEksportesana')

document.getElementById('button2').addEventListener('click', () => {
    POP_UP1.style.display = 'block';
})
document.getElementById('IeietPoga').addEventListener('click', () => {
    POP_UP1.style.display = 'none'
})
document.getElementById('ReģPoga1').addEventListener('click', () => {
    POP_UP1.style.display = 'none'
})

document.getElementById('button3').addEventListener('click', () => {
    POP_UP2.style.display = 'block';
})
document.getElementById('ReģPoga2').addEventListener('click', () => {
    POP_UP2.style.display = 'none'
})

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