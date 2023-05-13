  document.querySelector('.mobile-menu-btn').addEventListener('click', function() {
    this.classList.toggle('active');
});
$('#burger-button').on('touchstart', function() {
  $('#navbarNav').toggle();
});
const body = document.querySelector('body')
const burgerButton = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

burgerButton.addEventListener('click', function() {
    body.classList.toggle('body--no-scroll');
    mobileMenu.classList.toggle('active');
});