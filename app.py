from flask import Flask, render_template


###################
##
## Initial
##
###################

# Set up app
app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

# Serve static in debug mode
if app.config['DEBUG']:
    from werkzeug.wsgi import SharedDataMiddleware

    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            app.config['STATIC']: 'static'
    })


###################
##
## Views
##
###################

@app.route('/')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
