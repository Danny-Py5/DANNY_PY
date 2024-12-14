
let porductData = [
    {
        image: './images/product/evan-mcdougall-qnh1odlqOmk-unsplash.jpeg', 
        label: 'New Arrival',
        description: {
            name: 'Tree pot', 
            content: 'Original package design from house',
            price: '88' 
        },
    },
    {
        image: './images/product/jordan-nix-CkCUvwMXAac-unsplash.jpeg', 
        label: 'Low Price',
        description: {
            name: 'Fashion Set', 
            content: 'Costume Package',
            price: '90' 
        },
    },
    {
        image: './images/product/nature-zen-3Dn1BZZv3m8-unsplash.jpeg', 
        label: 'New Product',
        description: {
            name: 'Juice Drinks', 
            content: 'Nature made another world',
            price: '100' 
        },
    },
    {
        image: 'images/product/team-fredi-8HRKoay8VJE-unsplash.jpeg', 
        label: 'Trending',
        description: {
            name: 'Package', 
            content: 'Original package design from house',
            price: '50' 
        },
    },
    {
        image: 'images/product/quokkabottles-kFc1_G1GvKA-unsplash.jpeg', 
        label: 'DannyPy &smile;',
        description: {
            name: 'Buttle', 
            content: 'Package Design',
            price: '100' 
        },
    },
    {
        image: 'images/product/anis-m-WnVrO-DvxcE-unsplash.jpeg', 
        label: 'New Product DannyPy &smile;',
        description: {
            name: 'Medicine', 
            content: 'Original Design From House',
            price: '200' 
        },
    },
];

let productHTML = document.querySelector('.featured-product-contaner');

function generateProductHTML() {
    let html = '';
    porductData.forEach((data, index) => {
        html += `
        <article class="featured-product__product">
        <figure>
        <a href="product-details.html">
                        <img src="${data.image}" alt="product" width="500">
                    </a>
                    <figcaption class="featured-product__label">${data.label}</figcaption>
                </figure>
                <article class="featured-product-discription">
                    <section >
                        <a class="link-secondary" href="#">${data.description.name}</a>
                        <p class="f-color-secondary">${data.description.content}</p>
                    </section>
                    <p>$${data.description.price}</p>
                </article>
                </article>
                ${index === 2 ? '<section class="popular"><h2>Popular</h2></section>' : ''}
        `;
    })
    productHTML.innerHTML = html;
};
generateProductHTML();