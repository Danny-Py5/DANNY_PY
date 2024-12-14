export function removeCssClassFromArrayOfElem(ArrayElement, rClassName){
    /* 
       ArrayElement: array of elements of which a specific class has to be removed
       rClassName: the class that is to be removed from the ArrayElement. */
       ArrayElement.forEach(elem => {
        elem.classList.remove(rClassName);
    });
}