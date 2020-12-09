from flask import Flask
import requests

# Reverse loud text
def v1_reverse_loud_return(data = "Test"):
    return string_uppercase(data[::-1])

# For future work if we wanna replace shoutcloud or handle errors with them
def string_uppercase(text = "Test"):
    return(shoutcloud(text))

def shoutcloud(text = "Test"):
    url = "HTTP://API.SHOUTCLOUD.IO/V1/SHOUT"
    data = {"INPUT": text}
    r = requests.post(url, json=data)
    return r.json()["OUTPUT"]

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! If you tell us something in /v1/
    we will yell it back at you!\n'''
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text + instructions + footer_text))

# add a rule when the page is accessed with data appended to the site.
application.add_url_rule('/v1/<data>', 'shout', (lambda data: v1_reverse_loud_return(data)))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
    #print(v1_reverse_loud_return("Testing stuff"))