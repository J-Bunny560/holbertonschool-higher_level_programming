let toggleHeader = document.querySelector('#toggle_header');

toggleHeader.addEventListener('click', function() {
    if (toggleHeader.classList.contains('red')) {
        toggleHeader.classList.remove('red');
        toggleHeader.classList.add('green');
    }
    else if (toggleHeader.classList.contains('green')) {
        toggleHeader.classList.remove('green');
        toggleHeader.classList.add('red');
    }
    else {
        toggleHeader.classList.add('red');
    }
});
