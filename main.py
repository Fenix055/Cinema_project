from flask import Flask, render_template

main = Flask(__name__)


@main.route("/")
def index():
    return render_template('index.html')

@main.route("/watch")
def watch():
    return render_template('base_cinema.html')

@main.route("/about")
def about():
    return render_template('about.html')

@main.route("/watch/cinema1")
def cinema1():
    return render_template('cinema1.html')

if __name__ == '__main__':
    main.run(debug=True)