export const overlay = {
     createOverlayDiv() {
        const div = document.createElement('div');
        div.classList.add('disable');
        Object.assign(div.style, {
            position: 'fixed',
            top: '0',
            zIndex: '-1',
        });
        document.body.appendChild(div);
    },

    
    enableOverlay(){
        this.createOverlayDiv();
        const disableElem = document.querySelector('.disable');

        disableElem.style.zIndex = '1';
        disableElem.style.backgroundColor = '#88888858';
        disableElem.style.width = '100vw';
        disableElem.style.height = '100vh';
    }, 
    
    disableOverlay(){
        const disableElem = document.querySelector('.disable');
        disableElem.style.zIndex = '-1';
        disableElem.style.backgroundColor = 'transparent'
    },
};



