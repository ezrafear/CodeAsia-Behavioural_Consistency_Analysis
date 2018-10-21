from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class InterviewForm(FlaskForm):
    q1 = TextAreaField('What were the communication challenges on your last project?', validators=[DataRequired()])
    q2 = TextAreaField('What is your communication style with your team?', validators=[DataRequired()])
    q3 = TextAreaField('How do you communicate bad news?', validators=[DataRequired()])

    submit = SubmitField('Submit')