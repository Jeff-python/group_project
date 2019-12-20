import os
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("frontend.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    for image in request.files.getlist("file"):
        print(image)
        filename = image.filename
        destination = "/".join([target,filename])
        image.save(destination)
        print(destination)

    return render_template("complete.html")

if __name__ =="__main__":
    app.run(port=5000, debug=True)
