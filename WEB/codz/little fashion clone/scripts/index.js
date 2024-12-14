import { removeCssClassFromArrayOfElem } from "./general.js";

var log = console.log;

const autoUpdateHeroMilliseconds = 10000;

const heroImgs = [
    "./images/slideshow/medium-shot-business-women-high-five.jpeg", 
    "./images/slideshow/team-meeting-renewable-energy-project.jpeg", 
    "./images/slideshow/two-business-partners-working-together-office-computer.jpeg"
];

const heroText = [
    {
        h1: "Cool Fashion",
        p: "Little fashion template comes with total 8 HTML pages provided by Tooplate website."
    },
    {
        h1: "New Design",
        p: "Please share this Little Fashion template to your friends. Thank you for supporting us."
    }, 
    {
        h1: "Talk To Us", 
        p: "Tooplate is one of the best HTML CSS template websites for everyone."
    }
];

const aboutSectionData = [
    {
        id: "1",
        title: "instruction", 
        img: "./images/pim-chu-z6NZ76_UTDI-unsplash.jpeg",
        h3: "Good <span> Design</span> Ideas for <span> your </span>fashion",
        discription: {
            p1: "Little Fashion templates comes with sign in / sign up pages, product listing / product detail, about, FAQs, and contact page.",
            p2: "Since this HTML template is based on Boostrap 5 CSS library, you can feel free to add more components as you need.",
        }, 
        a: {
            action: 'LEARN MORE ABOUT US',
            href: ''
        }
    }, 

    {
        id: "1",
        title: "how we work?",
        img: "./images/retail-shop-owner-mask-social-distancing-shopping.jpg",
        h3: "Life at Studio",
        discription: {
            p1: "Over three years in business, We’ve had the chance to work on a variety of projects, with companies",
            p2: "Custom work is branding, web design, UI/UX design",
        }, 
        a: {
            action: 'WORK WITH US',
            href: ''
        }
    },

    {
        id: "0",
        title: "capabilities",
        img: "./images/cody-lannom-G95AReIh_Ko-unsplash.jpeg",
        h3: "What can help you?",
        discription: {
            p1: "Over three years in business, We’ve had the chance on projects",
            p2: ''
        }, 
        a: {
            action: 'EXPLORE PRODUCTS',
            href: 'product.html'
        }
    }
]

// let isClickIndicator = false;
const heroElement = document.getElementById('js-hero');

autoUpdateHero(); 


document.querySelectorAll('.js-hero-indicator-button').forEach(button => {
    button.addEventListener('click', () => {
        const clickedIndicatorId = Number(button.getAttribute('id'));
        unselectAllIndicators();
        SelectIndicatorOf(clickedIndicatorId);
        changeHeroBackgroundImage(clickedIndicatorId);
        changeHeroText(clickedIndicatorId);
        addAnimation('js-hero__overlay-animation', 'addfadeBg-animation');
    });
});

// about section eventListener
const allAboutNavPrimaryLinkElem = document.querySelectorAll('.js-about-nav-primary-link')

allAboutNavPrimaryLinkElem.forEach(navList => {
    navList.addEventListener('click', () => {
        // indicate the clicked nav elem
        removeCssClassFromArrayOfElem(allAboutNavPrimaryLinkElem, 'active');
        navList.classList.add('active');

        // update the page relevant to the elem clicked in the nav
        updateAboutSection(navList);
    });
});

function updateAboutSection(navList) {
    const clickLink = navList.textContent.toLocaleLowerCase()
    aboutSectionData.forEach(data => {
        
        // console.log(data.title, clickLink)
        if (clickLink == data.title) {
            document.querySelector('.js-about__container-middle').innerHTML = `
                <section class="about__container-middle">
                    <figure>
                        <img width="400" src="${data.img}" alt="">
                    </figure>
                </section>
            `;
            document.querySelector('.js-about__container-right').innerHTML = `
                <section class="about__container-right js-about__container-right">
                    <h3>${data.h3}</h3>
            
                    <section>
                        <p>${data.discription.p1}</p>
                        <p>${data.discription.p2}</p>
                        <div class="about__progress js-about__progress">
                            <div class="progress-cont">
                                <strong>Branding</strong>
                                <span class="float-end">90%</span>
                                <div class="pb progressing-bar1"></div>
                            </div>
                            <div class="progress-cont">
                                <strong>Design & Stragety</strong>
                                <span class="float-end">70%</span>
                                <div class="pb progressing-bar2"></div>
                            </div>
                            <div class="progress-cont">
                                <strong>Online Platform</strong>
                                <span class="float-end">80%</span>
                                <div class="pb progressing-bar3"></div>
                            </div>
                        </div>
                        <a href="${data.a.href}">${data.a.action} &rightarrow;</a>
                    </section>
                </section>
            `;
            // log(document.querySelector('.js-about__container-right'));
            showProgress(data);
        };
    });
}

function showProgress(data) {
    const progress = document.querySelector('.js-about__progress');
    if (data.id == '0') {
        progress.style.display = 'block';
    };
}



function autoUpdateHero(){
    let indicatorId = 0;

   setInterval(() => {
        SelectIndicatorOf(indicatorId);
        changeHeroBackgroundImage(String(indicatorId));
        changeHeroText(indicatorId);
        addAnimation('js-hero__overlay-animation', 'addfadeBg-animation');

        indicatorId++;
        if (indicatorId === 3){
            indicatorId = 0;
        }
    }, autoUpdateHeroMilliseconds);
};

function SelectIndicatorOf(indicatorId) {
    let selectedIndicatorElem = document.getElementById(`${indicatorId}`);
    unselectAllIndicators()
    selectedIndicatorElem.style.backgroundColor = 'white'
    selectedIndicatorElem.style.borderColor = "rgba(255, 255, 255, 0.407)";  // in relation with the css's own; js-indicator-button;
}

function unselectAllIndicators() {
    document.querySelectorAll('.js-hero-indicator-button').forEach((indicator) => {
        indicator.style.backgroundColor = 'transparent';
    });
}

function changeHeroBackgroundImage(clickedIndicatorId){
    heroElement.style.backgroundImage = `url("${heroImgs[clickedIndicatorId]}")`;
}

function changeHeroText(clickedIndicatorId) {
    const heroh1Element = heroElement.querySelector('.js-hero__h1');
    const heropElement = heroElement.querySelector('.js-hero__p');

    heroh1Element.textContent = `${heroText[clickedIndicatorId].h1}`;
    heropElement.textContent = `${heroText[clickedIndicatorId].p}`;
};

let timeoutId;
function addAnimation(elementClassName, animationClassName, removeAfter=500) {
    const elem = document.querySelector(`.${elementClassName}`)
    // log(elementClassName, animationClassName)
    // log(elem);
    if (timeoutId){
        clearTimeout(timeoutId);
    };
    elem.classList.add(`${animationClassName}`);
    timeoutId = setTimeout(() =>{
        elem.classList.remove(`${animationClassName}`);
        // log('animation removed')
    }, removeAfter)
}



