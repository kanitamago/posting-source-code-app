from app import db

class Post(db.Model):
    __tablename__ = "code_post_table"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), unique=True)
    image_path = db.Column(db.Text())
    description = db.Column(db.Text())
    url = db.Column(db.Text())
    code = db.Column(db.Text())

    def __init__(self, title=None, image_path=None, description=None, url=None, code=None):
        self.title = title
        self.image_path = image_path
        self.description = description
        self.url = url
        self.code = code
