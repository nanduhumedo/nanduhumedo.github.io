var request = new XMLHttpRequest();

request.open('GET', 'http://www.nfrancque.pythonanywhere.com/get_chain')

document.write('hello world')
request.onload = function () {
	document.write(this.response)
}
