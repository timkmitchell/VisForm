const menuBtn = document.querySelector('.menu-btn');
const menuPage = document.querySelector('.cont-page');

let menuOpen = false;

menuBtn.addEventListener('click', () => {
    if(!menuOpen) {
        menuBtn.classList.add('open');
        menuPage.classList.add('open');
        menuOpen = true;
    }else{
        menuBtn.classList.remove('open');
        menuPage.classList.remove('open');
        menuOpen = false;
    }
});