# run.py

import os

from app import create_app
from news import news_job


config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    news_job.news_job()
    app.run()
