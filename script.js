var request = new XMLHttpRequest();

request.open('GET', 'http://www.nfrancque.pythonanywhere.com/get_chain')


request.onload = function () {
	document.write(this.response)
}