from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []


@app.get("/")
def build_landing_page():
    title = survey.title
    instructions = survey.instructions
    return render_template("survey_start.html", title=title,
                           instructions=instructions)


@app.post("/begin")
def make_zero_page():
    responses.clear()
    return redirect("/question/0")


@app.get("/question/<question_Id>")
def show_current_question(question_Id):
    question_instance = survey.questions[int(question_Id)]
    #breakpoint()
    print(question_instance)
    
    return render_template("question.html", question=question_instance)


@app.post("/answer")
def get_answer_choices():
    responses.append(request.form["answer"])
    if len(responses)<len(survey.questions):
        next_question = len(responses)
        return redirect(f"/question/{next_question}")
    else:
        completed_responses = []
        for i in enumerate(survey.questions):
            completed_responses.append([i[1], responses[i[0]]])
        return render_template("completion.html", 
            responses=completed_responses)
