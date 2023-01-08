from flask import Flask, jsonify, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }




@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(random_cafe.to_dict())


@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    

    
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search():
    location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter(Cafe.location == location).all()
    if len(cafes) > 1:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
        

@app.route("/add",methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/update-price/<cafe_id>",methods=["PATCH"])
def update(cafe_id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffe_price = new_price
        return jsonify(respose={"Sucesess":"Task failed sucessfully"})
    else:
        return jsonify(response={"error":"you ok bro?"})


@app.route("/report-closed/<cafe_id>",methods=["DELETE"])
def db_delete(cafe_id):
    secret_api_key = "I-love-pizza"
    apiKey = request.args.get('api-key')
    cafe = Cafe.query.get(cafe_id)

    if apiKey == secret_api_key:
        if cafe:
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(response={"Sucsess":"DONE gone forever"})
        else:
            return jsonify(response={"Lol":"No cafe found"})
        
    return jsonify(response={"Failed":"WRONG API KEY"})



## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
