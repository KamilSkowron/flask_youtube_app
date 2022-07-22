from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, URL


class AddNewVideoForm(FlaskForm):
    title = StringField(label='Title:', validators=[Length(min=2, max=30)])
    category = StringField(label='Category:', validators=[DataRequired()])
    link_video = StringField(label='Link url:', validators=[URL()])
    submit = SubmitField(label='Add new Video!')


class SubmitButtonForm(FlaskForm):
    submit = SubmitField(label='TEST!')
    