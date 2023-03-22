const initialsInput = document.querySelectorAll('input[data-no-numbers]');
for (let i = 0; i < initialsInput.length; i++) {
    initialsInput[i].addEventListener('input', () =>{
        const value = initialsInput[i].value;
        const newValue = value.replace(/[0-9]/g, '');
        if (newValue !== value) {
            initialsInput[i].value = newValue; // если значение изменилось, обновляем поле ввода
        }
    });
}
const phoneInput = document.getElementById('user_phone_input');
$('#user_phone_input').mask('+7 (999) 999-99-99');
phoneInput.addEventListener('input', () =>{

    phoneInput.value = phoneInput.value.replace(/[^\d-()+]/g, "");

});

