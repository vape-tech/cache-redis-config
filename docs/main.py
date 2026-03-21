import redis
from config import Config
from app import create_app

config = Config()
app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)