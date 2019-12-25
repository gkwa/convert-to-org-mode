// ==UserScript==
// @name      convert-to-org-mode
// @namespace https://taylorm.net
// @version   1
// @match     *://*/*
// @require   https://craig.is/assets/js/mousetrap/mousetrap.min.js?9d308
// @require   https://cdn.jsdelivr.net/npm/alertifyjs@1.12.0/build/alertify.min.js
// @require   file:///Users/mtm/pdev/taylormonacelli/convert-to-org-mode/initiate.js
// @resource  alertifyCSS https://cdnjs.cloudflare.com/ajax/libs/AlertifyJS/1.12.0/css/alertify.min.css
// @resource  alertifyThemeCSS https://cdnjs.cloudflare.com/ajax/libs/AlertifyJS/1.12.0/css/themes/default.min.css
// @grant     GM_addStyle
// @grant     GM_getResourceText
// @grant     GM_getResourceURL
// ==/UserScript==

function cssElement(url) {
  var link = document.createElement("link");
  link.href = url;
  link.rel = "stylesheet";
  link.type = "text/css";
  return link;
}

async function fetchAsync(url, options) {
  // await response of fetch call
  let response = await fetch(url, options);
  // only proceed once promise is resolved
  let data = await response.json();
  console.log(`data: ${data}`);

  // only proceed once second promise is resolved
  return data;
}

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

function alertHealthStatus(url) {
  let options = {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    }
  };

  publish(url, options)
    .then(data => {
      alertify.notify("Endpoint is open", "success", 1, function() {
        console.log("alertifyjs reporting: dismissed");
      });
    })
    .catch(reason => {
      alertify.notify(reason.message, "error", 0, function() {
        console.log("alertifyjs reporting: dismissed");
      });
    });
}

function sendCurrentPageToEndpoint(url) {
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
    .then(data => {
      alertify.notify("Save completed", "success", 1, function() {
        console.log("alertifyjs reporting: dismissed");
      });
    })
    .catch(reason => {
      alertify.notify(reason.message, "error", 0, function() {
        console.log("alertifyjs reporting: dismissed");
      });
    });
}

const initiateWorkflow = async url => {
  // its a long running task so first just give status to say whether
  // endpoint is available
  alertHealthStatus(`${url}/healthcheck`);

  // meat
  sendCurrentPageToEndpoint(url);
};

function alertifySetup() {
  document.head.appendChild(cssElement(GM_getResourceURL("alertifyCSS")));
  document.head.appendChild(cssElement(GM_getResourceURL("alertifyThemeCSS")));
}

(function() {
  "use strict";
  // ------------------------------
  console.log("==> Script start.", new Date());

  // 1ST PART OF SCRIPT RUN GOES HERE.
  alertifySetup();
  console.log("==> 1st part of script run.", new Date());

  document.addEventListener("DOMContentLoaded", DOM_ContentReady);
  window.addEventListener("load", pageFullyLoaded);

  function DOM_ContentReady() {
    // 2ND PART OF SCRIPT RUN GOES HERE.
    // This is the equivalent of @run-at document-end
    console.log("==> 2nd part of script run.", new Date());
    alertifySetup();
  }

  function pageFullyLoaded() {
    console.log("==> Page is fully loaded, including images.", new Date());
  }

  console.log("==> Script end.", new Date());
  alertifySetup();
  // ------------------------------

  Mousetrap.bind(
    "g s",
    function() {
      initiateWorkflow("http://127.0.0.1:8989");
    },
    "keydown"
  );
  alertifySetup();
})();
