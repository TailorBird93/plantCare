from plantcare import db



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Plant", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.category_name



class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    watering = db.Column(db.String(50), nullable=False)
    environment = db.Column(db.String(20), nullable=False)
    care_level = db.Column(db.String(20), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"#{self.id} - Plant: {self.name} | Environment: {self.environment} | Watering: {self.watering} | Care Level: {self.care_level}"