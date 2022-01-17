from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/profile/<string:user_name>")
def profile(user_name):
    print("[pool-3-thread-1] INFO  [SimpleJobLauncher.java:133 run] - [Job: [SimpleJob: [name=jobXXXThread]] launched with the following parameters: [{time=1583247660000}]]")
    return "{name}さんのプロフィール画面です".format(name=user_name)


@app.route("/profile1/<string:user_name>")
def profile1(user_name):
    print("[taskExecutorXXX-1] ERROR [CollectEvent.java:109 collectEvent] - [NoData MongoDB tenant : ob7bf dataType : EV0000000001 from : 2020-03-03 14:57:00 to : 2020/03/03 14:58:00]")
    return "{name}さんのプロフィール画面です".format(name=user_name)


if __name__ == "__main__":
    app.run()
