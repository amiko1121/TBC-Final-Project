from ext import db, app, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class BaseModels:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.commit()


class Product(db.Model,BaseModels):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.ForeignKey("product_category.id"))
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    img = db.Column(db.String)
    img2 = db.Column(db.String)
    img3 = db.Column(db.String)
    img4 = db.Column(db.String)
    img5 = db.Column(db.String)
    colour=db.Column(db.String)
    coment=db.Column(db.String)
    engine=db.Column(db.Float)
    engine_type=db.Column(db.String)
    year=db.Column(db.Integer)
    transmission=db.Column(db.String)
    mileage=db.Column(db.Integer)
    phonenumber1 = db.Column(db.String)
    interior_colour = db.Column(db.String)
    cilindri = db.Column(db.String)
    category = db.relationship("ProductCategory")


class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String)
    products = db.relationship("Product")


class User(db.Model, BaseModels, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)
    gender = db.Column(db.String)
    birthday = db.Column(db.String)
    country = db.Column(db.String)
    phonenumber = db.Column(db.String)

    def __init__(self, password, username, gender, birthday, country, phonenumber,role="user"):
        self.password = generate_password_hash(password)
        self.username = username
        self.role = role
        self.gender = gender
        self.birthday = birthday
        self.country = country
        self.phonenumber = phonenumber

    def check_password(self,password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        new_user=User(username="amiko",password="12345678",role="admin",gender="კაცი",birthday="2007-03-21", country="Georgia", phonenumber="571246908")
        db.session.add(new_user)

        sedan_category=ProductCategory( id=1,name="სედანი")
        db.session.add(sedan_category)

        jeep_category=ProductCategory(id=2 , name="ჯიპი")
        db.session.add(jeep_category)

        heavy_category=ProductCategory(id=3,name="მძიმე ტექნიკა")
        db.session.add(heavy_category)

        db.session.commit()