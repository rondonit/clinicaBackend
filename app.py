from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "fazer em quantidade não é fácil"

if __name__ == '__main__':
    app.run(debug=True)
