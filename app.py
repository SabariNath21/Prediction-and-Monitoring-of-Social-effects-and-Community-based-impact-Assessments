from flask import Flask, render_template

app=Flask(__name__)
@app.route("/")
def dash():
    return render_template('home.html',msg=" ")
@app.route('/descrip')
def descrip():
    return render_template("descrip.html",msg=" ")
@app.route('/predict')
def predict():
    return render_template("predict.html",msg=" ")
@app.route('/visual')
def visual():
    return render_template("visual.html",msg=" ")
if __name__=='__main__':
    app.run(debug=True,port=5566)