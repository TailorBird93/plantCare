from flask import render_template, request, redirect, url_for, flash
from plantcare import app, db
from plantcare.models import PlantCategory, Plant

@app.route("/")
def home():
    return render_template("plants.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")

# @app.route("/add_category", methods=["GET","POST"])
# def add_category():
#     if request.method == "POST":
#         category = PlantCategory(plant_category_name=request.form.get("category_name"))
#         db.session.add(category)
#         db.session.commit()
#         return redirect(url_for("categories"))
#     return render_template("add_category.html")

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category_name = request.form.get("category_name")
        
        # Checking if the category already exists
        existing_category = PlantCategory.query.filter_by(plant_category_name=category_name).first()
        
        if existing_category:
            flash(f"Category '{category_name}' already exists.", "warning")
            return redirect(url_for("add_category"))
        
        # Adding new one
        new_category = PlantCategory(plant_category_name=category_name)
        db.session.add(new_category)
        db.session.commit()
        flash(f"Category '{category_name}' added successfully!", "success")
        return redirect(url_for("categories"))
    
    return render_template("add_category.html")