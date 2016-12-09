from flask import Flask, render_template, request
from inverse_via_lu import Matrix, WrongSize, NonInvertibleMatrix
app = Flask(__name__, )

def to_matrix(s):
    matrix = []
    lines = s.split('\n')
    for l in lines:
        matrix.append(list(map(float, l.split())))

    return matrix

def matrix_to_string(m):
    new_matrix = '$\\left(\\begin{matrix}\n'
    for el in range(len(m)):
        answer = ''
        for ele in range(len(m[el])):
            if m[el][ele] == int(m[el][ele]):
                answer += str(m[el][ele])[:-2]
            else:
                answer += str(round(m[el][ele], 4))

            if ele != (len(m[el])-1):
                answer += '&'

            else:
                answer += '\\\\\n'

        new_matrix += answer
    new_matrix += '\\end{matrix}\\right)$\n'
    return new_matrix

@app.route('/', methods=["GET", "POST"])
def get_index():
    try:
        if request.method == "POST":
            matrix = request.form['matrix']
            print(to_matrix(matrix))
            new_matrix = Matrix(to_matrix(matrix))
            new_matrix = new_matrix.matrix_inverse()
            new_matrix = matrix_to_string(new_matrix)
            return render_template('matrix_index.html', matrix=matrix, new_matrix=new_matrix)
        else:
            return render_template('matrix_index.html')
    except WrongSize:
        return render_template('matrix_index.html', error_message="Matrix should be square")
    except NonInvertibleMatrix:
        return render_template('matrix_index.html', error_message="It is a singular matrix")

if __name__ == "__main__":
    app.run(debug = True)
