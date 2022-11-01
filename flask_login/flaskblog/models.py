from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    phone_num = db.Column(db.INT())
    address_l1 = db.Column(db.String(240))
    address_l2 = db.Column(db.String(240))
    zip_code = db.Column(db.String(6))
    country = db.Column(db.String(60))
    region = db.Column(db.String(60))
    dietary_restrictions = db.Column(db.String())
    ingredients_restrictions = db.Column(db.String())
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text)
    serving_size = db.Column(db.Text)
    servings = db.Column(db.Text)
    ingredients_raw_str = db.Column(db.Text)
    steps = db.Column(db.Text)
    key_words = db.Column(db.Text)
    meals = db.Column(db.Text)
    prepare_time = db.Column(db.Text)
    food_types = db.Column(db.Text)
    ingredients_choice = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredients_raw_str = db.Column(db.Text)
    zipcode = db.Column(db.String(6), db.ForeignKey('user.zip_code'), nullable=False)