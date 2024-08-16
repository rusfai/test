function move() {
    const button = document.querySelector(".button");
    let elem = document.getElementById("greenBar");
    let stepValue = 0;
    let id = setInterval(frame, 6000);
    let timerElement = document.querySelector(".number");
    let currentValue = parseInt(timerElement.innerText);
    let textSignalElement = document.getElementById("text-signal");

    button.classList.add("disabled");

    const randomValue = Math.floor(Math.random() * 100) + 1;
    textSignalElement.innerText = randomValue + ".00 x";

    if (currentValue === 0) {
        timerElement.innerText = "60";
        currentValue = 60;
    }

    let timerInterval = setInterval(function() {
        currentValue--;
        timerElement.innerText = currentValue;

        if (currentValue === 0) {
            clearInterval(timerInterval);
            clearInterval(id);

            button.classList.remove("disabled");
        }
    }, 1000);

    function frame() {
        stepValue += 10;
        elem.style.width = stepValue + "%";
        elem.innerHTML = stepValue + "%";

        if (stepValue >= 100) {
            stepValue = 0;
            elem.style.width = stepValue + "%";
            elem.innerHTML = stepValue + "%";
        }
    }
}