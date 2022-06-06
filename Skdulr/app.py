from flask import Flask, render_template,request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sk.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class sk(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    # codeforces = db.Column(db.String(200), nullable=False)
    # leetcode = db.Column(db.String(200), nullable=False)
    # subject = db.Column(db.String(200), nullable=False)
    # extra = db.Column(db.String(200), nullable=False)
    ifany = db.Column(db.String(200), nullable=False)
    dates = db.Column(db.DateTime, default=datetime.utcnow)
    

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        ifany = request.form['ifany']
        # date = request.form['date']
        sk1 = sk(ifany=ifany)
        db.session.add(sk1)
        db.session.commit()
        
    allsk = sk.query.all() 
    return render_template('index.html', allSk=allsk)
    # return "<p>Hello, World!</p>"


@app.route('/delete/<int:sno>')
def delete(sno):
    sk1 = sk.query.filter_by(sno=sno).first()
    db.session.delete(sk1)
    db.session.commit()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True,port=8000)