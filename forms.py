from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename


class UploadForm(FlaskForm):
    csv_file = FileField('Select a file to upload:', validators=[FileRequired()])
    submit = SubmitField()
