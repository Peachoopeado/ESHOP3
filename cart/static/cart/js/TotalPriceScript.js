function updateTotalPrice(){
    var deliveryRadioButtons = document.getElementsByName('delivery');
    var selectedDeliveryPrice = 0;

    for (var i = 0; i < deliveryRadioButtons.length; i++){
        if (deliveryRadioButtons[i].checked){
            selectedDeliveryPrice = parseFloat(deliveryRadioButtons[i].value);
            console.log(selectedDeliveryPrice);
            break;
        }
    }
    console.log('{{ cart.get_total_price}}');
    var totalPrice = parseFloat(document.getElementById('total-price').getAttribute('data-total-price'));
    console.log(totalPrice)
    var totalWithDelivery = (totalPrice + selectedDeliveryPrice).toFixed(2);
    document.getElementById('total-price').innerHTML = totalWithDelivery
}
var deliveryRadioButtons = document.getElementsByName('delivery');
for (var i = 0; i < deliveryRadioButtons.length; i++){
    deliveryRadioButtons[i].addEventListener('change', updateTotalPrice);
}
updateTotalPrice();
