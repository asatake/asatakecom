from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name, title='Top')

if __name__ == '__main__':
    app.run()
