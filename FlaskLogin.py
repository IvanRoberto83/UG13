from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route("/login", methods=['POST'])  
def login():
    username = request.form['username']
    password = request.form['password']

    ListUsername = ['Admin','Ivan','Kenzie']
    ListPassword = ['qwe123','r0ku83','foca']

    if username == ListUsername[0] and password == ListPassword[0]:
        return f"Welcome back {username}!"
    elif username == ListUsername[1] and password == ListPassword[1]:
        return f"Welcome back {username}!"
    elif username == ListUsername[2] and password == ListPassword[2]:
        return f"Welcome back {username}!"
    else:
        return "Login Failed! Please check your username & password!"

if __name__ == '__main__':
    print("This is flask Program!")
    app.run()
