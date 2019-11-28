#!/usr/bin/sh python
# coding: utf-8

'''
@Author: Senkita
'''

from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import abort
from flask import request
from flask import session
from flask import flash
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os
import config
from datetime import datetime
import socket

app = Flask(
    __name__,
    template_folder='/home/用户名/.Handover Manual/templates/',
    static_folder='/home/用户名/.Handover Manual/static/'
    )

app.config.from_object(config)
app.config.update(SECRET_KEY=os.urandom(24))

db = SQLAlchemy(app)

class VerificationForm(FlaskForm):
    password = PasswordField(label=u'密码：', validators=[DataRequired()])
    submit = SubmitField(label=u'提交')

class WriterForm(FlaskForm):
    level = SelectField(
        label=u'级别：',
        choices=[
            (1, u'紧急'),
            (2, u'重要'),
            (3, u'一般')
        ],
        default=2,
        coerce=int,
        validators=[DataRequired()]
    )
    contents = TextAreaField(label=u'内容：', validators=[DataRequired()])
    submit = SubmitField(label=u'提交')

class Contents(db.Model):
    __tablename__ = 'contents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String(2))
    contents = db.Column(db.String(512), unique=True)
    record_time = db.Column(db.DateTime, default=datetime.now, unique=True)

@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/operation/', methods=['GET'])
def operation():
    return render_template('operation.html')

@app.route('/maternal_baby/', methods=['GET'])
def maternal_baby():
    return render_template('maternal_baby.html')

@app.route('/apparel/', methods=['GET'])
def apparel():
    return render_template('apparel.html')

@app.route('/toy/', methods=['GET'])
def toy():
    return render_template('toy.html')

@app.route('/account/', methods=['GET', 'POST'])
def account():
    if request.method == 'GET':
        verification_form = VerificationForm()
        return render_template('verification.html', verification_form=verification_form)
    else:
        if request.form.get('password') == '123321':
            session['password'] = '123321'
            return render_template('account.html', password=session.get('password'))
        else:
            return redirect(error_404)

@app.route('/configuration/', methods=['GET'])
def configuration():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip_address = s.getsockname()[0]
    s.close()
    return render_template('configuration.html', ip=ip_address)

@app.route('/unfinished_business/', methods=['GET', 'POST'])
def unfinished_business():
    if request.method == 'GET':
        writer_form = WriterForm()
        contents = Contents.query.all()
        return render_template('unfinished_business.html', writer_form=writer_form, contents=contents)
    else:
        if request.form.get('level') == '1':
            level = '紧急'
        elif request.form.get('level') == '2':
            level = '重要'
        else:
            level = '一般'
        contents = request.form.get('contents')
        try:
            new_record = Contents(
                level=level,
                contents=contents
            )
            db.session.add(new_record)
            db.session.commit()
        except:
            flash('添加失败！')
            db.session.rollback()
        finally:
            return redirect(url_for('unfinished_business'))

@app.route('/delete_event/<event_id>/', methods=['GET'])
def delete_event(event_id):
    try:
        Contents.query.filter_by(id=event_id).delete()
        db.session.commit()
    except:
        flash('删除失败！')
        db.session.rollback()
    finally:
        return redirect(url_for('unfinished_business'))

if __name__ == '__main__':
    db.create_all()
    app.run(port=8080)
