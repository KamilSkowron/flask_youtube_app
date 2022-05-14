from PIL import Image
import uuid as uuid
import os
from youtube import app, render_template, secure_filename, db, request, Response, flash
from youtube.models import Video_info
from youtube.forms import AddNewVideoForm


@app.route('/youtube')
def home_page():
    videos = Video_info.query.all()
    return render_template('youtube.html',videos=videos)


@app.route('/upload', methods=['POST','GET'])
def add_video():
    form = AddNewVideoForm()

    if form.validate_on_submit():

        video_pic_file = request.files['video_pic']
        i = Image.open(video_pic_file)
        out = i.resize((1280,720))
        pic_filename = secure_filename(video_pic_file.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        out.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))

        video = Video_info(title=form.title.data,
                        creator=form.creator.data,
                        video_pic=pic_name)
        
        form.title.data = ""
        form.creator.data =""

        db.session.add(video)
        db.session.commit()
    
        flash("Blog Post Submitted Successfully!")

    return render_template("upload.html",form=form)    
    


