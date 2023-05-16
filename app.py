from flask import Flask,render_template,request
app=Flask(__name__)

import sqlite3

# db=sqlite3.connect("register.sqlite")
# cur=db.cursor()
# cur.execute('Create table userInfo(name varchar(50),email varchar(50), password varchar(20))')
# cur.execute('Insert into userInfo values("Priyanshu","choudharypriyanshu2002@gmail.com","1234")')
# cur.execute('Insert into userInfo values("Mridul Gupta","mridulpal09@gmail.com","1334")')
# cur.execute('Drop table userInfo')
# db.commit()

@app.route('/temp')
def temp():
    return render_template('temp.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signIn',methods=['GET','POST'])
def signIn():
    if request.method=='POST':
        useremail=request.form.get('email')
        password=request.form.get('password')
        userlogin=request.form.get('loginUser')
        useradmin=request.form.get('loginAdmin')
        print(useremail+' '+password+' '+userlogin+' '+useradmin)
        
    return render_template('signIn.html')

@app.route('/',methods=['GET','POST'])
def login():
    # print("hello")
    if request.method == 'POST':
        # db=sqlite3.connect("register.sqlite")
        # cur=db.cursor()
        # # cur.execute('insert into userInfo values("Priyanshu","choudharypriyanshu2002@gmail.com","1234")')
        print("Hello")
        username=request.form.get('username')
        # username=request.form['username']
        email=request.form.get('email')
        password=request.form.get('password')
        print(username," ",email," ",password)
        # cur.execute('insert into Details values(?,?,?)',(username,email,password))
        # cur.execute('delete from details')
        # db.commit()
    return render_template('signUp.html')



if __name__=="__main__":
    app.run(debug=True)