// ==UserScript==
// @name      convert-to-org-mode
// @namespace https://taylorm.net
// @version   1
// @match     *://*/*
// @require   https://craig.is/assets/js/mousetrap/mousetrap.min.js?9d308
// @require   file:///Users/mtm/pdev/taylormonacelli/convert-to-org-mode/initiate.js
// @require   file:///Users/mtm/pdev/taylormonacelli/convert-to-org-mode/library.js
// @grant     GM_addStyle
// @grant     GM_getResourceText
// @grant     GM_getResourceURL
// ==/UserScript==

const publish = async (url, options) => {
  return new Promise((resolve, reject) => {
    fetchAsync(url, options)
      .then(data => {
        resolve(data);
      })
      .catch(reason => {
        console.log(reason);
        reject(reason);
      });
  });
};

function b64EncodeUnicode(str) {
  // first we use encodeURIComponent to get percent-encoded UTF-8,
  // then we convert the percent encodings into raw bytes which
  // can be fed into btoa.
  return btoa(
    encodeURIComponent(str).replace(/%([0-9A-F]{2})/g, function toSolidBytes(
      match,
      p1
    ) {
      return String.fromCharCode("0x" + p1);
    })
  );
}

function sendPageToPort(url) {
  let innerHTML = document.documentElement.innerHTML;
  let encodedString = b64EncodeUnicode(innerHTML);
  console.log(`debug data substring: ${encodedString.substring(1, 100)}`);

  let data_dict = {
    host: window.location.host,
    url: document.URL,
    data: encodedString,
    title: document.title
  };

  let options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data_dict)
  };

  publish(url, options)
    .then(data => {})
    .catch(reason => {
      console.log(reason);
    });
}

const initiateWorkflow = async url => {
  sendPageToPort(url);
};

(function() {
  "use strict";
  // ------------------------------
  console.log("==> Script start.", new Date());

  // 1ST PART OF SCRIPT RUN GOES HERE.
  console.log("==> 1st part of script run.", new Date());

  document.addEventListener("DOMContentLoaded", DOM_ContentReady);
  window.addEventListener("load", pageFullyLoaded);

  function DOM_ContentReady() {
    // 2ND PART OF SCRIPT RUN GOES HERE.
    // This is the equivalent of @run-at document-end
    console.log("==> 2nd part of script run.", new Date());
  }

  function pageFullyLoaded() {
    console.log("==> Page is fully loaded, including images.", new Date());
  }

  console.log("==> Script end.", new Date());
  // ------------------------------

  Mousetrap.bind(
    "ctrl+s",
    function() {
      initiateWorkflow("http://127.0.0.1:8989");
    },
    "keydown"
  );
})();
