from flask import Flask, render_template, request
import os

app = Flask(__name__)

INSTANCE_NAME = os.environ.get('INSTANCE_NAME', 'Unknown')

def success():
    try:
        rollno = request.form.get('rollno', 'Unknown')
        message = f"Hi from {INSTANCE_NAME}, ur roll number is {rollno}"
        return render_template('success.html', message=message)
    except Exception as e:
        msg = f"Error: {str(e)}"
        return render_template('error.html', error=msg)

@app.route('/cse/success', methods=['POST'])
def cse_success():
    return success()

@app.route('/eee/success', methods=['POST'])
def eee_success():
    return success()

@app.route('/ice/success', methods=['POST'])
def ice_success():
    return success()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)