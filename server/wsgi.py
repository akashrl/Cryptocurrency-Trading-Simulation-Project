from main import app


# This is the entry point for the production server.
# Please run this in a wsgi-compliant server, preferebly gunicorn.
# Sill need to research this
if __name__ == '__main__':
    # TODO do this before deploying to production
    app.run()
    # raise NotImplementedError("In development, just do `python run.py`")

