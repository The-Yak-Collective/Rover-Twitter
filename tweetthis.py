#maybe change to using bearer token
#add cron @reboot item
import os
import sys
from os.path import join, dirname
from dotenv import load_dotenv #python-dotenv
from datetime import datetime, timezone

ll=len(sys.argv)
if ll<2: #was called with no args
    sys.exit(0)

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
thetext=sys.argv[1]
if ll==2: #was called with just text (in quote marks, i hope)
    status = api.PostUpdate('#{}: '.format(myname)+thetext) #was: I woke up just now, at '+ str(datetime.now(timezone.utc))+" UTC"
else: #2nd parameter is always a single media file name
    themedia=sys.argv[2]
    status = api.PostUpdate('#{}: '.format(myname)+thetext,media=themedia)
