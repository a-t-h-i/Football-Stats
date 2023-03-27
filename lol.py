import os

all="""aiohttp==3.8.4
aiosignal==1.3.1
asgiref==3.6.0
asn1crypto==0.24.0
async-timeout==4.0.2
asynctest==0.13.0
attrs==22.2.0
certifi==2022.12.7
charset-normalizer==3.1.0
cryptography==2.6.1
dj-database-url==1.2.0
Django==3.2.18
dropbox==11.36.0
entrypoints==0.3
frozenlist==1.3.3
greenlet==0.4.15
gunicorn==20.1.0
idna==3.4
keyring==17.1.1
keyrings.alt==3.1.1
msgpack==0.5.6
multidict==6.0.4
neovim==0.3.0
numpy==1.21.6
openai==0.27.2
pandas==1.3.5
ply==3.11
psycopg2==2.9.5
psycopg2-binary==2.9.5
pycrypto==2.6.1
PyGObject==3.30.4
python-dateutil==2.8.2
pytz==2023.2
pyxdg==0.25
requests==2.28.2
SecretStorage==2.3.1
six==1.12.0
sqlparse==0.4.3
stone==3.3.1
tqdm==4.65.0
typing-extensions==4.5.0
urllib3==1.26.15
yarl==1.8.2"""

for item in all.split(' '):
    os.system('pip3 uninstall '+item)
