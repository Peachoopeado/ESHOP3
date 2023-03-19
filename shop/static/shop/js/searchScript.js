const searchButton = document.getElementById('search-button');
        const searchInput = document.getElementById('search-input');
        const cart = document.getElementById('cart-button');
        searchButton.addEventListener('click', function () {
            searchInput.style.display = 'block';
            cart.style.display = 'none';
            searchInput.focus();
        });
        searchButton.addEventListener('touchstart', function () {
            searchInput.style.display = 'block';
            cart.style.display = 'none';
            searchInput.focus();
        });