const POP_UP1 = document.getElementById('Pop_up1');
const POP_UP2 = document.getElementById('Pop_up2');

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