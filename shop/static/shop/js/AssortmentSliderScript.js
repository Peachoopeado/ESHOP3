var assortmentSlideWrapper = document.querySelector('.main_assortment_slider_wrapper');
var assortmentSlideWidth = assortmentSlideWrapper.offsetWidth / assortmentSlideWrapper.children.length;
var currentAssortmentSlideIndex = 0;
var assortmentSlideInterval;

function startSlideInterval(){
  clearInterval(assortmentSlideInterval);
  assortmentSlideInterval = setInterval(autoAssortmentSlide, 7000);
}

function goToAssortmentSlide(index) {
  assortmentSlideWrapper.style.transform = `translateX(-${assortmentSlideWidth * index}px)`;
  currentAssortmentSlideIndex = index;
}

function setActiveIndicator(index) {
  var indicators = document.querySelectorAll('.indicator');
  indicators.forEach(function (indicator) {
    indicator.classList.remove('active');
  });
  indicators[index].classList.add('active');
}

function slideToAssortmentIndex(index) {
  goToAssortmentSlide(index);
  setActiveIndicator(index);
  startSlideInterval();
}

function autoAssortmentSlide() {
  var totalAssortmentSlides = assortmentSlideWrapper.children.length;
  var nextAssortmentSlideIndex = (currentAssortmentSlideIndex + 1) % totalAssortmentSlides;
  slideToAssortmentIndex(nextAssortmentSlideIndex);

}

var indicators = document.querySelectorAll('.indicator');
indicators.forEach(function (indicator, index) {
  indicator.addEventListener('click', function () {
    slideToAssortmentIndex(index);
    
  });
});

// Инициализация: установка активного индикатора на первый слайд
slideToAssortmentIndex(currentAssortmentSlideIndex);