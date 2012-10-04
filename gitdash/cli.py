import logging
import argparse
from flask import Flask
from gitdash.git import Git

app = Flask(__name__)


@app.route("/")
def index():
    log = app.git.log()
    for line in log:
        print line
    return "Hello World"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbosity')
    parser.add_argument('repository')
    args = parser.parse_args()

    app.args = args
    app.git = Git(args.repository)

    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)

if __name__ == '__main__':
    main()
