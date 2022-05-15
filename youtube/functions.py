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


