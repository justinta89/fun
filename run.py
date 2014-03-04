# from app import create_app
from app import app

#app = create_app()
if __name__ in ['__console__', '__main__']:
    app.run(debug=True)