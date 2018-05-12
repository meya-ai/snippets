mkdir {BOTNAME}
cd {BOTNAME}
virtualenv env
. env/bin/activate
pip install meya
meya-cli init {USER_AUTH_TOKEN} {BOT_ID}
meya-cli watch
