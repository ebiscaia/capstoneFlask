from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import BlogForm
import time
import yaml

# Load the config file
with open("./config.yaml") as config_file:
    config = yaml.safe_load(config_file)

app = Flask(__name__)
app.config["SECRET_KEY"] = config.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///capstone.db"
db = SQLAlchemy(app)

blogs = [
    {"title": "Qtile issu", "snippet": "What is a snippet"},
    {
        "title": "Do Russians still support Putin’s war in Ukraine?",
        "snippet": """The happiness of the Russian public fell sharply last year
        after the invasion of Ukraine, according to analysis of their internet
        searches by a team from the University of Cambridge.,""",
    },
]


class Blogs(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    slug = db.Column(db.String(50), nullable=False)
    headline = db.Column(db.String, nullable=False)
    brief = db.Column(db.Text)
    lead = db.Column(db.Text)
    linkBrief = db.Column(db.String(100))
    detail01 = db.Column(db.Text)
    detail02 = db.Column(db.Text)
    detail03 = db.Column(db.Text)
    conclusion = db.Column(db.Text)
    quote = db.Column(db.String(100))
    photo1 = db.Column(db.String(20))
    photo2 = db.Column(db.String(20))

    def __repr__(self):
        return f"Blog: {self.id} - {self.slug}"


@app.route("/")
def home():
    return render_template("home.html", title="Home", blogs=blogs)


@app.route("/about")
def about():
    return render_template("about.html", title="About Page")


@app.route("/create", methods=["get", "post"])
def create():
    form = BlogForm()
    if form.validate_on_submit():
        flash("Blog created successfully!")
        time.sleep(0.5)
        return redirect(url_for("home"))
    return render_template(
        "create.html", legend="New Article", title="Create a New Post", form=BlogForm()
    )


if __name__ == "__main__":
    app.run(debug=True, port=5555)
