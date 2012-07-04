import os

from flask import Flask, render_template


# Set up app
app = Flask(__name__, template_folder='../templates')
if not __name__ == '__main__':
    app.config.from_object('app.config')
else:
    app.config.from_object('config')


# Serve static in debug mode
if app.config['DEBUG']:
    from werkzeug.wsgi import SharedDataMiddleware

    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            app.config['STATIC']: os.path.join(
                os.path.dirname(__file__), '../static'
            )
    })


@app.route('/')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
