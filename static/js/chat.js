document.onload = function() {
	console.log("Loaded!")
	var msg_log = document.getElementById("msg_log"),
		msg_input = document.getElementById("msg_input"),
		but_send = document.getElementById("send_msg");

	var username = msg_input.getAttribute("name");
	console.log(username);

	but_send.onclick = function() {
		sendMsg(msg_input.value + "\n");
	}

	function sendMsg(msg) {
		$.ajax({
			type: "POST",
			url: "/chat/chat_msg",
			data: {"username": username, "msg": msg},
			cache: false,
			success: function(data, b, c) {
				if(data["status"] == "1") {
					msg_log.value += data["msg"] + "\n"
				}
			},
			error: function(a, b, c) {
				console.log("Server error");
			}
		});
	}

	function getMsgLog() {
		console.log("get")
		$.ajax({
			type: "GET",
			url: "/chat/get_msg_log",
			cache: false,
			success: function(data, b, c) {
				msg_list = data["msg_log"];
				msg_log.value = "";
				for(var i = 0; i < msg_list.length; i++) {
					msg_log.value += msg_list[i];
				}
			},
			error: function(a, b, c) {
				console.log("Server error");
			},
			complete: function() {
		    	setTimeout(getMsgLog, 2000);
			}
		});
	}

	getMsgLog();
}