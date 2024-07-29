from flask import render_template, request, redirect, url_for, flash
from plantcare import app, db
from plantcare.models import Category, Plant

@app.route("/")
def home():
    plants = list(Plant.query.order_by(Plant.id).all())
    return render_template("plants.html", plants=plants)

@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category_name = request.form.get("category_name")
        
        # Checking if the category already exists
        existing_category = Category.query.filter_by(category_name=category_name).first()
        
        if existing_category:
            flash(f"Category '{category_name}' already exists.", "warning")
            return redirect(url_for("add_category"))
        
        # Adding new one
        new_category = Category(category_name=category_name)
        db.session.add(new_category)
        db.session.commit()
        flash(f"Category '{category_name}' added successfully!", "success")
        return redirect(url_for("categories"))
    
    return render_template("add_category.html")

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category= Category.query.get_or_404(category_id)
    if request.method=="POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)

@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))

@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        plant = Plant(
            name = request.form.get("plant_name"), 
            watering = request.form.get("watering"), 
            environment = request.form.get("environment"), 
            care_level = request.form.get("care_level"),
            category_id = request.form.get("category_id")
        )
        db.session.add(plant)
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("add_plant.html", categories=categories)