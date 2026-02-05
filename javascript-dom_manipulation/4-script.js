const addItem = document.querySelector('#add_item');
const ul = document.querySelector('.my_list');

addItem.addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});
