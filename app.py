from flask import Flask, render_template, request, redirect, session
import pandas as pd
import os
import hashlib

app = Flask(__name__)
app.secret_key = "sabari-secret"

# ------------------------------
# FIXED CSV PATH (DATA FOLDER)
# ------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_FILE = os.path.join(DATA_DIR, "leads.csv")

# Create /data folder if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Create CSV if missing
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=[
        "id", "first_name", "last_name", "company", "email", "phone",
        "lead_source", "lead_status", "industry", "annual_revenue",
        "employees", "website", "rating", "lead_type",
        "street", "city", "state", "zip_code", "country",
        "linkedin", "description", "last_contact", "next_followup",
        "lead_score", "deal_value", "probability", "expected_close"
    ])
    df.to_csv(CSV_FILE, index=False)

# ------------------------------
# LOGIN CREDENTIALS
# ------------------------------
USERNAME = "admin"
PASSWORD_HASH = "7c4e5707012201e984fe34c792139998f8982e371f6d473c3db57155820cf088"  # spike@99

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------------------
# LOGIN
# ------------------------------
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        print("DEBUG username =", username)
        print("DEBUG password =", password)
        print("DEBUG hash_typed =", hash_password(password))
        print("DEBUG hash_correct =", PASSWORD_HASH)

        if username == USERNAME and hash_password(password) == PASSWORD_HASH:
            session["user"] = username
            return redirect("/leads")
        else:
            return render_template("login.html", error="Invalid login")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ------------------------------
# LEADS PAGE
# ------------------------------
@app.route("/leads")
def leads():
    if "user" not in session:
        return redirect("/login")

    df = pd.read_csv(CSV_FILE)
    return render_template("leads.html", leads=df.to_dict("records"))

# ------------------------------
# ADD LEAD
# ------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_lead():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        df = pd.read_csv(CSV_FILE)
        new_id = len(df) + 1

        new_data = {col: request.form.get(col) for col in df.columns if col != "id"}
        new_data["id"] = new_id

        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

        return redirect("/leads")

    return render_template("add.html")

# ------------------------------
# EDIT LEAD
# ------------------------------
@app.route("/edit/<int:lead_id>", methods=["GET", "POST"])
def edit_lead(lead_id):
    if "user" not in session:
        return redirect("/login")

    df = pd.read_csv(CSV_FILE)
    lead = df[df["id"] == lead_id].iloc[0]

    if request.method == "POST":
        for col in df.columns:
            if col != "id":
                df.loc[df["id"] == lead_id, col] = request.form.get(col)

        df.to_csv(CSV_FILE, index=False)
        return redirect("/leads")

    return render_template("edit.html", lead=lead)

# ------------------------------
# DELETE LEAD
# ------------------------------
@app.route("/delete/<int:lead_id>")
def delete_lead(lead_id):
    if "user" not in session:
        return redirect("/login")

    df = pd.read_csv(CSV_FILE)
    df = df[df["id"] != lead_id]
    df.to_csv(CSV_FILE, index=False)

    return redirect("/leads")

# ------------------------------
# RUN SERVER
# ------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
