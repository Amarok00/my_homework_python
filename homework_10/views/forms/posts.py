from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField(
        label="Title:",
        validators=[DataRequired(), Length(min=3)],
    )
    body = StringField(
        label="text:",
        validators=[DataRequired(), Length(min=3)],
    )
