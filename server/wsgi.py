from main import create_app


# This is the entry point for the production server.
# Please run this in a wsgi-compliant server, preferebly gunicorn.
# Sill need to research this
if __name__ == '__main__':
    # TODO do this before deploying to production
    create_app().run()
    #app.run()
    #socketio_app.run(app, host='0.0.0.0', debug=True, port=5000)
    # raise NotImplementedError("In development, just do `python run.py`")

