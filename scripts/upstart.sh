cd /usr
sudo mkdir apps
cd apps
sudo git clone https://github.com/nnur/recipes.git
sudo chmod -R 0777 recipes
cd recipes
sudo apt update
sudo apt install python3-virtualenv -y
virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:8000 -w 4 main:app
