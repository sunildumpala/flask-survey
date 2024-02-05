from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.config['SECRET_KEY']="garfield"
debug = DebugToolbarExtension(app)
responses = []

@app.route('/')
def show_home():
  title = surveys.get('satisfaction').title
  instructions = surveys.get('satisfaction').instructions
  return render_template('welcome.html', title=title, instructions=instructions )

@app.route('/thanks')
def say_thanks():
  return render_template('thanks.html')

@app.route('/questions/<number>')
def ask_questions(number):
  if (len(surveys.get('satisfaction').questions) > int(number)):
    quest = surveys.get('satisfaction').questions[int(number)]
    question = quest.question
    choices = quest.choices  
    return render_template('question.html', question = question, choices = choices)
  else:
    return render_template('thanks.html')