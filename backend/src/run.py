"""
Entry point of flask application.
"""

from food_for_all import app, db


@app.shell_context_processor
def make_shell_context():
    return {
        "app": app,
        "db": db
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
