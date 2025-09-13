from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index(): 
  page = f"""<html><body>
  <h1>My projects</h1>
  <ul>
  <li><a href="/portfolio">Portfolio</a></li>
  <li><a href="/linktree">Linktree</a></li>
  </ul>
  </body>
  </html>"""
  return page

@app.route('/portfolio')
def portfolio(): 
  page = f"""
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="static/css/portfolio.css">
      <title>My Portfolio</title>
  </head>
  <body>
      <h1>Oscar Ruelas - Portfolio</h1>
      <article class="project">
          <h2>Project - Day 44</h2>
          <p>This project consist in create a bingo card, and display in a pretty print, i like it.</p>
          <a href="https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_44.py"><img src="static/images/day 44.png" width="600px" alt="Image of code"></a>
      </article>
      <article class="project">
          <h2>Project - Day 48</h2>
          <p>I like this project because was the first projects to implement file manipulation, and because the score with 3 letter made me remember the old arcade games.</p>
          <a href="https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_48.py"><img src="static/images/day 48.png" alt="Image of code"></a>
      </article>
      <article class="project">
          <h2>Project - Day 57</h2>
          <p>This project consist in a recursive implementation of the fibonacci method, and i failed to try code this, so its one of my favorites.</p>
          <a href="https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_57.py"><img src="static/images/day 57.png" alt="Image of code"></a>
      </article>
      <article class="project">
          <h2>Project - Day 59</h2>
          <p>This project was to figure out if a word it's a palindrome (forward and backward written the same.)</p>
          <a href="https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_59.py"><img src="static/images/day 59.png" alt="Image of code"></a>
      </article>
      <article class="project">
          <h2>Project - Day 70</h2>
          <p>This project its about a basic login, i like because the enviroment variables was needed in all type of programs</p>
          <a href="https://github.com/oscar-ruinz/replit-100-days-python/blob/main/day_70.py"><img src="static/images/day 70.png" alt="Image of  code"></a>
      </article>
      <br>

  </body>
  </html>
  """
  return page

@app.route('/linktree') 
def home(): 
  page = f"""
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="static/css/linktree.css">
      <title>Fake Linktree</title>
  </head>
  <body>
      <main>
          <div class="container">
              <img src="static/images/avatar.png" alt="">
              <h1>Oscar Ruelas</h1>
              <p>Una terrorífica máquina del chambeo</p>
              <section class="socials">
                  <h2><strong>Socials</strong></h2>
                  <a class="card" href="https://www.linkedin.com/in/oscar-ruinz/">LinkedIn (@oscar-ruinz)</a>
                  <a class="card" href="https://replit.com/@oscarruelasinz1">Replit (@oscarruelasinz1)</a>
                  <a class="card"href="https://github.com/oscar-ruinz">GitHub (@oscar-ruinz)</a>
              </section>
          </div>
      </main>
  </body>
  </html>
  """

  return page
