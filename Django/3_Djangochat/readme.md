# Djangochat app project

Read this before you start coding and exploring the code.

## Prerequisites

Before you start, you have to install all requirements. Installation process on Linux/macOS and Windows:

__1. In your terminal create a new folder where you would like to store this project and enter it:__

```
mkdir Djangochat
cd Djangochat
```

__2. Clone repository by typing:__

```
git clone https://github.com/Szymon-Budziak/CodeBrainers.git
```

__3. Enter `CodeBrainers/Django/3_Djangochat/` folder:__

```
cd CodeBrainers/Django/3_Djangochat/
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

If this command is now working, install `django` and `channels` in command line:

```
pip install django channels
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

Now you are ready to explore Django code and run server, enter dashboard website `http://localhost:8000`:

- Linux/macOS machine:

```
python manage.py runserver
```

(if python is not working try using python3)

- Windows machine:

```
py manage.py runserver
```