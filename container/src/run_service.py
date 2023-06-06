
from flask import Flask, request, render_template
from detoxify import Detoxify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/results',methods=['POST'])
def get_predict():
    text = request.get_json(force=True)
    print(text['text'])
    results = Detoxify('original').predict(text['text'])
    return str(results)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')


# curl -i -X POST -H 'Conten"application/json' -d '{"text": "You are moroon"}' http://127.0.0.1:5000/results