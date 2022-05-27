from youtube import db

class Video_info(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    creator = db.Column(db.String, nullable=False)
    video_pic = db.Column(db.String(500), nullable=True)
    link_video = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "creator": self.creator, "video_pic": self.video_pic, "link_video": self.link_video}


db.create_all()