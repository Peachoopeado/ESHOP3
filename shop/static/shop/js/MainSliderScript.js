var mainSlideWrapper = document.querySelector('.main_slider-wrapper');
var mainSlideWidth = mainSlideWrapper.offsetWidth / mainSlideWrapper.children.length;
var currentMainSlideIndex = 0;
var mainSlideInterval;

function goToMainSlide(index) {
  mainSlideWrapper.style.transform = `translateX(-${mainSlideWidth * index}px)`;
  currentMainSlideIndex = index;
}

function slideMainPrev() {
  if (currentMainSlideIndex > 0) {
    goToMainSlide(currentMainSlideIndex - 1);
  } else {
    goToMainSlide(mainSlideWrapper.children.length - 1);
  }
  clearInterval(saleSlideInterval);

  mainSlideInterval = setInterval(slideMainNext, 15000);
}

function slideMainNext() {
  if (currentMainSlideIndex < mainSlideWrapper.children.length - 1) {
    goToMainSlide(currentMainSlideIndex + 1);
  } else {
    goToMainSlide(0);
  }
  clearInterval(saleSlideInterval);

  mainSlideInterval = setInterval(slideMainNext, 15000);
}

var mainPrevButton = document.querySelector('.slider-prev');
var mainNextButton = document.querySelector('.slider-next');

mainPrevButton.addEventListener('click', slideMainPrev);
mainNextButton.addEventListener('click', slideMainNext);

setInterval(slideMainNext, 15000);