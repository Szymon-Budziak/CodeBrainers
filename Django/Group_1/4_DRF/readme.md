# DRF

Read this before you start coding and exploring the code.

This is code from the Beginner's Guide to the Django Rest Framework tutorial, here is the link for the
reference: [Beginner's Guide to the Django Rest Framework](https://code.tutsplus.com/tutorials/beginners-guide-to-the-django-rest-framework--cms-19786)

## Prerequisites

Before you start, you have to install all requirements. Installation process on Linux/macOS and Windows:

__1. In your terminal create a new folder where you would like to store this project and enter it:__

```
mkdir DRF
cd DRF
```

__2. Clone repository by typing:__

```
git clone https://github.com/Szymon-Budziak/CodeBrainers.git
```

__3. Enter `CodeBrainers/Django/4_DRF/` folder:__

```
cd CodeBrainers/Django/4_DRF/
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

If this command is now working, install `django` and `djangorestframework` in command line:

```
pip install django
pip install djangorestframework
```

__6. Enter `django_rest` directory and run `setup.py` file to create custom data:__

- Linux/macOS machine:

```
cd django_rest && python setup.py
```

(if python is not working try using python3)

- Windows machine:

```
cd django_rest
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

Now you are ready to explore Django and DRF code and run server, enter bookreview/authors/
website `http://localhost:8000/bookreview/authors/`:

- Linux/macOS machine:

```
python manage.py runserver
```

(if python is not working try using python3)

- Windows machine:

```
py manage.py runserver
```