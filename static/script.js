var request = new XMLHttpRequest();


document.write('hello world')

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
  document.getElementById("demo").innerHTML =
  this.responseText;
}
};
xhttp.open("GET", "/get_chain", true);
xhttp.send();