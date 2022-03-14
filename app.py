from flask import Flask,render_template,session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route("/index")
def index():
    #show items on the todo app
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template("index.html")

if __name__ == "__main__":
    db.create_all()
    
    #create new item on the todo app
    new_todo = Todo(title="Todo 1",complete=False)
    db.session.add(new_todo)
    db.session.commit()

    app.run(debug = True)
