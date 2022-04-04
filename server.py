from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/test',methods = ['POST', 'GET'])
def test():
  parametri = ["IQ","Augums","Kājas izmērs"]
  images1 = open("static/images.db.txt", "r")
  images = images1.read()
  images1.close()
  images = images.strip().split("\n")
  return render_template("test.html",parametri=parametri,images=images)

#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "Viss kārtībā!"

@app.route('/response/<response>')
def response(response = "2"):
  return response

if __name__ == '__main__':
  app.run(debug="true")
