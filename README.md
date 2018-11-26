## # CourseFlow

## Installing 
Clone repository 
Open terminal and navigate to 'CourseFlow' directory.

First check to make sure pip is installed. If not run the command: sudo easy_install pip

After installing pip, run the following commands:
```
python3 -m"venv" env
source env/bin/activate 
pip install -r requirements.txt 
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

Copy and paste the local host url: http://127.0.0.1:8000/login