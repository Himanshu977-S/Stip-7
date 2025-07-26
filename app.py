# from flask import Flask , render_template , request , url_for
# app=Flask(__name__)

# @app.route("/")
# def home():
#      return"hello extolling your efforts "

# @app.route('/contact')
# def contact():
#      return render_template('contact.html')

# @app.route('/about')
# def about():
#      return render_template('about.html')

# @app.route('/project', method = ["POST", "GET"])
# def predict():
#      if request.method=='POST':
#           brand_name=request.form['brand_name']
#           owner=request.form['owner']
#           age=request.form['age']
#           power=request.form['power']
#           kms_driven=request.form['kms_driven']
#           print("My Data >>>>>>>", brand_name, age, power, kms_driven, owner )
#           return render_template('project.html')

# if __name__=="__main__":
#      app.run(debug=True)

from flask import Flask, render_template, request, url_for
import joblib

app = Flask(__name__)
model = joblib.load('model.lb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project', methods=['GET', 'POST'])
def predict():
    pred = None  # ✅ Initialize prediction as None
    if request.method == 'POST':
        brand_name = request.form['brand_name']
        age = float(request.form['age'])
        power = float(request.form['power'])
        owner = int(request.form['owner'])
        kms_driven = float(request.form['kms_driven'])

        brand_dict = {
            'TVS': 0, 'Royal Enfield': 1, 'Triumph': 2, 'Yamaha': 3, 'Honda': 4,
            'Hero': 5, 'Bajaj': 6, 'Suzuki': 7, 'Benelli': 8, 'KTM': 9,
            'Mahindra': 10, 'Kawasaki': 11, 'Ducati': 12, 'Hyosung': 13,
            'Harley-Davidson': 14, 'Jawa': 15, 'BMW': 16, 'Indian': 17,
            'Rajdoot': 18, 'LML': 19, 'Yezdi': 20, 'MV': 21, 'Ideal': 22
        }

        brand_name = brand_dict.get(brand_name, -1)  # Add safety check
        if brand_name == -1:
            return "Invalid brand name!"

        print("data:->>>>", brand_name, age, owner, power, kms_driven)
        lst = [[brand_name, owner, age, power, kms_driven]]
        pred = model.predict(lst)[0]  # ✅ Get the first prediction

        print("Prediction:", pred)

    return render_template('project.html', prediction=pred)
