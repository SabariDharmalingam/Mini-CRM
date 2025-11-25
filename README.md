📌 Mini CRM System (Flask + CSV Storage)

A lightweight, user-friendly Customer Relationship Management (CRM) system built using Flask, Pandas, and CSV storage.
Includes login authentication, lead management, editing, deletion, and CSV export support.

🚀 Live deployment supported on Render
💾 No database required (CSV-based)
🔐 Secure login using hashed password
📱 Clean and responsive UI

🌟 Features
🔐 Secure Login

SHA256 hashed password (no plain-text password)

Session-based authentication

Default login:

Username: admin
Password: spike@99

🧾 Lead Management

Add new leads

Edit existing leads

Delete leads

View all leads in a data table

All data stored in data/leads.csv

📂 CSV Storage (No Database Needed)

Automatically creates CSV file if missing

Easy to migrate to SQL later

🎨 Clean UI

HTML/Bootstrap templates

Fully responsive

🌍 Deployable on Render

Includes:

render.yaml

requirements.txt

gunicorn start command

📁 Project Structure
mini-crm/
│ app.py
│ requirements.txt
│ render.yaml
│ README.md
│
├── templates/
│   ├── login.html
│   ├── leads.html
│   ├── edit.html
│   └── add.html
│
└── data/
    └── leads.csv

⚙️ Installation (Local)
1️⃣ Clone the repo
git clone https://github.com/YOUR-USERNAME/mini-crm.git
cd mini-crm

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Flask app
python app.py

4️⃣ Open in browser
http://127.0.0.1:5000

🚀 Deployment on Render

Commit this repo to GitHub

Log in to https://render.com

Create New Web Service

Connect your GitHub repository

Render auto-detects render.yaml

Click Deploy

Wait 2–3 minutes

Your public URL will look like:

https://mini-crm.onrender.com

🔐 Login Credentials

Default (you can change inside app.py):

USERNAME = "admin"
PASSWORD = "spike@99"

🧠 Tech Stack

Python (Flask)

Pandas

HTML / Bootstrap

Gunicorn (for Render deployment)

🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

📜 License

This project is open-source and free to use.
