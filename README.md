# thunderuserbot
<p align="center">
<img src="https://telegra.ph/file/6ad3dc5bd1ce286cbb094.jpg" alt="THUNDER USERBOT">

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


Best User Bot To Manage Your Telegram Account 
## Most Cool And Better And Trusted

## © By Team #ThunderGᴀɴɢ™

### For any query or want to know how it works join our Channel and Support Group 

<a href="https://t.me/thunderuserbot"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>
<a href="https://t.me/thunderuserbotchat"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>
## Don't Forget To Give A Star ⭐

## FORK NOT ALLOWED !


### Deploy Thunderuserbot In Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Thundergang/thunderuserbot)


## Telegram-String

[![Run on Repl.it](https://repl.it/badge/github/Thundergang/thunderuserbot)](https://thundergang.deadanonymous.repl.run)


Simply clone the repository and run the main file:

```bash
git clone https://github.com/Thundergang/thunderuserbot
cd thunderuserbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

**The Userbot should work by setting only the first two variables**

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  # 6 is the length of api id
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  # Use Your Own Api Hash these are just for example
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration** Simply just leave the Config as it is.

**Local Configuration** Fortunately there are no Mandatory vars for the UniBorg
Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
  - `APP_ID`: You can get this value from https://my.telegram.org
  - `API_HASH`: You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

##  CONTRIBUTIONS IN MAKING BASE FOR USERBOT WORLD

Thanks to Uniborg™,Paperplane™,Indianbot™,Thundergang™
