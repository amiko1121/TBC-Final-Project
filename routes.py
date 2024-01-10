from flask import Flask, render_template, redirect
from flask_login import login_user, logout_user, login_required, current_user
from forms import AddProductForm, RegisterForm, LoginForm
from os import path
from models import Product, ProductCategory, User
from ext import app, db

library = "Flask 2,0"


# products = [{"title": "Toyota Camry 2014", "price": 11500, "img": "camry.jpg", "id": 0},
#           {"title": "Toyota Camry 2012", "price": 11500, "img": "camry.jpg", "id": 1},
#           {"title": "Toyota Camry 2013", "price": 11500, "img": "camry.jpg", "id": 2},
#         {"title": "Toyota Camry 2015", "price": 11500, "img": "camry.jpg", "id": 3},
#         {"title": "BMW x5", "price": 11500, "img": "camry.jpg", "id": 4}

#      ]


@app.route("/")
def index():
    products = Product.query.limit(12).all()
    return render_template("index.html", products=products)



@app.route("/product/<int:product_id>")
def view_product(product_id):
    chosen_product = Product.query.get(product_id)
    return render_template("product.html", product=chosen_product)


@app.route("/delete_product/<int:product_id>", methods=["POST", "GET"])
@login_required
def delete_product(product_id):
    if current_user.role != "admin":
        return redirect("/")
    chosen_product = Product.query.get(product_id)
    db.session.delete(chosen_product)
    db.session.commit()
    return redirect("/")


@app.route("/category/<int:category_id>")
def category(category_id):
    products = Product.query.filter(Product.category_id == category_id).all()
    return render_template("category.html", products=products)


@app.route("/addproduct", methods=["POST", "GET"])
@login_required
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data, price=form.price.data, img=form.img.data.filename,
                              img2=form.img2.data.filename, img3=form.img3.data.filename, img4=form.img4.data.filename,
                              img5=form.img5.data.filename, engine=form.engine.data, coment=form.coment.data,
                              phonenumber1=form.phonenumber1.data, interior_colour=form.interior_colour.data,
                              cilindri=form.cilindri.data,
                              category_id=form.category.data, year=form.year.data,
                              colour=form.colour.data, mileage=form.mileage.data, engine_type=form.engine_type.data,
                              transmission=form.transmission.data)

        db.session.add(new_product)

        file_directory = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_directory)
        file_directory = path.join(app.root_path, "static", form.img2.data.filename)
        form.img2.data.save(file_directory)
        file_directory = path.join(app.root_path, "static", form.img3.data.filename)
        form.img3.data.save(file_directory)
        file_directory = path.join(app.root_path, "static", form.img4.data.filename)
        form.img4.data.save(file_directory)
        file_directory = path.join(app.root_path, "static", form.img5.data.filename)
        form.img5.data.save(file_directory)
        db.session.commit()
        return redirect("/")
    return render_template("add_product.html", form=form)





















@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data, gender=form.gender.data,
                        birthday=form.birthday.data, country=form.country.data, phonenumber=form.phonenumber.data,
                        role="user")
        new_user.create()
        return redirect("/login")
    return render_template("register.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/search/<string:name>")
def search(name):
    products = Product.query.filter(Product.name.ilike(f"%{name}%")).all()

    return render_template("search.html", products=products)
