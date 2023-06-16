from main import db


class Blogs(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    slug = db.Column(db.String(50), nullable=False)
    headline = db.Column(db.String, nullable=False)
    brief = db.Column(db.Text)
    lead = db.Column(db.Text)
    linkBrief = db.Column(db.Text)
    detail01 = db.Column(db.Text)
    detail02 = db.Column(db.Text)
    detail03 = db.Column(db.Text)
    conclusion = db.Column(db.Text)
    quote = db.Column(db.Text)
    photo1 = db.Column(db.Text)
    photo2 = db.Column(db.Text)

    def __repr__(self):
        return f"Blog: {self.id} - {self.slug}"
