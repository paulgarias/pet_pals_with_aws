def create_Pet_class(db):
    class Pet(db.Model):
        __tablename__ = 'pets'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64))
        lat = db.Column(db.Float)
        lon = db.Column(db.Float)

        def __repr__(self):
            return '<Pet %r>' % (self.name)
    return Pet

def create_Owner_class(db):
    class Owner(db.Model):
        __tablename__ = 'owner'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64))
        lat = db.Column(db.Float)
        lon = db.Column(db.Float)
        pet_name = db.Column(db.String(64))

        def __repr__(self):
            return '<Owner %r, Pet %r>' % (self.name, self.pet_name) 
    return Owner
