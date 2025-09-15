from flask import Flask, redirect

app = Flask(__name__)

reflections = {
    "70": {
        "reflection": "good project with a environment variables",
        "link": "https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_70.py"
    },
    "71": {
        "reflection": "cool project with a login and hash password",
        "link": "https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_71.py"
    },
    "72": {
        "reflection": "a private diary with a login",
        "link": "https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_72.py"
    },
    "73": {
        "reflection": "the begin of html journey, my first projects portfolio",
        "link": "https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_73"
    },
    "74": {
        "reflection": "day 73 but with some cool styles adding css",
        "link": "https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_74"
    },
    "75": {
        "reflection": "a link tree copy",
        "link": "https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_75"
    },
    "76": {
        "reflection": "introduction to flask",
        "link": "https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_76"
    },
    "77": {
        "reflection": "introduction to template files",
        "link": "https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_77"
    }
}

@app.route('/<pageNumber>')

def index(pageNumber):
    link = reflections[pageNumber]["link"]
    reflection = reflections[pageNumber]["reflection"]

    page = ""
    f = open("templates/reflection.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{{day}}",pageNumber)
    page = page.replace("{{link}}",link)
    page = page.replace("{{reflection}}",reflection)
    return page

app.run(host='0.0.0.0', port=81)