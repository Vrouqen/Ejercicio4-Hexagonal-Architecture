# App entry point

from infraestructure.web.flask_controller import app

if __name__ == "__main__":
    app.run(debug=True)
