
"""Application entry point."""
from front_end_with_flask import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
