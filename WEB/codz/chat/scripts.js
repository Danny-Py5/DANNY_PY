function sendMessage() {
    let newSentMassageElem = document.createElement('div');
    let messsageBodyPElem = document.createElement('p');

    const userTypedMessgeElem = document.getElementById('message');

    if (userTypedMessgeElem.value.trim()){
        messsageBodyPElem.textContent = userTypedMessgeElem.value;
        newSentMassageElem.appendChild(messsageBodyPElem);
        newSentMassageElem.classList.add('sent-message-body');
        document.querySelector('.chats').appendChild(newSentMassageElem);
        // clear the message elem
        userTypedMessgeElem.value = '';
        setTimeout(() => {
            respond()
        }, 500)
    }

}
const randomResponses = [
    'Hello, how are you doing',
    'Am fine and you?',
    'How was your day',
    'I am the best. doing great, you are good always'
]

function respond(){
    let newResponseMassageElem = document.createElement('div');
    let responseBodyPElem = document.createElement('p');

    const responseIndex = Math.floor(Math.random() * randomResponses.length);
    responseBodyPElem.textContent = randomResponses[responseIndex];

    newResponseMassageElem.appendChild(responseBodyPElem);
    newResponseMassageElem.classList.add('received-message-body');
    document.querySelector('.chats').appendChild(newResponseMassageElem);
    
}

const sendButton = document.querySelector('.send');
sendButton.addEventListener('click', sendMessage)

const messageTexarea = document.getElementById('message');
messageTexarea.addEventListener('keydown', (event) => {
    if(event.key == 'Enter'){
        sendMessage();
    }
})