let nextText = document.querySelector("#text > .next");
let mainInput = document.querySelector("#type");
let top_stuff = document.querySelector("#counter");
let bottom_stuff = document.querySelector("#text");
let h1 = document.createElement("h1");
let hahah = document.createElement("p");
h1.innerText = "Нажимай на кнопку пробела с небольшим интервалом";
hahah.innerText = "пользуйся на здоровье ;) (с тебя вкусняшка)";
h1.style.color = "red";
h1.style.fontSize = "36px";
hahah.style.fontSize = "24px";
hahah.style.color = "red";
top_stuff.append(h1);
mainInput.before(hahah);
document.addEventListener("keydown", (event) => {
    if (event.key === " ") {
        // event.preventDefault();
        // event.preventDefault('')
        setTimeout(() => {
            typing();
        }, [100]);
    }
});

function typing() {
    mainInput.focus();
    let currentText = document.querySelector("#text > .current");
    let text = currentText.innerText;
    let index = 0;
    let interval = setInterval(function () {
        if (index < text.length) {
            mainInput.value += text[index];
            let event = new Event("input", { bubbles: true });
            mainInput.dispatchEvent(event);
            index++;
        } else {
            clearInterval(interval);
        }
    }, 10);
}
