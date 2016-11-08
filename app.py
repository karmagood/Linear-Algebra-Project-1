from flask import Flask, render_template, request
from inverse_via_lu import Matrix
app = Flask(__name__, )

def to_matrix(s):
    matrix = []
    lines = s.split('\n')
    for l in lines:
        matrix.append(list(map(float, l.split())))

    return matrix

def matrix_to_sring(m):
    pass


@app.route('/', methods=["GET", "POST"])
def get_index():
    if request.method == "POST":
        matrix = request.form['matrix']
        print(to_matrix(matrix))
        new_matrix = Matrix(to_matrix(matrix))
        new_matrix = new_matrix.matrix_inverse()
        return render_template('index.html', matrix=matrix, new_matrix=new_matrix)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)