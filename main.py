
from flask import Flask,render_template
from  GUI import GUIWindow


gui= GUIWindow("MyApp")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ =="__main__":
    gui.run(app)
