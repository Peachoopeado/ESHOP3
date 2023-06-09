document.addEventListener('DOMContentLoaded', function () {
    var saleSlideWrapper = document.querySelector('.sale_slider-wrapper');
    var saleSlideWidth = saleSlideWrapper.offsetWidth / saleSlideWrapper.children.length;
    var currentSaleSlideIndex = 0;

    function goToSaleSlide(index) {
        saleSlideWrapper.style.transform = `translateX(-${saleSlideWidth * index}px)`;
        currentSaleSlideIndex = index;
    }

    function slideSalePrev() {
        if (currentSaleSlideIndex > 0) {
            goToSaleSlide(currentSaleSlideIndex - 1);
        } else {
            goToSaleSlide(saleSlideWrapper.children.length - 1);
        }
        clearInterval(saleSlideInterval);
        saleSlideInterval = setInterval(slideSaleNext, 15000); // Установить интервал снова
    }

    function slideSaleNext() {
        if (currentSaleSlideIndex < saleSlideWrapper.children.length - 1) {
            goToSaleSlide(currentSaleSlideIndex + 1);
        } else {
            goToSaleSlide(0);
        }
        clearInterval(saleSlideInterval);
        saleSlideInterval = setInterval(slideSaleNext, 15000); // Установить интервал снова
    }

    var salePrevButton = document.querySelector('.sale-slider-prev');
    var saleNextButton = document.querySelector('.sale-slider-next');

    salePrevButton.addEventListener('click', slideSalePrev);
    saleNextButton.addEventListener('click', slideSaleNext);

    setInterval(slideSaleNext, 15000);
});
