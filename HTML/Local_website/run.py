from bottle import route, get, run, post, request, response, redirect, static_file
#-----------------------------------------------------------------------------
# This class loads html files from the "template" directory and formats them using Python.
# If you are unsure how this is working, just
class FrameEngine:
    def __init__(this,
        template_path="templates/",
        template_extension=".html",
        **kwargs):
        this.template_path = template_path
        this.template_extension = template_extension
        this.global_renders = kwargs

    def load_template(this, filename):
        path = this.template_path + filename + this.template_extension
        file = open(path, 'r')
        text = ""
        for line in file:
            text+= line
        file.close()
        return text

    def simple_render(this, template, **kwargs):
        '''
        Commented Out for Maths to work. Doesnt seem to impact anything atm
        '''
        #template = template.format(**kwargs)
        return  template

    def render(this, template, **kwargs):
        keys = this.global_renders.copy() #Not the best way to do this, but backwards compatible from PEP448, in Python 3.5+ use keys = {**this.global_renters, **kwargs}
        keys.update(kwargs)
        template = this.simple_render(template, **keys)
        return template

    def load_and_render(this, filename, header="header", tailer="tailer", **kwargs):
        template = this.load_template(filename)
        rendered_template = this.render(template, **kwargs)
        rendered_template = this.load_template(header) + rendered_template
        rendered_template = rendered_template + this.load_template(tailer)
        return rendered_template

#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------

# Allow image loading
@route('/img/<picture>')
def serve_pictures(picture):
    return static_file(picture, root='img/')

# Allow CSS
@route('/css/<css>')
def serve_css(css):
    return static_file(css, root='css/')

# Allow javascript
@route('/js/<js>')
def serve_js(js):
    return static_file(js, root='js/')

#-----------------------------------------------------------------------------
@route('/')
@route('/home')

@get("/home")
def home():
    return fEngine.load_and_render("home")

@get("/about")
def about():
    return fEngine.load_and_render("about")

@get("/stats")
def stats():
    return fEngine.load_and_render("stats")

@get("/football")
def football():
    return fEngine.load_and_render("football")

@get("/other")
def other():
    return fEngine.load_and_render("other")

@get("/stats_y1s2")
def stats_y1s2():
    return fEngine.load_and_render("stats_y1s2")

@get("/stats_y2s1")
def stats_library_book():
    return fEngine.load_and_render("stats_y2s1")

@get("/christian")
def christian():
    return fEngine.load_and_render("christian")

@get("/analysis")
def analysis():
    return fEngine.load_and_render("analysis")

fEngine = FrameEngine()
run(host='localhost', port=8080, debug=True)
