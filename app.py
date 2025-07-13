from flask import Flask, render_template,request,redirect,url_for
import mysql.connector as msc

con = msc.connect(host='localhost',user='root',password="Dak@021105",database='netflix')
cursor = con.cursor()

def user_check(username,password):
    cursor.execute(f"SELECT * FROM USER WHERE username = '{username}' and password = '{password}'")
    user = cursor.fetchall()
    return user
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if user_check(username,password):
            return redirect(url_for('main_home'))  
        else:
            return render_template('login.html', error="Incorrect username or password")

    return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])  
def signup():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        cpassword = request.form['cpassword'].strip()
        cursor.execute(f"SELECT * FROM user WHERE email = '{email}'")
        user = cursor.fetchall()
        
    
        if password != cpassword:
            return render_template('signup.html', error="The password does not match !")
        elif user:
            return render_template('signup.html', error="Account already exits !")
        else:   
            cursor.execute(f"INSERT INTO user VALUES('{email}','{username}','{password}')") 
            return redirect(url_for('payment'))  
        
        
    return render_template('signup.html')  

@app.route('/main-home') 
def main_home():
    
    return render_template('main-home.html')  

@app.route('/video-play') 
def video_play():
    return render_template('video-play.html')  

@app.route('/payment')
def payment():
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
