function openTab(evt, tabName){
    // получаем все блоки контента и скрываем их
    let tabcontent = document.getElementsByClassName("tab-content");
    for (let i = 0; i < tabcontent.length; i++){
        tabcontent[i].style.display = 'none';
    }

    // получаем все кнопки вкладок и удаляем класс 'active'
    let tablinks = document.getElementsByClassName("tablinks");
    for (let i = 0; i < tablinks.length; i++){
        tablinks[i].classList.remove("active");
    }

    // Отображаем выбранный блок контента и добавляем класс "active" к кнопке вкладки
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.classList.add("active");
}

// По умолчанию открываем вкладку "Избранное"
// По умолчанию скрываем все блоки контента и удаляем класс 'active' у всех кнопок вкладок
let tabcontent = document.getElementsByClassName("tab-content");
for (let i = 0; i < tabcontent.length; i++){
    tabcontent[i].style.display = 'none';
}

let tablinks = document.getElementsByClassName("tablinks");
for (let i = 0; i < tablinks.length; i++){
    tablinks[i].classList.remove("active");
}

// Отображаем блок контента "Профиль" и добавляем класс "active" к кнопке вкладки "Профиль"
document.getElementById("profile").style.display = "block";
document.getElementsByClassName("tablinks")[2].classList.add("active");

window.addEventListener('DOMContentLoaded', (event) => {
  const tablinks = document.getElementsByClassName('tablinks');

  // Найти кнопку вкладки "Избранное" по тексту
  let favoritesTabButton;
  for (let i = 0; i < tablinks.length; i++) {
    if (tablinks[i].textContent === 'Избранное') {
      favoritesTabButton = tablinks[i];
      break;
    }
  }

  // Если кнопка найдена, добавить класс "active" и вызвать функцию openTab
  if (favoritesTabButton) {
    favoritesTabButton.classList.add('active');
    openTab(null, 'favorites');
  }
});
