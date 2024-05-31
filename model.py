from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    screenname = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    save_files = db.relationship("SaveFile", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class SaveFile(db.Model):
    """A save file belonging to a user"""

    __tablename__ = "saves"

    save_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    farm_name = db.Column(db.String)

    user = db.relationship("User", back_populates="save_files")
    items = db.relationship("Item", secondary="save_items", back_populates="save_files")

    def __repr__(self):
        return f"<SaveFile farm={self.farm_name}>"

class Item(db.Model):
    """An item from the game Stardew Valley"""

    __tablename__ = "items"

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_name = db.Column(db.String)
    bundle_name = db.Column(db.String)
    seasons_available = db.Column(db.String) #spring, summer, fall, winter, all
    locations_available = db.Column(db.String)
    conditions_available = db.Column(db.String)

    save_files = db.relationship("SaveFile", secondary="save_items", back_populates="items")
    
    def __repr__(self):
        return f'<Item item_name={self.item_name}>'


class SaveItem(db.Model):
    """Connects a save file to the items relevant to it"""

    __tablename__ = "save_items"

    save_item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    save_id = db.Column(db.Integer, db.ForeignKey('saves.save_id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'), nullable=False)
    found_status = db.Column(db.String)


def connect_to_db(flask_app, db_uri="postgresql:///stardew", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)