# Django course
Read this before you start coding and exploring the code.

This is code from the official Django documentation, here is the link for the reference: https://docs.djangoproject.com/en/4.1/
## Prerequisites
Before you start, you have to install all requirements. Installation process on Linux and Windows:

__1. In your terminal create a new folder where you would like to store this project and enter it:__
```
mkdir Django_project
cd Django_project
```
__2. Clone repository by typing:__
```
git clone https://github.com/Szymon-Budziak/CodeBrainers.git
```
__3. Enter `CodeBrainers/Django/` folder:__
```
cd CodeBrainers/Django/
```
__4. Create new virtual environment for this project and activate it:__
 - Linux machine:
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
this will create new virtual environment with venv name and activate it.

__5. Install required packages:__
```
pip install -r requirements.txt
```
If this command is now working, install django in command line, because this is the only library we will need to work with this project:
```
pip install django
```
__6. Enter `mysite` directory and run `setup.py` file to create questions and choices:__
 - Linux machine:
```
cd mysite && python setup.py
```
(if python is not working try using python3)
- Windows machine:
```
cd mysite
py setup.py
```

__7. Create `superuser` to have access to admin page:__
 - Linux machine:
```
python manage.py createsuperuser
```
(if python is not working try using python3)
- Windows machine:
```
py manage.py createsuperuser
```

Now you are ready to explore Django code and run server, enter polls website `http://localhost:8000/polls/`:
 - Linux machine:
```
python manage.py runserver
```
- Windows machine:
```
py manage.py runserver
```