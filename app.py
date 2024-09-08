from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Define the form class
class ResumeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    aboutme = TextAreaField('About Me', validators=[DataRequired()])
    skills = TextAreaField('Skills', validators=[DataRequired()])
    languages = TextAreaField('Languages', validators=[DataRequired()])
    education = TextAreaField('Education', validators=[DataRequired()])
    experience = TextAreaField('Experience', validators=[DataRequired()])
    submit = SubmitField('Generate Resume')

# Route for the main form page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = ResumeForm()
    if form.validate_on_submit():
        return render_template('resume.html', data=form.data)
    return render_template('index.html', form=form)

# No need for a separate /resume route; the form submission renders the resume template directly
if __name__ == '__main__':
    app.run(debug=True)
