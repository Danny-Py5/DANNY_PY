const footerHTML = `
        <section class="a-a">
            <h2 class="a-a__h2"><span>Little</span> Fashion</h2>
            <p>Copyright &copy; 2024 <strong>Little Fashion</strong></p>
            <p class="developer">Designed by DannyPy</p>
        </section>

        <section class="socials-container">
            <section class="socials-container__left">
                <h2 class="socials-container__h2">Sitemap</h2>
                <a href="#" class="social-link" >Story</a>
                <a href="#" class="social-link" >Privacy policy</a>
                <a href="#" class="social-link" >Contact</a>
            </section>
            
            <section class="socials-container__middle">
                <a class="social-link" href="#">Products</a>
                <a href="#" class="social-link" >FAQs</a>
            </section>

            <section class="socials-container__right" >
                <h2 class="socials-container__h2">Social</h2>
                <a href="#" class="social-link">YouTube</a>
                <a href="#" class="social-link">Facebook</a>
                <a href="#" class="social-link">WhatsApp</a>
            </section>
        </section>
`;

document.querySelector('.js-footer').innerHTML = footerHTML;

