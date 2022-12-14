"""Logged-in page routes."""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user


# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))


@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main_bp.route('/recommands')
@login_required
def recommands():
    return render_template('recommands.html')


@main_bp.route('/post')
@login_required
def post():
    return render_template('post.html')


@main_bp.route('/fav_receipies')
@login_required
def fav_receipies():
    return render_template('fav_receipies.html')


@main_bp.route('/profile')
@login_required
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
