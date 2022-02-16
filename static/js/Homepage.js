const POP_UP1 = document.getElementById('Pieslēgšanās_logs');
const POP_UP2 = document.getElementById('Registresanas_logs');

document.getElementById('Pieslegšanās').addEventListener('click', () => {
    POP_UP1.style.display = 'block';
})
document.getElementById('PiesledzPoga').addEventListener('click', () => {
    POP_UP1.style.display = 'none'
})

document.getElementById('Regist').addEventListener('click', () => {
    POP_UP2.style.display = 'block';
})
document.getElementById('RegPoga').addEventListener('click', () => {
    POP_UP2.style.display = 'none'
})