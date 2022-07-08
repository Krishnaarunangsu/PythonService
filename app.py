# Python Flask Microframework
from flask import Flask, request, json, jsonify

app = Flask(__name__)  # Flask Constructor


# A decorator is used to tell the application which url is associated with the function
@app.route('/')
def show_hello():
    """

    :return:
    """
    return 'HELLO'


# Single Argument in the URL
# url: http://localhost:5000/login/Krishna
@app.route('/login/<username>', methods=['GET'])
def get_user_name(username):
    """
    Get Username
    :return:
    """
    print(f'Username is:{username}')
    return "Krishna is the Truth"


# Multiple Parameters
# url: http://localhost:5000/login?username=Krishna&password=pw1
@app.route('/login', methods=['GET'])
def get_login_params():
    """
    get username
    :return:
    """
    user_name = request.args.get('username')
    password = request.args.get('password')
    print(f'User name:{user_name}')
    print(f'Password:{password}')
    return f'{user_name} Logged in Successfully'


@app.route('/login', methods=['POST'])
def login():
    """
    login with username and password
    :return:
    """
    user_name = request.form.get('username')
    password = request.form.get('password')
    message = f'{user_name} Logged In Successfully'
    print('Coming Here')
    # return jsonify({'msg': 'Logged In successfully'})
    return jsonify({'msg': message})


@app.route('/echo', methods=['POST'])
def hello():
    return jsonify(request.json)


if __name__ == '__main__':
    app.run()
# https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask
# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# https://flask.palletsprojects.com/en/2.1.x/api/
# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
