from flask import Flask
app = Flask(_name_)

@app.route('/')
def index():
 return '<h1>hello</h1>'

if __name__== '__main__ ':
  app.run(debug=True)
