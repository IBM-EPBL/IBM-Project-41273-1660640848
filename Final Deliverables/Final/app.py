from flask import Flask ,render_template, request, session,flash,redirect
import ibm_db

app = Flask(__name__)

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCerficate=DigiCertGlobalRootCA.crt;UID=gqx98810;PWD=shidQiWRftvLQAf5",'  ',' ')

print(conn)
print("Connection Successful...")


# app.secret_key ="lgkfkdkhglf"

@app.route('/')
def home():
    return render_template("login.html")


@app.route('/signup')
def home():
    return render_template("signup.html")


@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("login.html")


@app.route('/login', methods=['POST', "GET"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pssword = request.form.get('password')

        sql = "select * from GQX98810.USER where username = ? and password = ?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.bind_param(stmt, 2, pssword)
        ibm_db.execute(stmt)
        user = ibm_db.fetch_assoc(stmt)
        if user:
              session['username'] = user['username']
              session['is_loggedin'] = True
              return redirect('index.html')

        user = ibm_db.fetch_assoc(stmt)

        if user:
            print(user)
            print(user['ID'])
            user_password = user['PSSWORD']
            
        else:
                flash('Password is incorrect')
                return render_template('login.html')
       




@app.route('/signup', methods=['POST', "GET"])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('full')
        username = request.form.get('username')
        email = request.form.get('email')
        pssword = request.form.get('password')
        
        
        sql = "INSERT INTO GQX98810.USER(fullname,username,email,pssword) VALUES('{}','{}','{}','{}')".format(fullname,username,email,pssword)
        ibm_db.exec_immediate(conn,sql)
        flash("Register Successful")
        return render_template('login.html')

    else:

        return render_template('signup.html')



