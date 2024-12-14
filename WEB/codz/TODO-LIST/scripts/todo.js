var log = console.log;
// console.log(JSON.parse(localStorage.getItem('todos')), localStorage.getItem('todos'))

const todos =  JSON.parse(localStorage.getItem('todos')) || [{}] 

// const todos =  [
//     {
//         title: 'Play game',
//         dueDate: '13-8-2024',
//         status: {
//             isCheck: false
//         }
//     },
//     {
//         title: 'Play game',
//         dueDate: '13-8-2024',
//         status: {
//             isCheck: false
//         }
//     },
//     {
//         title: 'Watch Youtube',
//         dueDate: '9-8-2024',
//         status: {
//             isCheck: false
//         }
//     }
// ];
// saveTodoToLocalStorage(todos);

// load todos 
// document.addEventListener('DOMContentLoaded', loadTodos);

let todoContainer = document.querySelector('.js-todos-container');
loadTodos()
setDueDateValue()


function loadTodos() {
    let todoHTML = '';
    todos.forEach((todo, index) => {
        html = `
        <section class="todo js-todos" id="${index}">
            <section class='todo-name js-todo-name'>${todo.title}</section>
            <section class="js-todo-due-date">${todo.dueDate}</section>
            <input type="checkbox" class="todo-checkbox js-todo-checkbox js-todo-checkbox${index}" data-index="${index}">

            <div class="updating" id="updating-${index}">
                <input class="updating-todo-input  js-updating-todo-input" type="text" placeholder="Replace with">
                <input class="updating-todo-duedate js-updating-todo-duedate  updating-todo-duedate-${index}" type="date" id="updating-todo-duedate">
                <button class="save-changes js-save-changes">Save changes</button>
                <button class="cancel-updating js-cancel-updating">Cancel</button>
            </div>
        </section>
        `;
        todoHTML += html;
    });
    todoContainer.innerHTML = todoHTML;
    trackCompleteTask();
    addContextMenuOnTodo();
};

// make the add button interactive;
// add new todo to todos array 
document.querySelector('.js-add-button').addEventListener('click', addtodo);


// make the checkbox interactive 
function trackCompleteTask(){
    document.querySelectorAll('.js-todo-checkbox').forEach(checkbox => {
        checkbox.addEventListener('click', event => {
            const clickedTodoindex = checkbox.dataset.index;
            if (event.target.checked){
                const removingTodo = document.getElementById(clickedTodoindex);
                setTimeout(() => {
                    removingTodo.classList.add('slideOut');
                    setTimeout(() => {
                        todos.splice(clickedTodoindex, 1);
                        removingTodo.classList.remove('slideOut');
                        loadTodos();
                        saveTodoToLocalStorage(todos);
                    }, 501);
                }, 500);
            };
        });
    });
};

let activeTodo = null;
const contextMenuElement = document.querySelector('.js-right-click-menu');

function addContextMenuOnTodo() {
    document.querySelectorAll('.js-todos').forEach(todo => {
        todo.addEventListener('contextmenu', contextmenuEvent => {
            handleRightOnTodo(contextmenuEvent, todo);
        });
    });
};

document.addEventListener('click', (event) => {
    if (!contextMenuElement.contains(event.target)) {
        hideContextMenu();
        return null;
    };
});



function handleRightOnTodo(contextmenuEvent, todo) {
    contextmenuEvent.preventDefault();
 
    activeTodo = todo;

    contextMenuElement.style.display = 'block';
    contextMenuElement.style.top = contextmenuEvent.clientY + 'px';
    contextMenuElement.style.left =  contextmenuEvent.clientX + 'px';
    // the click eventListener on the contextmenuElement must not be defined here to prevent the addition of multiple eventListener each time the user right click on any todo, but be defined outside this scope(global).
};

// here is where the eventListener should be added 
contextMenuElement.addEventListener('click', event => {
    if (event.target.textContent == 'Update todo') {
        hideContextMenu();
        hideUpdatingTodo();
        updateTodo();
        trackCancelClick();
        trackSaveChangesClick();
    }else if (event.target.textContent == 'Delete'){
        // do something
        deleteTodo();
        hideContextMenu();
    };
});

function updateTodo() {
    const activeTodoUpdatingElem = document.getElementById(`updating-${activeTodo.id}`);
    
    activeTodoUpdatingElem.classList.add('updating--display-flex');
}



function hideContextMenu(){
    contextMenuElement.style.display = 'none';
}



