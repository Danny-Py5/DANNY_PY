const digitalClock = document.getElementById('js-digital-clock');

// getting the hour, minute, and second elements
const clock = {
    // PZ: padwith-zero
    hour: {
        PZ: digitalClock.querySelector('.hour-padwith-zero'),
        hour: digitalClock.querySelector('.hour')
    }, 
    minute: {
        PZ: digitalClock.querySelector('.minute-padwith-zero'),
        minute: digitalClock.querySelector('.minute')
    }, 
    second: {
        PZ: digitalClock.querySelector('.second-padwith-zero'),
        second: digitalClock.querySelector('.second')
    }
};

// document.querySelector('.set').addEventListener('click', () => {
//     clock.hour.hour.innerHTML = document.getElementById('HOUR').value;
//     clock.minute.minute.innerHTML = document.getElementById('MINUTE').value;
//     clock.second.second.innerHTML = document.getElementById('SECOND').value;
// });

function runTime(){
    let hour = Number(clock.hour.hour.textContent);
    let minute = Number(clock.minute.minute.textContent);
    let second = Number(clock.second.second.textContent);
    let mmm = false;
    setInterval(function (){
        // seconds incremental logics
        second++
        if (second === 60){
            second = 0;
        }
        clock.second.second.textContent = second;
        if (String(second).length > 1) {
            clock.second.PZ.textContent = ''
        } else {
            clock.second.PZ.textContent = '0'
        };

        // minute incremental logics
        if (second === 0){
            minute++ 
            if (minute === 60){
                minute = 0;
                mmm = true;
            }
            clock.minute.minute.textContent = minute;
            if (String(minute).length > 1) {
                clock.minute.PZ.textContent = ''
            } else {
                clock.minute.PZ.textContent = '0'
            };
        }

        // hour incremental logics
        if (mmm){
            hour++ 
            mmm = false
            if (hour === 24){
                hour = 0;
            }
            clock.hour.hour.textContent = hour;
            if (String(hour).length > 1) {
                clock.hour.PZ.textContent = ''
            } else {
                clock.hour.PZ.textContent = '0'
            };
        };


        // [clock.hour, clock.minute, clock.second].forEach(element => {
        //     [hour, minute, second].forEach((time) => {
        //         if (String(time).length > 1){
        //             element.PZ.textContent = '';
        //         } else {
        //             element.PZ.textContent = '0';
        //         };
        //     });
        // }) 
    }, 1000); 
};
runTime();



// spread the clock number
document.querySelectorAll('.clock-number').forEach(clockHand => {
    let aa = 33;
    clockHand.style.setProperty('--translateValue', String(aa) +'px');
    aa += 10;
})


let clockHandElem = document.querySelector('.hand')
 
document.addEventListener('DOMContentLoaded', () => {
    let rotateValue = parseInt(clockHandElem.getAttribute('data-one'));
    
    setInterval(() => {
        let rotateValuePluesDeg = String(rotateValue) + 'deg';
        console.log(rotateValuePluesDeg);
        clockHandElem.style.setProperty('--rotate-angle', rotateValuePluesDeg);
        rotateValue += 6;
    }, 1000)
})


