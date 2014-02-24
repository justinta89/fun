from flask import Blueprint, render_template, redirect
default = Blueprint('default', __name__)
admin = Blueprint('admin', __name__)

LST = ["index",
       "resume",
       "security"]

SOCIALLIST = { "facebook": "http://www.facebook.com/cowpunk1",
               "twitter": "http://www.twitter.com/cowpunk1",
               "github": "http://www.github.com/justinta89",
               "linkedin": "http://www.linkedin.com/profile/view?id=143851789",
               "google-plus": "https://plus.google.com/112956732382970385846/posts" }


@default.route('/')
def index():
    return render_template('index.html', LST = LST, SOCIALLIST = SOCIALLIST)

@default.route('/resume')
def resume():
    return render_template('resume.html', LST = LST, SOCIALLIST = SOCIALLIST)

@default.route('/security')
def security():
    return render_template('security.html', LST = LST, SOCIALLIST = SOCIALLIST)

@admin.route('/admin')
def adminPage():
    return render_template('admin.html')