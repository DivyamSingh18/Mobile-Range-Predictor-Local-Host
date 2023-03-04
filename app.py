# importing libraries
import numpy as np
import pickle
from flask import Flask,request,render_template


# Global variables 
app = Flask(__name__)
loadedModel=pickle.load(open('mobile_Range_predict_model.pkl','rb'))
 
#User Defined functions
@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')


@app.route('/predict' ,methods=['POST'])
def predict():
    batteryPower=request.form['battery_power']
    frontCamera=request.form['fc']
    internalMemory=request.form['int_memory']
    mobileWeight=request.form['mobile_wt']
    pixelHeight=request.form['px_height']
    pixelWidth=request.form['px_width']
    ram=request.form['ram']
    talkTime=request.form['talk_time']
    
    a = [batteryPower,frontCamera,internalMemory,mobileWeight,pixelHeight,pixelWidth,ram,talkTime]
    b = np.array(a, dtype=float)  # converting the text data into float

    prediction=loadedModel.predict([b])

    if prediction==[0]:
        prediction="Low Budget Range"
    elif prediction==[1]:
        prediction="Mid Budget Range"
    elif prediction==[2]:
        prediction="High Budget Range"
    elif prediction==[3]:
        prediction="Flagship"
    else:
        prediction="Something Went Wrong"

    # return render_template('index.html',prediction_text='Your Mobile Ranges B/w ${}'.format(prediction))
    return render_template('index.html',output=prediction)

#main Function
if __name__=='__main__':
    app.run(debug=True) 
