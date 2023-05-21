var slidesWrapper = document.querySelector('.main_slider-wrapper');
    var slideWidth = slidesWrapper.offsetWidth / slidesWrapper.children.length;
    var currentSlideIndex = 0;

    function goToSlide(index) {
        slidesWrapper.style.transform = `translateX(-${slideWidth * index}px)`;
        currentSlideIndex = index;
    }

    function slidePrev() {
        if (currentSlideIndex > 0) {
            goToSlide(currentSlideIndex - 1);
        } else {
            goToSlide(slidesWrapper.children.length - 1);
        }
    }

    function slideNext() {
        if (currentSlideIndex < slidesWrapper.children.length - 1) {
            goToSlide(currentSlideIndex + 1);
        } else {
            goToSlide(0);
        }
    }

    var prevButton = document.querySelector('.slider-prev');
    var nextButton = document.querySelector('.slider-next');

    prevButton.addEventListener('click', slidePrev);
    nextButton.addEventListener('click', slideNext);

    setInterval(slideNext, 7000);