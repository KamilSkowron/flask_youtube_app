from youtube import db

class Video_info(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    link_video = db.Column(db.String(500), nullable=False)
    video_id = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {"id": self.id, 
                "title": self.title, 
                "category": self.category, 
                "description": self.description, 
                "link_video": self.link_video, 
                "video_id":self.video_id}



db.create_all()