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