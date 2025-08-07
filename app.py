from flask import Flask, render_template, request
import boto3
from botocore.exceptions import ClientError

# Create a Flask application instance
app = Flask(__name__)

# Function to check if an S3 bucket is public and return findings + severity level
def is_bucket_public(bucket_name):
    # Create an S3 client using boto3 AWS SDK
    s3 = boto3.client('s3')
    severity = "Low"           # Default severity level
    findings = []              # List to hold all findings/messages

    try:
        # Try to get the bucket's Access Control List (ACL)
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        # Iterate through each grant in the ACL
        for grant in acl['Grants']:
            grantee = grant.get('Grantee', {})
            # Check if the grant gives public access (AllUsers group URI)
            if grantee.get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
                findings.append("ACL allows public access")
                severity = "High"  # If public ACL found, raise severity
    except ClientError as e:
        # Handle specific error if bucket does not exist
        if e.response['Error']['Code'] == 'NoSuchBucket':
            return "Bucket does not exist", "Critical", []
        # If other errors, add a generic message
        findings.append("Could not retrieve ACL")

    try:
        # Try to get the bucket's policy status to check if policy makes it public
        policy_status = s3.get_bucket_policy_status(Bucket=bucket_name)
        # If bucket policy states it is public, add finding and increase severity
        if policy_status['PolicyStatus']['IsPublic']:
            findings.append("Bucket policy allows public access")
            severity = "High"
    except ClientError:
        # If no bucket policy is found, ignore and add a note
        findings.append("No bucket policy found")

    # If no findings, bucket is not public
    if not findings:
        findings.append("No public access detected")

    # Return the list of findings and the severity level
    return findings, severity

# Define the main route '/' that handles GET and POST requests
@app.route("/", methods=["GET", "POST"])
def index():
    result = None    # To hold findings/results to display
    severity = None  # To hold severity level to display

    # Handle form submission (POST)
    if request.method == "POST":
        bucket_name = request.form["bucket"]  # Get bucket name from form input
        result, severity = is_bucket_public(bucket_name)  # Run the check

    # Render the HTML template, passing the results if available
    return render_template("index.html", result=result, severity=severity)

# Run the Flask app only if this file is executed directly (not imported)
if __name__ == "__main__":
    app.run(debug=True)  # Run with debug mode ON for easier development

