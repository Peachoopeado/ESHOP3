const quantitySelect = document.getElementById('quantity-select');
const priceIndicator = document.getElementById('price-indicator');
const price = parseFloat(priceIndicator.textContent.split(':')[1]);

quantitySelect.addEventListener('change', (event)=>{
    const selectedQuantity = parseInt(event.target.value);
    const totalPrice = price * selectedQuantity;
    priceIndicator.textContent = `Цена: ${totalPrice.toFixed(2)} руб.`;
});