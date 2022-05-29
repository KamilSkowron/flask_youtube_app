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


class TimeVideo():
    def __init__(self, time):
        self.time = time

    def __extract_data(self):
        res = {}
        data = ""
        for i in self.time:
            if i in 'HMS':
                if i == 'S' and len(data) != 2: data = "0" + data
                res[i], data = data, ""
            else:
                data += i
        return res


    def repr(self):
        dict_time = self.__extract_data()
        if "H" in dict_time and "M" in dict_time and "S" in dict_time: return f'{dict_time["H"]}:{dict_time["M"]}:{dict_time["S"]}'
        elif "H" in dict_time and "S" in dict_time: return f'{dict_time["H"]}:00:{dict_time["S"]}'
        elif "H" in dict_time and "M" in dict_time: return f'{dict_time["H"]}:{dict_time["M"]}:00'
        elif "H" in dict_time: return f'{dict_time["H"]}:00:00'
        elif "M" in dict_time and "S" in dict_time: return f'{dict_time["M"]}:{dict_time["S"]}'
        elif "M" in dict_time: return f'{dict_time["M"]}:00'
        elif "S" in dict_time: return f'00:{dict_time["S"]}'