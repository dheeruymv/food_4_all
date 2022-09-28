from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommands')
def recommands():
    return render_template('recommands.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/fav_receipies')
def fav_receipies():
    return render_template('fav_receipies.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

# @app.route('/contact', methods = ['GET','POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         message = request.form['message']
#         return redirect(url_for('profile.html'))
#     else:
#         return render_template('post.html')

# @app.route('/database', methods=['GET', 'POST']) 
# def database():
#     query = []
#     for i in session.query(models.BlogPost):
#         query.append((i.title, i.post, i.date))
#     return render_template('database.html', query = query)