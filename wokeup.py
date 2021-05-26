#maybe change to using bearer token
#add cron @reboot item
import os
from os.path import join, dirname
from dotenv import load_dotenv #python-dotenv
from datetime import datetime, timezone

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CK = os.environ.get("CK")
CS = os.environ.get("CS")
ATK = os.environ.get("ATK")
ATS = os.environ.get("ATS")
myname=os.environ.get("YAK_ROVER_NAME","other-bot")

import twitter
api = twitter.Api(consumer_key=CK,
                  consumer_secret=CS,
                  access_token_key=ATK,
                  access_token_secret=ATS)
status = api.PostUpdate('#{}:'.format(name)'I woke up just now, at '+ str(datetime.now(timezone.utc)))