let addItem = document.querySelector('#add_item');

addItem.addEventListener('click', function() {
    let newListItem = document.createElement('li');
    newListItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newListItem);
});