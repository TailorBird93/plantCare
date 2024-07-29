from plantcare import db



class PlantCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_category_name = db.Column(db.String(25),unique=True, nullable=False)
    def __repr__(self):
        return self.plant_category_name



class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    watering = db.Column(db.String(50), nullable=False)
    environment = db.Column(db.String(20), nullable=False)
    care_level = db.Column(db.String(20), nullable=False)
    plant_category_id = db.Column(db.Integer, db.ForeignKey("plantcategory.id"), nullable=False)

    def __repr__(self):
        return self.name