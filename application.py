from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/info")
def profile():
    print("[pool-3-thread-1] INFO  [SimpleJobLauncher.java:133 run] - [Job: [SimpleJob: [name=jobXXXThread]] launched with the following parameters: [{time=1583247660000}]]")
    return "infoのログ


if __name__ == "__main__":
    app.run()
