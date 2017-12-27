from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % (self.username)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120))

    def __repr__(self):
        return '<Admin %r>' % (self.username)

class County(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    headline = db.Column(db.String(1000))
    content = db.Column(db.String(10000))

    def __repr__(self):
        return '<County %r>' % (self.name)


class SuccessStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    video_link = db.Column(db.String(120))
    image = db.Column(db.String(120))
    story = db.Column(db.String(1000))
    county = db.Column(db.Integer, db.ForeignKey('county.id'))

    def __repr__(self):
        return '<SuccessStory %r>' % (self.first_name + ' ' + self.last_name)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(120))
    county = db.Column(db.Integer, db.ForeignKey('county.id'))
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)

    def __repr__(self):
        return '<Location %r>' % (self.name)
