let inputTextArea = document.getElementById("input-textarea");
let characCount = document.getElementById("charac-count");

let wordCount = document.getElementById("word-count");

let insta = document.getElementById("instagram-count");

let FB = document.getElementById("facebook-count");

let Wapp = document.getElementById("whatsapp-count");

inputTextArea.addEventListener("input", () => {
    let temp = inputTextArea.value.length;
    characCount.textContent = temp;
    insta.textcontent = temp;

    let txt = inputTextArea.value.trim();

    wordCount.textContent = txt.split(/\s+/).filter((item) => item).length;

});

