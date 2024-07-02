from SohiniMusic.core.bot import Aviax
from SohiniMusic.core.dir import dirr
from SohiniMusic.core.git import git
from SohiniMusic.core.userbot import Userbot
from SohiniMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
