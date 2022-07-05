// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://10ff.net/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=10ff.net
// @grant        none
// ==/UserScript==

(function () {
    alert("                  SCRIPT made by g4o2#5384 \n                  BUTTON is at the BOTTOM LEFT")
    var sheet = window.document.styleSheets[0];
    sheet.insertRule('button{height:60px;width:150px;background:rgb(29, 29, 29);border-radius:10px;border:solid 3px rgb(212, 0, 0);color:rgb(212, 0, 0)}', sheet.cssRules.length);
    let btn = document.createElement("button");
    btn.innerHTML = "SUPER SPEED";
    btn.onclick = function hack() {

    }
    var myHoverInterval = null;
    btn.addEventListener("click", function () {
        if (myHoverInterval != null) {
            return;
        }
        myHoverInterval = setInterval(function () {
            let text = document.querySelector(".highlight").textContent + " ";
            document.querySelector("input").value = text
            var inputEvent = new InputEvent("input");
            document.querySelector("input").dispatchEvent(inputEvent)
        }, 1);
    });
    document.body.appendChild(btn);
})();