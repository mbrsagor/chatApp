# Eshop ecommerce Package
##### The project is a basically Django E-commerce package which users can implemented any project for the blog app.

## Setup
- Python 3.8
- Postgresql 13.0

<h3>Fist you will clone the product from github</h3>
```bash
https://github.com/mbrsagor/eshop.git
```

The following steps will walk you thru installation Ubuntu. Linux related others OS should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.
If you've developed the django apps run on Windows, you should have little problem getting
up and running.


### Install and active ```vritualenv```
Activate `virutalenv` like
```
cd eshop
virtualenv venv --python=python3.8
source venv/bin/activate
```

### Run the project
```
pip install -r requirements.text
```
###### Then create ``.env`` file and paste code from `sample.env` file and add validate information.

-------------------------------------------
```bash
|--> sample.env
|--> .env
```

### Migrate and create superuser
```
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```

#### Open postgres using terminal database:
```
psql postgres 
```
