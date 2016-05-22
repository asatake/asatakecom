from flask import Flask, render_template, redirect, request, url_for
from flask.ext.assets import Environment, Bundle
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle(
    'scss/variables.scss', 'scss/common.scss',
    filters='pyscss', output='css/common.css'
)
assets.register('scss_all', scss)


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name, title='Top')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/music')
def music():
    return render_template('music.html', title='Music')


@app.route('/works')
def works():
    return render_template('works.html', title='Works')


@app.route('/link')
def link():
    return render_template('link.html', title='Links')

if __name__ == '__main__':
    app.run(debug=True)
