#x
#xx
#xxx
#xxxx

from flask import Flask
app = Flask(__name__)

@app.route('/')
def Dhules():
    return 'BotsBro'


if __name__ == "__main__":
    app.run()
