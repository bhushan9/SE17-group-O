# run.py

import os

from app import create_app
#from news import news_job
#from social import social_job


app = create_app('development')

if __name__ == '__main__':
    #news_job.news_job()
    #social_job.social_job()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, use_reloader=False)
