const iconWrap = document.getElementById('iconWrap');
const iconOpen = document.getElementById('iconOpen');
const iconClose = document.getElementById('iconClose');
const mainMenu = document.getElementById('mainMenu');
const hi_block = document.getElementById('hi_block');
const head = document.getElementById('head');
const up = document.getElementById('up');
var homeLink = document.querySelector('a[href="#text"]');
var aboutLink = document.querySelector('a[href="#a_text"]');
var portfolioLink = document.querySelector('a[href="#p_text"]');
var contactLink = document.querySelector('a[href="#g_text"]');

iconWrap.addEventListener('click', () => {
    mainMenu.classList.toggle('hide-menu');
    iconOpen.classList.toggle('hide');
    iconClose.classList.toggle('hide');
    hi_block.classList.toggle('hide');
	head.classList.toggle('content-height')
});

homeLink.addEventListener('click', function (event) {
    event.preventDefault();
    var targetElement = document.querySelector('#text');
    var targetPosition = targetElement.getBoundingClientRect().top;
    window.scrollTo({
        top: targetPosition - 200,
        behavior: 'smooth'
    });
});
aboutLink.addEventListener('click', function (event) {
    event.preventDefault();
    var targetElement = document.querySelector('#a_text');
    var targetPosition = targetElement.getBoundingClientRect().top;
    window.scrollTo({
        top: targetPosition - 200,
        behavior: 'smooth'
    });
});
portfolioLink.addEventListener('click', function (event) {
    event.preventDefault();
    var targetElement = document.querySelector('#p_name');
    var targetPosition = targetElement.getBoundingClientRect().top;
    window.scrollTo({
        top: targetPosition - 300,
        behavior: 'smooth'
    });
});
contactLink.addEventListener('click', function (event) {
    event.preventDefault();
    var pageHeight = document.body.scrollHeight - window.innerHeight;
    window.scrollTo({
        top: pageHeight,
        behavior: 'smooth'
    });
})
up.addEventListener('click', function (event) {
    event.preventDefault();
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});
