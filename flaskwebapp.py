from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Chika baby is going to be a DevOps Engineer!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Change the port number here
