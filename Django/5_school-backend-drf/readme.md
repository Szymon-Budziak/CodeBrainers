# School API

Read this before you start coding and exploring the code.

## Prerequisites

Before you start, you have to install all requirements. Installation process on Linux/macOS and Windows:

__1. In your terminal create a new folder where you would like to store this project and enter it:__

```
mkdir school_api
cd school_api
```

__2. Clone repository by typing:__

```
git clone https://github.com/Szymon-Budziak/CodeBrainers.git
```

__3. Enter `CodeBrainers/Django/5_school-backend-drf/` folder:__

```
cd CodeBrainers/Django/5_school-backend-drf/
```

__4. Create new virtual environment for this project and activate it:__

- Linux/macOS machine:

```
python -m venv venv
source venv/bin/activate
```

(if python is not working try using python3)

- Windows machine:

```
py -m venv venv
venv\Scripts\activate
```

this will create new activated virtual environment with `venv` name.

__5. Install required packages:__

```
pip install -r requirements.txt
```

If this command is now working, install `django`, `djangorestframework`, `pytest`, `python-dotenv` and `drf-extensions`
in command line:

```
pip install django
pip install djangorestframework
pip install pytest
pip install python-dotenv
pip install drf-extensions
```

__6. Enter `school_drf`, `.env` file and run `setup.py` file:

- Linux/macOS machine:

```
cd school_drf
touch .env
python setup.py
```

(if python is not working try using python3)

- Windows machine:

```
cd school_drf
touch .env
py setup.py
```

__7. Create `superuser` to have access to admin page:__

- Linux/macOS machine:

```
python manage.py createsuperuser
```

(if python is not working try using python3)

- Windows machine:

```
py manage.py createsuperuser
```

Now you are ready to explore Django and DRF code and run server, enter api/exams/
website `http://localhost:8000/api/exams/`:

- Linux/macOS machine:

```
python manage.py runserver
```

(if python is not working try using python3)

- Windows machine:

```
py manage.py runserver
```