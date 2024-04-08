from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.json.sort_keys = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    # Select a random cafe
    # random_cafe = db.session.execute(db.select(Cafe).order_by(db.func.random()).limit(1)).scalar_one()
    # random_cafe = db.session.query(Cafe).order_by(db.func.random()).limit(1).scalar()
    random_cafe = Cafe.query.order_by(db.func.random()).first()
    # return jsonify({"cafe": random_cafe.to_dict()})
    return jsonify(cafe = random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    # all_cafes = db.session.query(Cafe).all()
    all_cafes = Cafe.query.all()
    cafes = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes = cafes)


@app.route("/search")
def get_cafes_by_location():
    query_location = request.args.get("location")
    # Caseless partial match of location
    cafes_at_location = Cafe.query.where(Cafe.location.ilike(f"%{query_location}%"))
    cafes = [cafe.to_dict() for cafe in cafes_at_location]
    if cafes:
        return jsonify(cafes = cafes)
    else:
        return jsonify(error={"Not found": f"No cafes found for location, {query_location}"}), 404



# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
