from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# Create Database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialize app with extension
db.init_app(app)


# Create table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # ** is equivalent of spread operator for dict.... * is for a list
        new_book = Book(**{key:value for (key, value) in request.form.items()})
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    book_to_edit = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    if request.method == "POST":
        book_to_edit.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', book=book_to_edit)


@app.route('/delete/<int:id>')
def delete(id):
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

