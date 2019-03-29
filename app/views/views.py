from app import app
from flask import render_template, url_for, redirect, session, request
from app import db
from app.models.post import Post

@app.route("/")
def index():
    posted_items = Post.query.order_by(Post.id.desc()).all()
    return render_template("index.html", posted_items=posted_items)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form["username"] == app.config["USERNAME"]:
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route("/logout", methods=["POST", "GET"])
def logout():
    if request.method == "POST":
        session.pop("logged_in", None)
        return redirect(url_for("index"))
    return redirect(url_for("index"))

@app.route("/post", methods=["POST", "GET"])
def post():
    if request.method == "POST":
        try:
            title = request.form["title"]
            exist_checker = Post.query.filter(Post.title == title).all()
            if not exist_checker:
                image_path = request.form["image_path"]
                description = request.form["description"]
                url = request.form["url"]
                code = request.form["code"]
                if title == "" or image_path == "" or description == "" or url == "" or code == "":
                    return redirect(url_for("index"))
                description = clean_text(description)
                post_item = Post(title=title, image_path=image_path, description=description, url=url, code=code)
                db.session.add(post_item)
                db.session.commit()
                return redirect(url_for("index"))
            else:
                return redirect(url_for("index"))
        except:
            return url_for("index")
    return redirect(url_for("index"))

def clean_text(text):
    text = text.replace("　", " ")
    text = text.split("　")
    text = text[0].replace("\r\n", "<br>")
    return text

@app.route("/detail/<int:id>", methods=["POST", "GET"])
def detail(id):
    post_item = Post.query.get(id)
    return render_template("detail.html", post_item=post_item)

@app.route("/<int:id>/delete", methods=["POST", "GET"])
def delete(id):
    if request.method == "POST":
        post_item = Post.query.get(id)
        db.session.delete(post_item)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return redirect(url_for('index'))

def test_print(title, image_path, description, url, code):
    print("TITLE: ", title)
    print("IMAGE-PATH: ", image_path)
    print("DESCRIPTION: \n", description)
    print("URL: ", url)
    print("CODE: \n", code)
