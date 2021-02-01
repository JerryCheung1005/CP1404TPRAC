from flask import Flask

app = Flask(__name__)


@app.route('/')
def name():
    return 'ZHANG JIAYU 13851049'

if __name__ == '__main__':
    app.run()