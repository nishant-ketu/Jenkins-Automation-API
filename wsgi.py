'''__main__.py file'''
from app import app
from app.routes import home

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8880')
