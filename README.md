## Deployment

#### To deploy this project run

Clone the github repository:

```bash
  git clone https://github.com/ramshadvv/python-web.git
```

Go to the project directory:

```bash
  cd python-web
```

Create virtualenv:

```bash
  python -m venv env
```

Activate environment:

```bash
  env/Scripts/activate
```

install dependencies:

```bash
  pip install -r requirements.txt
```

Migarte all models:

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Start the server:

```bash
  python manage.py runserver
```
