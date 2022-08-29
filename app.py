from operator import methodcaller
from flask import make_response,Flask,render_template
from flask import request, jsonify
from jinja2 import Template
from flask import send_file
import io 
from random import randint
text = '''Lorem Ipsum is simply dummy text of\n the printing and typesetting industry. Lorem\n Ipsum has been the industry's standard dummy\n text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing\n software like Aldus PageMaker including versions of Lorem Ipsum.'''
def create_app() : 
    app = Flask(__name__)
    @app.route("/",methods=['GET','POST'])
    def show():
        if(request.method == "GET"):
            name_text = request.args.get("name_text")
            if ( name_text == None) : 
                return render_template("index.html")
            print("Now displaying the text")
            lg_text      = request.args.get("name_text",type=str)
            print("Showing ", lg_text)
            return render_template("processed.html",name_text=lg_text+text)
        return render_template("index.html")
    if __name__ == "__main__":
        app.run()
    return app