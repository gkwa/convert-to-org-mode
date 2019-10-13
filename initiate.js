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
  let response = await fetch(url, options);
}

(function () {
  "use strict"
  Mousetrap.bind('ctrl+s', sendPageToPort, 'keydown');
})();
