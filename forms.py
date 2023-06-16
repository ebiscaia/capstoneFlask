from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class BlogForm(FlaskForm):
    headline = StringField("Headline*", validators=[DataRequired(), Length(min=2)])
    lead = TextAreaField("Lead")
    # After implementing the text editor, create two versions os the lead
    # sanitized with and without html
    brief = TextAreaField("Brief")
    linkBrief = StringField("LinkBrief")
    detail01 = TextAreaField("Detail01")
    detail02 = TextAreaField("Detail02")
    detail03 = TextAreaField("Detail03")
    conclusion = TextAreaField("Conclusion")
    quote = StringField("Highlighted Quote")
    photo1 = FileField("Main Photo", validators=[FileAllowed(["jpg", "jpeg", "png"])])
    photo2 = FileField("Photo", validators=[FileAllowed(["jpg", "jpeg", "png"])])
    submit = SubmitField("Submit")

    # Brief, details and conclusion need a sanitized version
    # after making the forms using the text editor
    # Also create a function to slugfy the headline
