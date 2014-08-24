from flask import Flask
from main_page.view import main_page
from chat.view import chat

app = Flask(__name__)
app.register_blueprint(main_page)
app.register_blueprint(chat)

@app.route("/")
def main():
	return "Hello!"

if __name__ == "__main__":
    app.run(debug=True)