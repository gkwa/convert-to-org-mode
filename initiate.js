// ==UserScript==
// @name      convert-to-org-mode
// @namespace https://taylorm.net
// @version   1
// @match     *://*/*
// @grant     GM_addStyle
// @grant     GM_getResourceText
// @grant     GM_getResourceURL
// @require   https://craig.is/assets/js/mousetrap/mousetrap.min.js?9d308
// @require   https://cdn.jsdelivr.net/npm/alertifyjs@1.12.0/build/alertify.min.js
// @require   file:///Users/mtm/pdev/taylormonacelli/convert-to-org-mode/library.js
// @require   file:///Users/mtm/pdev/taylormonacelli/convert-to-org-mode/initiate.js
// @resource  alertifyCSS https://cdnjs.cloudflare.com/ajax/libs/AlertifyJS/1.12.0/css/alertify.min.css
// @resource  alertifyThemeCSS https://cdnjs.cloudflare.com/ajax/libs/AlertifyJS/1.12.0/css/themes/default.min.css
// ==/UserScript==

document.head.appendChild(cssElement(GM_getResourceURL("alertifyCSS")));
document.head.appendChild(cssElement(GM_getResourceURL("alertifyThemeCSS")));

function b64EncodeUnicode(str) {
  // first we use encodeURIComponent to get percent-encoded UTF-8,
  // then we convert the percent encodings into raw bytes which
  // can be fed into btoa.
  return btoa(encodeURIComponent(str).replace(/%([0-9A-F]{2})/g,
    function toSolidBytes(match, p1) {
      return String.fromCharCode('0x' + p1);
    }));
}

const sendPageToPort = async () => {

  let innerHTML = document.documentElement.innerHTML;
  let encodedString;

  encodedString = b64EncodeUnicode(innerHTML)
  console.log(encodedString);

  let data_dict = {
    host: window.location.host,
    url: document.URL,
    data: encodedString,
    title: document.title
  }

  let options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data_dict)
  }

  let url = "http://127.0.0.1:8989/";
  publish(url, options)
    .then(data => {
      console.log(data);
      alertify.notify("ALL GOOD", "success", 2.0, function() {
        console.log("dismissed");
      });
    })
    .catch(reason => {
      alertify.notify(reason, "error", 5, function() {
        console.log("dismissed");
      });
    });
}

(function () {
  "use strict"
  Mousetrap.bind('ctrl+s', sendPageToPort, 'keydown');
})();
