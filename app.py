from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

debug = DebugToolbarExtension(app)

responses = []

@app.get("/")
def build_landing_page():
    title = survey.title
    instructions = survey.instructions
    return render_template("survey_start.html", title=title,
        instructions=instructions)

# @app.post("/question/<question_Id>")
# def show_current_question(question_Id):
#     question_instance = survey.questions[question_Id]

#     return render_template("question.html", question = question_instance)

#@app.post("/begin")
