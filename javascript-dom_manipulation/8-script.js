fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
.then(response => {
    return response.json();
})
.then(data => {
    let helloData = data.hello;
    let hello = document.querySelector('#hello');
    hello.textContent = helloData;
})
.catch(error =>  {
    console.error('Error:', error)
}); 
