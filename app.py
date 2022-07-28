from crypt import methods
import sqlite3
from turtle import title
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

def db_connect():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/select/")
def select():
    conn = db_connect()
    todo = conn.execute('SELECT * FROM todo').fetchall()
    conn.close()
    return render_template('select.html', todo=todo)

@app.route('/create/', methods = ('GET', 'POST'))
def create():

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = db_connect()
            conn.execute(f'INSERT INTO todo (title, content) VALUES ("{title}", "{content}")')
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/delete/', methods = ('GET', 'POST'))
def delete():

    if request.method == 'POST':
        
        titledel = request.form['titledel']

        conn = db_connect()
        conn.execute(f'DELETE FROM todo WHERE title="{titledel}";')
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('delete.html')

@app.route('/update/', methods = ('GET', 'POST'))
def update():

    if request.method == 'POST':

        titletoup = request.form['titletoup']
        titleup = request.form['titleup']
        contentup = request.form['contentup']

        conn = db_connect()
        conn.execute(f'UPDATE todo SET title="{titleup}", content="{contentup}" WHERE title="{titletoup}";')
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('update.html')
