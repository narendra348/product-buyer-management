# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(80))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    description = db.Column(db.Text)

class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))

@app.route('/')
def index():
    products = Product.query.all()
    buyers = Buyer.query.all()
    return render_template('index.html', products=products, buyers=buyers)

@app.route('/add', methods=['POST'])
def add():
    if request.form['record_type'] == 'product':
        new_product = Product(
            name=request.form['name'],
            category=request.form['category'],
            price=request.form['price'],
            quantity=request.form['quantity'],
            description=request.form['description']
        )
        db.session.add(new_product)

    elif request.form['record_type'] == 'buyer':
        new_buyer = Buyer(
            name=request.form['name'],
            email=request.form['email'],
            phone=request.form['phone'],
            address=request.form['address']
        )
        db.session.add(new_buyer)

    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<record_type>/<int:record_id>')
def delete(record_type, record_id):
    if record_type == 'product':
        record = Product.query.get(record_id)
    else:
        record = Buyer.query.get(record_id)

    if record:
        db.session.delete(record)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
