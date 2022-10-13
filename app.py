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


@app.post("/begin")
def make_zero_page():

    return render_template("question.html", )


@app.get("/question/<question_Id>")
def show_current_question(question_Id):
    question_instance = survey.questions[int(question_Id)]
    breakpoint()
    print(question_instance)
    return render_template("question.html", question=question_instance)


@app.post("/answer")
def get_answer_choices():
    responses.append(request.form["answer"])
    print(responses)

    return redirect("/question/1")


# @app.post("/post-example")
# def post_example():
#     """An example of good POST handling."""

#     isbn = request.form["isbn"]

#     if isbn in VALID_ISBNS:
#         print(f"\n\nBuying Book: {isbn}\n\n")

#         # flash message: we'll talk about this soon
#         # flash(f"Book {isbn} bought!")

#         return redirect("/thanks")
#     else:
#         error = "Invalid isbn"
#         return render_template("post-form.html", isbn=isbn, error=error)