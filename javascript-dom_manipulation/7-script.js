fetch('https://swapi-api.hbtn.io/api/films/?')
.then(response => {
    return response.json();
})
.then(data => {
    let filmNames = data.results;
    filmNames.forEach(film => {
        let title = film.title;
        let listItem = document.createElement('li');
        listItem.textContent = title;
        let listMovies = document.querySelector('#list_movies');
        listMovies.appendChild(listItem);
    });
})
.catch(error => {
    console.error('Error', error);
});