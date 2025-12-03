from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker + GitHub + EC2!"

if __name__ == "__main__":
    # important: 0.0.0.0 so Docker can expose it
    app.run(host="0.0.0.0", port=5000)
