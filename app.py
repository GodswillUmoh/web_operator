from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
  return render_template("index.html")

@app.route("/calculate", methods = ["post"])
def calculate():
  first_number =int(request.form["firstNumber"])
  operation = request.form["operation"]
  second_number = int(request.form["secondNumber"])
  if operation == "plus":
    result = first_number + second_number
  elif operation =="minus":
    result = first_number - second_number
  elif operation =="multiply":
    result = first_number * second_number
  elif operation =="divide":
    result = first_number / second_number
  else:
    return "There is an error,insert numbers only"
  return render_template("index.html", result=result)
if __name__ == "__main__":
  app.run(debug=True)