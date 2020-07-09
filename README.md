# amadersheba
##### The project basically I had taught my university younger brothers. when I was a new starting in Django. The proejct main theme is user sell and buy old or new products which look like idea Bikroy.com.

## Setup
You have must be install python3 and Django 2.0 on your operation system. Be default I used `sqlite` database in the project. If may use another `database` in this app.

<h3>Fist you will clone the product from github</h3>

The following steps will walk you thru installation Ubuntu. Linux related others OS should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.
If you've developed the django apps run on Windows, you should have little problem getting
up and running.


### Install ```vritualenv```
Activate `virutalenv` like
```
source venv/bin/activate
```

### Run the project
```
pip install -r requirements.text
```


### Migrate and create superuser
```
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```
