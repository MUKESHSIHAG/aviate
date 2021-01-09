from app import app, db
from flask import render_template, request, flash, redirect, url_for
import pandas as pd
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    u = User.query.all()
    for i in u:
        print(i.timestamp,i.name,i.age)
    return render_template("index.html", data=u)

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    data = pd.read_csv(file, header=0)
    dl = list(data.values)
    for d in dl:
        # print(d[0],d[1],d[2],d[3])
        user = User(timestamp=d[0],email=d[1],name=d[2],city=d[3],contact=d[4],age=d[5],recent_company=d[6],role_in_company=d[7],current_ctc=d[8],fixed_component_ctc=d[9],experience=d[10],comfort=d[11],relocate=d[12],rate_english=d[13],skills=d[14],industries=d[15],profile=d[16],factors=d[17])
        db.session.add(user)
        db.session.commit()
    flash("User added successfully")
    # print(data)
    # print("upload")
    return redirect(url_for("index"))