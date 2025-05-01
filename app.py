from flask import Flask, request, render_template
 
app = Flask(__name__)
 
# Home route with a form for the calculator
@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            # Get numbers and operation from the form
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form.get("operation")
 
            # Perform the calculation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2
            else:
                result = "Invalid operation"
        except Exception as e:
            result = f"Error: {e}"
 
    return render_template("calculator.html", result=result)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)