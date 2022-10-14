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
    """Render start page with title and instructions"""

    title = survey.title
    instructions = survey.instructions
    return render_template(
        "survey_start.html",
        title=title,
        instructions=instructions
    )


@app.post("/begin")
def make_zero_page():
    """Clears response list and redirects to first question"""

    responses.clear()
    return redirect("/question/0")


@app.get("/question/<int:question_Id>")
def show_current_question(question_Id):
    """Renders and displays current questions"""

    question_instance = survey.questions[question_Id]
    # breakpoint()
    return render_template(
        "question.html",
        question=question_instance
    )


@app.post("/answer")
def get_answer_choices():
    """Appends answer to response and either
    continues to new question or shows results
    of all questions"""

    responses.append(request.form["answer"])
    if len(responses) < len(survey.questions):
        next_question = len(responses)
        return redirect(f"/question/{next_question}")
    else:
        completed_responses = []
        for i, question in enumerate(survey.questions):
            completed_responses.append([question, responses[i]])
        return render_template(
            "completion.html",
            responses=completed_responses
        )
