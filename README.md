# s3-bucket-security-checker

## Overview
This project is a **mock AWS S3 bucket security checker** built using **Python (Flask)**. I created it out of **curiosity and a desire to learn more about cloud security concepts**.  

> **Note:** This project does **not connect to real AWS buckets**. All results are simulated for educational purposes.  

I leveraged **AI assistance (ChatGPT)** throughout the project to help with design, coding, and explanations.

---

## Features
- Web-based interface using Flask
- Input a bucket name to receive **mock security scan results**
- Each issue includes:
  - **Severity:** High, Medium, Low
  - **Description:** Explanation of the security concern
  - **Remediation:** Suggested steps to fix the issue
- Color-coded display for severity levels
- Fully self-contained; does **not require AWS credentials**

---

## How It Works
1. User inputs a bucket name on the web page.
2. The app generates a **mock security report** with multiple issues.
3. Issues are displayed with severity indicators and remediation suggestions.

> Scan results are **static**, meaning they are the same for every input, designed to illustrate typical S3 bucket misconfigurations.

---

## Technologies Used
- **Python 3.13**
- **Flask** (web framework)
- **HTML / Jinja2 templates** for front-end rendering

---

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/kevinhtng/s3-bucket-security-checker.git
2. Naviage into the project directory:
   cd s3-bucket-security-checker
3. Install Flask:
   pip install flask
4. Run the app:
   py app.py
5. Open your browser and go to http://127.0.0.1:5000/ to use the tool
