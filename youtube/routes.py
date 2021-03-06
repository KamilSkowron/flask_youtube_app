

from flask import jsonify, redirect, url_for, make_response

from youtube import app, render_template, secure_filename, db, request, Response, flash, api, Resource
from youtube.models import Video_info
from youtube.forms import AddNewVideoForm, SubmitButtonForm
from youtube.functions import get_picture, get_yt_video_id, get_yt_title
from youtube.apis import get_most_popular_videos
from youtube.lists_of_data import region_list, category_list
from urllib.parse import urlparse



@app.route('/home')
def home_page():
    videos = Video_info.query.all()
    return render_template('youtube.html',videos=videos)


@app.route('/upload', methods=['POST','GET'])
def add_video():
    form = AddNewVideoForm()

    if form.is_submitted():

        #pic_name = get_picture("video_pic")
        print(form.link_video.data)
        url_data = get_yt_video_id(form.link_video.data)
        title = get_yt_title(get_yt_video_id(form.link_video.data))


        video = Video_info(title=title,
                        category=form.category.data,
                        link_video=form.link_video.data,
                        video_id=url_data
                        )
        
        form.category.data = ""
        form.link_video.data = ""
        db.session.add(video)
        db.session.commit()
    
        flash("Video Submitted Successfully!")

    return render_template("upload.html",form=form)    

@app.route('/delete_video/<int:id>')
def delete_video(id):
    video = Video_info.query.get_or_404(id)
    db.session.delete(video)
    db.session.commit()
    flash("Video was deleted")
    return redirect(url_for('home_page'))

@app.route('/explore', methods=['GET','POST'])
def explore():

    form = SubmitButtonForm()

    if form.submit:
        region = request.form.get('region')
        category_ID = request.form.get('category')
        videos = get_most_popular_videos(region, category_ID)
        return render_template('explore.html', videos=videos, region_list=region_list, category_list=category_list)

    videos = get_most_popular_videos()
    return render_template('explore.html', videos=videos, region_list=region_list, category_list=category_list)

