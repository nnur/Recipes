cd usr
sudo mkdir apps
git clone https://github.com/nnur/recipes.git
sudo chmod -R 0777 recipes
cd recipes
apt update
apt install python3-virtualenv
virtualenv .venv
. .venv/bin/activate
sudo pip install -r requirements.txt
gunicorn --bind 0.0.0.0:8000 -w 4 main:app
