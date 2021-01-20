import os
from os.path import join, dirname
from dotenv import load_dotenv #python-dotenv
from datetime import datetime, timezone

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CK = os.environ.get("CK")
CS = os.environ.get("CS")
AT = os.environ.get("AT")
ATS = os.environ.get("ATS")

import twitter
api = twitter.Api(consumer_key=CK,
                  consumer_secret=CS,
                  access_token_key=AT,
                  access_token_secret=ATS)
status = api.PostUpdate('I am alive at '+ str(datetime.now(timezone.utc)))