from flask import Blueprint, render_template, request, jsonify

chat = Blueprint("chat", __name__,
                 template_folder="templates")

users_list = list()
msg_log = list()

@chat.route("/chat")
def chat_main():
    return render_template("index.html")

@chat.route("/chat/login", methods=["POST"])
def login():
	username = request.form["username"]
	return render_template("chat_log.html", name=username)

@chat.route("/chat/chat_msg", methods=["POST"])
def chat_msg():
	# smth = request.form
	# print smth["msg"]
	# return make_response("ok")
	username = request.form["username"]
	msg = request.form["msg"]
	msg_item = username + ": " + msg

	print msg_item
	if len(msg_log) > 40:
		shift(msg_item, 1)
		msg_log[-1] = msg_item
		print "More"
	else:
		msg_log.append(msg_item)
	return jsonify({"status": "1", "msg": msg_item})

@chat.route("/chat/get_msg_log", methods=["GET"])
def get_logs():
	print msg_log
	return jsonify({"msg_log": msg_log})

def shift(l, n):
	return l[n:] + l[:n]
