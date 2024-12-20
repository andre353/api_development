# API Development 

The API Development project provides a visual demonstration of skills and knowledge of System Analysis domain including:
- Rest API JavaScript
- Rest API Python
- Postman CI/CD testing automation, newman, htmlextra
- XML
- openRPC


## Rest API Python последовательность

Создать общую папку
в ней main.py
создать окружение командой python -m venv .venv
выйти из окружения `source deactivate`
войти в окружение: `source activate`
или `source .venv/bin/activate`
`pip install requests`
`pip install flask`
`pip install flask-sqlalchemy`
`pip freeze > requirements.txt`
`touch application.py`
`export FLASK_APP=application.py`
`export FLASK_ENV=development`
`flask run`

`main.py`
`from flask import Flask, request`
`from flask_sqlalchemy import SQLAlchemy`
  
`app = Flask(__name__)`
`app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"`
`db = SQLAlchemy(app)`
`app.app_context().push()` 

`class Drink(db.Model):`
    `id = db.Column(db.Integer, primary_key=True)`
    `name = db.Column(db.String(80), unique=True, nullable=False)`
    `description = db.Column(db.String(120))`

    `def __repr__(self):`
        `return f"Drink('{self.name}', '{self.description}')"`

Входим в интерактивный  режим
`python`
`from application import db`

`db.create_all()`
`from application import Drink`
`Drink`
`drink = Drink(name="Grape Soda", description="Tastes like grapes")`
`drink.name`
`drink.description`

`db.session.add(drink)`
`db.session.commit()`

`Drink.query.all()`

добавить новый объект класса Drink

`db.session.add(Drink(name="Cherry", description="Tastes like that one ice creame"))`
`drink = Drink(name="Lemon Drink", description="Tastes like lemon")`
`db.session.add(drink)`
`db.session.commit()`

`db.session.add(Drink(name="Cherry", description="Tastes like that one ice creame"))`
`db.session.commit()`

`db.session.add(Drink(name="Lemon Drink", description="Tastes like lemon"))`
`db.session.commit()`

`Drink.query.all()`
`[<Drink 'Grape Soda'>, <Drink 'Cherry'>, <Drink 'Lemon Drink'>]`

`flask run`

Написать функции под каждый метод: GET (по умолчанию), POST, DELETE

Через Postman протестить каждый метод