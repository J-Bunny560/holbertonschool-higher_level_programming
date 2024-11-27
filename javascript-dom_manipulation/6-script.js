fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(response => {
    return response.json();
})
.then(data => {
    let characterName = data.name;
    let characterElement = document.querySelector('#character');
    characterElement.textContent = characterName;
})
.catch(error => {
    console.error('Error', error);
});
