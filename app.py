from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# A global variable to store calculation history
calculation_history = []

@app.route("/", methods=["GET"])
def home():
    return render_template("calculator.html", history=calculation_history)

@app.route("/calculate", methods=["POST"])
def calculate():
    result = None
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
            if num2 == 0:
                result = "Error: Cannot divide by zero."
            else:
                result = num1 / num2
        else:
            result = "Invalid operation."

        # Add the calculation to history
        calculation_history.append(f"{num1} {operation} {num2} = {result}")
    except Exception as e:
        result = f"Error: {e}"

    # Render the result back in the original template
    return render_template("calculator.html", result=result, history=calculation_history)

@app.route("/clear-history", methods=["POST"])
def clear_history():
    # Clear the calculation history
    calculation_history.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)