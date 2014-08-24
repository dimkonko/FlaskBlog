window.onload = function() {
	var butLogin = document.getElementById("butLogin"),
		input_nickaname = document.getElementById("username");

	butLogin.onclick = function() {
		login(input_nickaname.value);
	}

	function login(_username) {
		$.ajax({
			type: "POST",
			url: "/chat/login",
			data: {"username": _username},
			cache: false,
			async: false,
			success: function(data, b, c) {
				console.log(data)
				document.getElementById("wrapp")
					.innerHTML = data;
			},
			error: function(a, b, c) {
				console.log("Server error");
			}
		});
	}
}