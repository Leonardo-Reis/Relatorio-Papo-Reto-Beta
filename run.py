from flask import render_template
from app import app
import os


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
