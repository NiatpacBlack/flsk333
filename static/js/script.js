/* Создаем массив в который в дальнейшем будем складывать данные о всех полях из бд. */
let inputsData = [];

function createInput(name) {
    /* Функция, которая создает поле input в html коде. */

    const input = document.createElement('input');

    input.type = 'text';
    input.name = name;
    input.classList.add('form-control', 'my-1');

    $('#inputsContainer').append(input);
}

$(document).ready(async function () {
    /* При загрузке верстки получаем данные из бд и создаем столько input полей, сколько есть в базе. */

    const response = await fetch('/api/v1/input');

    inputsData = await response.json();
    inputsData.forEach(inputData => createInput(inputData.data));
});

$('#addBtn').click(async function () {
    /* При нажатии на кнопку добавляем новое поле в базу данных и input в html шаблон. */

    let name = "name1";

    if (inputsData.length >= 1) {
        name = "name" + (inputsData.length + 1);
    }

    await fetch('/api/v1/input', {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({"data": name}),
    });

    createInput(name);
    inputsData.push({"data": name});
});
