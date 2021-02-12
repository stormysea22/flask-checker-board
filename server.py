from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/play/<num>/<color>')
# def level_3(num, color):
    # # return render_template('index.html', num_times=int(num), color_change=color)

@app.route('/')
def checker_board_1():
    return render_template('index.html', num_x=int(8), num_y=int(8), color1="red", color2="blue")

@app.route('/<num_x>')
def checker_board_2(num_x):
    return render_template('index.html', num_x=int(num_x), num_y=int(8), color1="red", color2="blue")

@app.route('/<num_x>/<num_y>')
def checker_board_3(num_x, num_y):
    return render_template('index.html', num_x=int(num_x), num_y=int(num_y), color1="red", color2="blue")

@app.route('/<num_x>/<num_y>/<color1>/<color2>')
def checker_board_4(num_x, num_y, color1, color2):
    return render_template('index.html', num_x=int(num_x), num_y=int(num_y), color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)
