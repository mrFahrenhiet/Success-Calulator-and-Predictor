from flask import Flask, request, render_template, jsonify
import joblib

# __name__==__main__
app = Flask(__name__)

lr = joblib.load('./model.pkl')


@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        hours = float(request.form['work'])

        success = str(lr.predict([[1, hours]])[0][0])
        return jsonify({'marks': success})
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
