from flask import Flask
from main_page.view import main_page

app = Flask(__name__)
app.register_blueprint(main_page)

if __name__ == "__main__":
    app.run(debug=True)