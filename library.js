async function fetchAsync(url, options) {
  // await response of fetch call
  let response = await fetch(url, options);
  // only proceed once promise is resolved
  let data = await response.json();
  // only proceed once second promise is resolved
  return data;
}
