const iconWrap = document.getElementById('iconWrap')
const iconOpen = document.getElementById('iconOpen')
const iconClose = document.getElementById('iconClose')
const mainMenu = document.getElementById('mainMenu')
const blurElement = document.getElementById('blur-element')
const scrollButtons = document.querySelectorAll('.menu-button');


iconWrap.addEventListener('click',() => {
	mainMenu.classList.toggle('hide-menu')
	iconOpen.classList.toggle('hide')
	iconClose.classList.toggle('hide')
	blurElement.classList.toggle("blur");
	toggleScrollLock();
})

function toggleScrollLock() {
	const body = document.querySelector('body');
	body.style.overflow = body.style.overflow === 'hidden' ? 'auto' : 'hidden';
	window.scrollTo(0, 0);
}

scrollButtons.forEach(button => {
  button.addEventListener('click',() => {
    const body = document.querySelector('body');
	body.style.overflow = 'auto';
	mainMenu.classList.toggle('hide-menu')
	iconOpen.classList.toggle('hide')
	iconClose.classList.toggle('hide')
	blurElement.classList.toggle("blur");
  });
});
