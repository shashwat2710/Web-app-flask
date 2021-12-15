from re import TEMPLATE
from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Shashwat Ahuja',
        'title': 'Blog Post 1',
        'Content': 'First Post Content',
        'date_posted': 'December 15 2021'
    },
    {
        'author': 'Sakshi Ahuja',
        'title': 'Blog Post 2',
        'Content': 'Second Post Content',
        'date_posted': 'December 16 2021'
    }
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)