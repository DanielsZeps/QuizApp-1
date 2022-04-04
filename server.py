from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

@app.route('/style1')
def style1():
    return render_template("style.css")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/quizz')
def quizz():
  file = open("static/questions.txt", "r")
  text = file.read()
  file.close()
  text = text.split("\n")
  numbers = []
  for x in range(0, len(text)):
    text[x] = text[x].split(":")
    text[x][0] = text[x][0].split(",")
    text[x][0][0] = str(x+1) + ". " + text[x][0][0]
    text[x][1] = text[x][1].split(",")
    for y in range(0, len(text[x][1])):
      text[x][1][y] = str(y+1) + ". " + text[x][1][y]
  return render_template("quizz.html",questions = text)

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

@app.route('/response1/<response>')
def response1(response = "2"):
  return response

@app.route('/response2/<response>')
def response2(response = "1"):
  file = open("static/storage001.txt", "w")
  file.write(response)
  file.close()
  return "1"

@app.route('/response3')
def response3():
  file = open("static/storage001.txt", "r")
  file1 = file.read()
  file.close()
  return file1

if __name__ == '__main__':
  app.run(debug="true")
