let url = 'http://localhost:3002/api/';

console.log(11111111);

fetch(`${url}cursos`)
    .then(response => response.json())
    .then((data) => {
        console.log(data);
    })

console.log(222222);