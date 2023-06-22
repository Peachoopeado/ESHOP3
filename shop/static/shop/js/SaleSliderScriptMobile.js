document.addEventListener('DOMContentLoaded', function () {
    var saleMobileSlideWrapper = document.querySelector('.sale_slider_wrapper_mobile');
    var saleMobileSlideWidth = saleMobileSlideWrapper.offsetWidth / saleMobileSlideWrapper.children.length;
    var currentSaleMobileSlideIndex = 0;
    var saleMobileSliderInterval = null;


    function goToSaleSlideMobile(index) {
        saleMobileSlideWrapper.style.transform = `translateX(-${saleMobileSlideWidth * index}px)`;
        currentSaleMobileSlideIndex = index;
    }

    function slideSalePrevMobile() {
        if (currentSaleMobileSlideIndex > 0) {
            goToSaleSlideMobile(currentSaleMobileSlideIndex - 1);
        } else {
            goToSaleSlideMobile(saleMobileSlideWrapper.children.length - 1);
        }
        clearInterval(saleMobileSliderInterval);
        saleMobileSliderInterval = setInterval(slideSaleMobileNext, 15000); // Установить интервал снова
    }

    function slideSaleMobileNext() {
        if (currentSaleMobileSlideIndex < saleMobileSlideWrapper.children.length - 1) {
            goToSaleSlideMobile(currentSaleMobileSlideIndex + 1);
        } else {
            goToSaleSlideMobile(0);
        }
        clearInterval(saleMobileSliderInterval);
        saleMobileSliderInterval = setInterval(slideSaleMobileNext, 15000); // Установить интервал снова
    }

    var saleMobilePrevButton = document.querySelector('.sale-slider-prev-mobile');
    var saleMobileNextButton = document.querySelector('.sale-slider-next-mobile');

    saleMobilePrevButton.addEventListener('click', slideSalePrevMobile);
    saleMobileNextButton.addEventListener('click', slideSaleMobileNext);

    setInterval(slideSaleMobileNext, 15000);
});
