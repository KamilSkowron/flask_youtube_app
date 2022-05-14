from youtube import db

class Video_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    creator = db.Column(db.String, nullable=False)
    video_pic = db.Column(db.String(500), nullable=True)

db.create_all()