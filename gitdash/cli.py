import logging
import argparse
from flask import Flask, render_template, request
from gitdash.git import Git

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        app.git.checkout(request.form['commit'])
    return render_template('log.html',
        log=app.git.log(app.args.branch),
        head=app.git.head(),
        )


@app.route("/update", methods=["POST"])
def update():
    return app.git.update()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbosity')
    parser.add_argument('-b', '--branch', default='master')
    parser.add_argument('repository')
    args = parser.parse_args()

    app.args = args
    app.git = Git(args.repository)

    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)

if __name__ == '__main__':
    main()
