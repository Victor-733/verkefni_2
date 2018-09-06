from bottle import *
from sys import argv

@route('/')
def index():
    return """
    <h1>Rót</h1>
    <h2>verkefni 2</h2>
    <p><a href="/lidur/lidur_a">liður_a</a></p>
    <p><a href="/lidur/lidur_b">liður_b</a></p>
    """
@route('/lidur/lidur_a')
def index_2():
    return """
    <h1>Liður A</h1>
    <h2>verkefni 2</h2>
    <p><a href="/link/link_1">link_1</a></p>
    <p><a href="/link/link_2">link_2</a></p>
    <p><a href="/link/link_3">link_3</a></p>
    """
@route('/lidur/lidur_b')
def index_2():
    return """
    <h1>Liður B</h1>
    <h2>verkefni 2</h2>
    <a href="/myndir?image=1"><img src="/myndir/farquaad.jpg"></img></a>
    <a href="/myndir?image=2"><img src="/myndir/shrek.jpg"></img></a>
    <a href="/myndir?image=3"><img src="/myndir/donkey.jpg"></img></a>
    """

@route('/myndir/<image>')
def static_image(image):
    return static_file(image, root='../myndir')

@route('/myndir')
def page():
    image = request.query.image
    if image == "1":
        return """
        <h2>I am Farquaad!</h2>
        <img src="/myndir/farquaad.jpg">
        <br>
        <hr>
        <a href="/lidur/lidur_b">back</a>
        """
    elif image == "2":
        return """
        <h2>I am Shrek!</h2>
        <img src="/myndir/shrek.jpg"></img>
        <br>
        <hr>
        <a href="/lidur/lidur_b">back</a>
        """
    elif image == "3":
        return """
        <h2>Zoinks!</h2>
        <img src="/myndir/donkey.jpg"></img>
        <br>
        <hr>
        <a href="/lidur/lidur_b">back</a>
        """
    else:
        abort(404)

@route('/link/<link>')
def page(link):
    if link == "link_1":
        return "Welcome to link 1"
    elif link == "link_2":
        return "Welcome to link 2"
    elif link == "link_3":
        return "Welcome to link 3"
    else:
        abort(404)


@error(404)
def villa(error):
    return "<h2 'style=color:blue'>Error 404: See, I pulled a lil sneaky on ya</h2>"

run(host="0.0.0.0", port=argv[1], debug=True)