import { removeCssClassFromArrayOfElem } from './general.js';





const headerElement = document.getElementById('js-header');

let flag = 0;
const headerButton = headerElement.querySelector('.js-header__button');
const menuIcon = headerElement.querySelector('.header__menu-icon');
const headerNav =  document.querySelector('.js-header__nav');
const headerButtonHandler = {
    // when the button is clicked
    buttonClicked: headerElement.querySelector('.js-header__button').addEventListener('click', () => {
        flag++;
        if (flag === 2){
            removeCssClassFromArrayOfElem([headerButton, menuIcon], "active");
            headerNav.classList.remove('active')
            headerNav.classList.remove('display-block');
            flag = 0;
        } else {
            [headerButton, menuIcon].forEach(button  => {
                button.classList.add('active')
            });
            headerNav.classList.add('display-block');
        };
    }),

    // add event listener to all the li(s) to display the nav bar none when clicked
    linkClicked: document.querySelectorAll('.js-li').forEach(li => {
        li.addEventListener('click', () => {
            headerNav.classList.remove('active');
            headerNav.classList.remove('display-block');
            removeCssClassFromArrayOfElem([headerButton, menuIcon], "active");
            flag = 0;
        });
    })
};

// let activeLink;
// headerElement.querySelectorAll('.header-link').forEach(currentLink => {
//     currentLink.addEventListener('click', () => {indicateActiveSection(currentLink)})
// })

// function indicateActiveSection(currentLink) {
//     headerElement.querySelectorAll('.header-link').forEach(l => {
//         l.classList.remove('inview'); 
//     });
//     currentLink.classList.add('inview');
    
// }

