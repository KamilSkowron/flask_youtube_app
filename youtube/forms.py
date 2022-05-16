from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, URL


class AddNewVideoForm(FlaskForm):
    title = StringField(label='Tytuł:', validators=[DataRequired(), Length(min=2, max=30)])
    creator = StringField(label='Autor:', validators=[DataRequired()])
    video_pic = FileField ("Video Pic:")
    link_video = StringField(label='Link to youtube file:', validators=[URL()])
    submit = SubmitField(label='Add new Video!')


class SubmitButtonForm(FlaskForm):
    submit = SubmitField(label='TEST!')
    