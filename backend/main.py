from app.api import create_app
from config import CONFIG

api = create_app(config=CONFIG)

if __name__ == "__main__":
    api.run()
