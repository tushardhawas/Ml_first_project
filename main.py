import pickle
from flask import Flask, request , render_template




app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
#url
@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/predict',methods = ['POST','GET'])
def predict():
    prediction = model.predict([[float(request.form.get('temperature'))]])
    if(0>prediction): return render_template('index.html',prediction_text=f'Enter Valid Inupt')
    output = round(prediction [0],2)
    print(output)
    return render_template('index.html', prediction_text=f'Total revenue generated is $ {output}/-')

if __name__ == '__main__':
    app.run(debug= True)