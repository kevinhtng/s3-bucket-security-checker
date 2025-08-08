from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        bucket_name = request.form['bucket_name']

        # Expanded mocked scan results with more issues & severities
        result = {
            "Bucket": bucket_name,
            "Issues": [
                {
                    "Severity": "High",
                    "Description": "Bucket allows public read access.",
                    "Remediation": "Remove public read permissions."
                },
                {
                    "Severity": "Medium",
                    "Description": "Bucket has no encryption enabled.",
                    "Remediation": "Enable SSE-S3 or SSE-KMS encryption."
                },
                {
                    "Severity": "Low",
                    "Description": "Bucket logging is not enabled.",
                    "Remediation": "Enable access logging for audit purposes."
                },
                {
                    "Severity": "Medium",
                    "Description": "Bucket policy allows overly broad IAM roles.",
                    "Remediation": "Restrict IAM roles to least privilege."
                }
            ]
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
