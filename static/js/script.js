const addBtn = document.getElementById('addBtn');
const inputsContainer = document.getElementById('inputsContainer');

let inputsData = [];

function createInput(name, id) {
    const input = document.createElement('input');
    input.type = 'text';
    input.name = name;
    input.id = id;
    input.classList.add('form-control', 'my-1');
    inputsContainer.append(input);
}

async function getInputs() {
    const response = await fetch('/api/v1/input');
    const data = await response.json();
    inputsData = data;
    inputsContainer.innerHTML = '';
    inputsData.forEach(inputData => createInput(inputData.data, inputData.id));
    addBtn.disabled = false;
}

async function addInput() {
    addBtn.disabled = true;
    const response = await fetch('/api/v1/input', {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({"data": "name" + (inputsData.length + 1)}),
    });
    getInputs();
}

addBtn.addEventListener('click', addInput);
document.addEventListener('DOMContentLoaded', getInputs);