from flask import Blueprint ,render_template ,request

views = Blueprint('views',__name__)

@views.route('/')
def hello():
    return render_template('home.html')

@views.route('/about')
def about():
    menu = 'About Us'
    return render_template('about.html',menu=menu)

@views.route('/services')
def services():
    menu = 'Services'
    return render_template('services.html',menu=menu)

@views.route('/cases')
def cases():
    menu = 'Cases Study'
    return render_template('cases.html',menu=menu)

@views.route('/blog')
def blog():
    menu = 'Blog'
    return render_template('blog.html',menu=menu)

@views.route('/contact')
def contact():
    menu = 'Contact'
    return render_template('contact.html',menu=menu)