function hideUpdatingTodo() {
    document.querySelectorAll('.updating').forEach(updatingContainer => {
        updatingContainer.classList.remove('updating--display-flex');
    });

    //  this function loops through all the todos and remove the 'updating--display-flex' class which allows the updating of any todo. That means if the todos are 300, it loops 300 times each time user selects 'update todo' from the todo ContextMenu.
};


function trackCancelClick() {
    const aciveTodoCancelBtnElem = activeTodo.querySelector('.js-cancel-updating');

    // remove previous eventListener because this function is called and eventListener is added in every successive call.
    aciveTodoCancelBtnElem.removeEventListener('click', hideUpdatingTodo);

    aciveTodoCancelBtnElem.addEventListener('click', () => {
        hideUpdatingTodo();
    });
};

function trackSaveChangesClick() {
    const aciveTodoSaveChangesBtnElem = activeTodo.querySelector('.js-save-changes');
    
    aciveTodoSaveChangesBtnElem.removeEventListener('click', saveUpdate);

    aciveTodoSaveChangesBtnElem.addEventListener('click', saveUpdate);
};

function saveUpdate() {
    hideUpdatingTodo();

    const newTodoName = activeTodo.querySelector('.js-updating-todo-input');
    const newTodoDueDate = activeTodo.querySelector('.js-updating-todo-duedate');
    // log({newTodoName, newTodoDueDate});
    if (!newTodoName.value.trim()) 
        return;
    
    // update the todos array;
    todos[activeTodo.id].title = newTodoName.value;
    todos[activeTodo.id].dueDate = newTodoDueDate.value.split('-').reverse().join('-');
    loadTodos();
    saveTodoToLocalStorage(todos);
};

function deleteTodo(){
    setTimeout(() => {
        activeTodo.classList.add('slideOut');
        setTimeout(() => {
            todos.splice(activeTodo.id, 1);
            activeTodo.classList.remove('slideOut');
            loadTodos();
            saveTodoToLocalStorage(todos);
        }, 501);
    }, 500);
};


function addtodo(event){
    // add new todo to the page.
    const todo = document.getElementById('todoname-input').value;
    const dueDate = document.getElementById('due-date-input').value.split('-').reverse().join('-');
    
    if (!todo){
        return showMsg('Please input a task to be completed.');
    } 
    todos.push({
        title: todo,
        dueDate: dueDate,
        status: {
            isCheck: false
        }
    });
    loadTodos();
    saveTodoToLocalStorage(todos);
    setDueDateValue();
};




function showMsg(msg) {
    const popupElem = document.getElementById('popup');

    popupElem.classList.add('popup--display-block');
    popupElem.querySelector('.msg-content').textContent = msg;   
    
    disableBodyUntilClickOkay(popupElem);
};


function disableBodyUntilClickOkay(popupElem){
    // change html body::before styleds to disallow any click aside the okay button 
    // that will be shown in the pup-up
    const htmlStyleTag = document.createElement('style');
    const textNode = document.createTextNode(`
        body::before{
            z-index: 1;
            background-color: hsl(180, 7%, 17%, 0.8);
            height: 100vh;
        }
        `);
    htmlStyleTag.appendChild(textNode);
    document.head.appendChild(htmlStyleTag);    
    enableBodyAfterClickOkay(popupElem, htmlStyleTag);
};

function enableBodyAfterClickOkay(popupElem, htmlStyleTag){
    // display none the msg pup-up if the okay btn is clicked and allow rest the body::before to allow click;
    popupElem.querySelector('.popup__ok').addEventListener('click', () => {
        try {
            document.head.removeChild(htmlStyleTag);
            popupElem.classList.remove('popup--display-block');
        } catch (error) {
            return;
        };
    });
};



function saveTodoToLocalStorage(todos){
    localStorage.setItem('todos', JSON.stringify(todos))
}

function setDueDateValue(isUpdatingTodo){
    const dueDateElem = document.getElementById('due-date-input');
    const allUpdatingDueDateElem = document.querySelectorAll('.updating-todo-duedate')
    
    const currentDate = new Date();
    
    // get date in yyyy mm dd
    currentDateArray = currentDate.toLocaleDateString().split('/');

    const month = currentDateArray[0];
    const day = currentDateArray[1];

    currentDateArray[0] = day < 10 ? '0' + day : day;
    currentDateArray[1] = month < 10 ? '0' + month : month;


    dueDateElem.value = currentDateArray.reverse().join('-');
    allUpdatingDueDateElem.forEach(dateElem => {
        dateElem.value = currentDateArray.join('-');
    });
    // log(currentDateArray)   
}

