from BubuXDudu.core.bot import Anony
from BubuXDudu.core.dir import dirr
from BubuXDudu.core.git import git
from BubuXDudu.core.userbot import Userbot
from BubuXDudu.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
