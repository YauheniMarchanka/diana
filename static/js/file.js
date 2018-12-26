
const url = "/server_time";
function fetch_data(_url) {
fetch(_url, {
    method : "POST",
    body : JSON.stringify({})
        // user : document.getElementById('user').value,
        // ...
    // })
}).then(
    response => response.json() // .json(), etc.
    // same as
).then(
    function(elem) {
        console.log('Elem.data', elem.data);
        var item = document.getElementById("timepos");
        item.innerHTML = elem.data;
        return elem;
    }
);
}

window.onload = function(e){
    console.log("window.onload", e, Date.now());
    fetch_data(url);
    var timerId = setInterval(function() {
  fetch_data(url);
}, 1000);
}