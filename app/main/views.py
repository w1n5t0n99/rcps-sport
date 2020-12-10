from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import NameForm
from ..models import Sport


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           current_date=datetime.utcnow())


@main.route('/sports')
def sports():
    s = Sport.query.all()
    return render_template('sports.html', sports=s)


@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)