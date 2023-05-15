# Python Flask Microframework
from flask import Flask, request, json, jsonify
from src.middleware.data_processing_1 import get_module_subject
from src.middleware.user_data import check_user_login

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
    #print(f'Password:{password}')
    logged_in = check_user_login(user_name, password)
    if logged_in:
        message = f'{user_name} Logged In Successfully'
    else:
        message = "Invalid Credentials"
    return message


@app.route('/return_json',methods=['GET'])
def return_json():
    """

    :return:
    """
    if request.method == 'GET':
        data= dict(module=15, subject='Big data and Analytics')
        return jsonify(data)

@app.route('/return_subject/<module>',methods=['GET'])
def get_subject(module)->json:
    """

    Args:
        module: int

    Returns:
        subject:json

    """
    subject=get_module_subject(int(module))
    return subject



@app.route('/login', methods=['POST'])
def login():
    """
    login with username and password
    :return:
    """
    user_name = request.form.get('username')
    password = request.form.get('password')
    logged_in=check_user_login(user_name,password)
    if logged_in:
        message = f'{user_name} Logged In Successfully'
    else:
        message = "Invalid Credentials"
    # return jsonify({'msg': 'Logged In successfully'})
    return jsonify({'msg': message})


@app.route('/echo', methods=['POST'])
def hello():
    """

    :return:
    """
    return jsonify(request.json)



@app.route('/save_employee', methods=['POST'])
def submit_employee_data():
    """
    Create a new Employee
    Returns:

    """
    data=request.json
    print(data['age'])
    if data['name']!= '' and data['age']!=0:
        return jsonify(f'{data["name"]} has been created successfully')
    else:
        return jsonify(f'Record has not been created successfully')

if __name__ == '__main__':
    app.run()
# https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask
# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# https://flask.palletsprojects.com/en/2.1.x/api/
# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
# https://www.imaginarycloud.com/blog/flask-python/
