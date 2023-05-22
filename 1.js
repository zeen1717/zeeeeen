// select a list
const ul = document.querySelector('ul');
const input = document.getElementById('item');
// load existing item from local storage ,but creating an array if it does not exist.
let itemsArray = localStorage.getItem('items') ?
JSON.parse(localStorage.getItem('items')) : [];
itemsArray.forEach(addTask);
function addTask(text){
  const li = document.createElement('li')
  li.textContent = text;
  ul.appendChild(li);
}
// assign funciton to login button
function add(){
  itemsArray.push(input.value);
  localStorage.setItem('items', JSON.stringify(itemsArray));
  addTask(input.value);
  input.value = '';
}
//assgin function to sighout button
function del(){
  localStorage.clear();
  ul.innerHTML = '';
  itemsArray = [];
}

