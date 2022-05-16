
from flask import jsonify
from youtube import app, render_template, secure_filename, db, request, Response, flash
from youtube.models import Video_info
from youtube.forms import AddNewVideoForm, SubmitButtonForm
from youtube.functions import get_picture
from youtube.apis import get_most_popular_videos


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
        form.creator.data = ""

        db.session.add(video)
        db.session.commit()
    
        flash("Blog Post Submitted Successfully!")

    return render_template("upload.html",form=form)    

@app.route('/explore', methods=['GET','POST'])
def explore():

    form = SubmitButtonForm()
    videos = get_most_popular_videos()

    region_list=[{'region':'' , 'display':'All World'}, {'region':'PL', 'display':'Poland'}, {'region':'NZ', 'display':'New Zealand'}, {'region':'GR', 'display':'Germany'}, {'region':'GB', 'display':'Great Britain'}, {'region':'CZ', 'display':'Czech Republic'}, {'region':'RU', 'display':'Russia'}]

    category_list=[{'categoryID': 0, 'display':'All Categories'}, {'categoryID':10, 'display':'Music'}, {'categoryID':20, 'display':'Gaming'}, {'categoryID':23, 'display':'Comedy'}, {'categoryID':27, 'display':'Education'}, {'categoryID':28, 'display':'Science & Technology'}]


    if form.submit:
        region = request.form.get('region')
        category_ID = request.form.get('category')
        videos = get_most_popular_videos(region, category_ID)
        return render_template('explore.html', videos=videos, region_list=region_list, category_list=category_list)


    return render_template('explore.html', videos=videos, region_list=region_list, category_list=category_list)
    #return jsonify(videos) # most_views_response['items']
    #return render_template('explore.html',videos=videos)

