from youtube import api, Resource,request,db
from youtube.models import Video_info

@api.route('/api/videos')
class Videos(Resource):
    def get(self):
        videos = Video_info.query.all()
        videos_data = [video.to_dict() for video in videos]
        return videos_data, 200
    

    def post(self):
        data = request.get_json()
        title = data.get('title')
        creator = data.get('creator')
        # video_pic = data.get('video_pic')
        link_video = data.get('link_video')

        video = Video_info(title=title,creator=creator,link_video=link_video)
        

        db.session.add(video)
        db.session.commit()

        return video.to_dict(), 201

@api.route('/api/video/<int:video_id>')
class Video(Resource):
    def get(self, video_id):
        video = Video_info.query.get_or_404(video_id)
        return video.to_dict(), 200

    def put(self, video_id):
        video = Video_info.query.get_or_404(video_id)

        data = request.get_json()
        video.title = data.get('title')
        video.creator = data.get('creator')
        video.video_pic = data.get('video_pic')
        video.link_video = data.get('link_video')

        db.session.commit()

        return video.to_dict(), 204

    def delete(self, video_id):
        video = Video_info.query.get_or_404(video_id)
        db.session.delete(video)
        db.session.commit(), 204


    