if [ -d "game_store_env" ]; then rm -Rf game_store_env; fi
if [ -f "db.sqlite3" ]; then rm -f db.sqlite3; fi

virtualenv game_store_env
game_store_env/bin/pip install -r requirements.txt
game_store_env/bin/python manage.py migrate
