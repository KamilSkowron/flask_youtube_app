from PIL import Image
import uuid as uuid
import os
from youtube import request, secure_filename, app


def get_picture(file):
    video_pic_file = request.files[file]
    i = Image.open(video_pic_file)
    out = i.resize((1280,720))
    pic_filename = secure_filename(video_pic_file.filename)
    pic_name = str(uuid.uuid1()) + "_" + pic_filename
    out.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
    return pic_name

def convert_views_to_readable(views):
	views = views[::-1]
	subList = [views[n:n+3] for n in range(0,len(views), 3)][::-1]
	Z = [i[::-1] for i in subList]
	views_with_dots = ".".join(Z)
	return views_with_dots
