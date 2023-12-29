alert('Welcome To CutieBakery')

const d = new Date();
document.getElementById("waktu").innerHTML
= d.toDateString();

const navbarNav = document.querySelector('.navbar-nav');
document.querySelector('#hamburger-menu').onclick = () => {
    navbarNav.classList.toggle('active');
};


const hamburger = document.querySelector('#hamburger-menu');

document.addEventListener('click', function (e) {
    if (!hamburger.contains(e.target) && !navbarNav.contains(e.target)) {
        navbarNav.classList.remove('active');
    }
});

$(document).ready(function(){
    let h1 = $('h1')
    h1.html("WELCOME")
    h1.before('<i><h3>Bakery Dari Hati</h3></i>')
    h1.after('<h2>Cari Roti? CutieBakery Aja!!!</h2>')
    h1.css('color','#f0e7c0')
})

$(document).ready(function(){
    let button = $('button')
    let h2 = $('h2')

    button.on('click', function() {
        h2.toggle(2000)
    })
})