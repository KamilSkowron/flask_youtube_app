
from youtube import app, render_template, secure_filename, db, request, Response, flash
from youtube.models import Video_info
from youtube.forms import AddNewVideoForm
from youtube.functions import get_picture


@app.route('/')
def home_page():
    videos = Video_info.query.all()
    return render_template('youtube.html',videos=videos)


@app.route('/upload', methods=['POST','GET'])
def add_video():
    form = AddNewVideoForm()

    if form.validate_on_submit():

        pic_name = get_picture("video_pic")

        video = Video_info(title=form.title.data,
                        creator=form.creator.data,
                        video_pic=pic_name,
                        link_video=form.link_video.data)
        
        form.title.data = ""
        form.creator.data =""

        db.session.add(video)
        db.session.commit()
    
        flash("Blog Post Submitted Successfully!")

    return render_template("upload.html",form=form)    

@app.route('/explore', methods=['POST','GET'])
def explore():

    return render_template("explore.html")    
