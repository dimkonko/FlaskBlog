window.onload = function() {
	var openBut = document.getElementById("open_modal_but");
	var modal = Modal(document.getElementById("main_modal"));

	openBut.onclick = function() {
		modal.show();
	}
}