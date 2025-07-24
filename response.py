from flask import Flask, render_template, request
import os

app = Flask(__name__)

INSTANCE_NAME = os.environ.get('INSTANCE_NAME', 'Unknown')

@app.route('/success')
def success():
    dept = request.form.get('dept', 'Unknown')
    rollno = request.form.get('rollno', 'Unknown')
    message = f"Hi from {dept} {INSTANCE_NAME}, ur roll number is {rollno}"
    if INSTANCE_NAME == "Unknown":
        msg = "Error in server"
        return render_template('error.html', message=msg)
    elif "cse" in INSTANCE_NAME:
        return render_template('success.html', message=message)
    elif "eee" in INSTANCE_NAME:
        return render_template('success.html', message=message)
    elif "ice" in INSTANCE_NAME:
        return render_template('success.html', message=message)
    else:
        return render_template('error.html', message="Invalid department")


if __name__ == '__main__':
    app.run(debug=True)

