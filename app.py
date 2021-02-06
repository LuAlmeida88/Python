from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["num1"] != "" and  request.form["num2"] != ""):

            if (request.form["opc"] == "soma"):
                soma = int(request.form["num1"]) + int(request.form["num2"])
                return str(soma)

            elif (request.form["opc"] =="sub"):
                sub = int(request.form["num1"]) - int(request.form["num2"])
                return str(sub)

            elif (request.form["opc"] =="mult"):
                mult = int(request.form["num1"]) * int(request.form["num2"])
                return str(mult) 
            else:
                div= int(request.form["num1"]) / int(request.form["num2"])
                return str(div)        

        else:
            return "Informe um valor válido!"    

@app.errorhandler(404)
def not_found(error):
    return render_template ("error.html")

app.run(debug=True)    
