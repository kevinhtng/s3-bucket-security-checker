from flask import Flask, render_template, request  # Import Flask and helpers

app = Flask(__name__)  # Create a Flask app instance

# Define the route for the home page ('/') and allow GET and POST methods
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None  # Initialize 'result' to None; will hold scan results if POST

    # Check if the form was submitted via POST
    if request.method == 'POST':
        # Get the bucket name submitted by the user from the form
        bucket_name = request.form['bucket_name']

        # Here we simulate/mock scan results instead of real AWS checks
        result = {
            "Bucket": bucket_name,  # Echo the bucket name back
            "Issues": [             # List of mocked security issues found
                {
                    "Severity": "High",
                    "Description": "Bucket allows public read access.",
                    "Remediation": "Remove public read permissions."
                },
                {
                    "Severity": "Medium",
                    "Description": "Bucket has no encryption enabled.",
                    "Remediation": "Enable SSE-S3 or SSE-KMS encryption."
                }
            ]
        }

    # Render the 'index.html' template, passing the 'result' data (None if GET)
    return render_template('index.html', result=result)

# If this script is run directly, start the Flask development server in debug mode
if __name__ == '__main__':
    app.run(debug=True)

