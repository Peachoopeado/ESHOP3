const links = document.querySelectorAll('.filter_block li a');

links.forEach(link => {
    link.addEventListener('click', function(event){

        links.forEach(l => l.classList.remove('selected'));

    link.classList.add('selected');
    });

});
