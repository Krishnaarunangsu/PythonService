# Python Flask Microframework
from flask import Flask, request,make_response,json, jsonify
from src.middleware.data_processing_1 import get_module_subject
from src.middleware.user_data import check_user_login
from src.python_crud.python_crud import insert_employee, fetch_all_employees, fetch_employee_detail_by_employee_id, \
    update_employee_email,delete_employee

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
    # print(f'Password:{password}')
    logged_in = check_user_login(user_name, password)
    if logged_in:
        message = f'{user_name} Logged In Successfully'
    else:
        message = "Invalid Credentials"
    return message


@app.route('/return_json', methods=['GET'])
def return_json():
    """

    :return:
    """
    if request.method == 'GET':
        data = dict(module=15, subject='Big data and Analytics')
        return jsonify(data)


@app.route('/return_subject/<module>', methods=['GET'])
def get_subject(module) -> json:
    """

    Args:
        module: int

    Returns:
        subject:json

    """
    subject = get_module_subject(int(module))
    return subject


@app.route('/login', methods=['POST'])
def login():
    """
    login with username and password
    :return:
    """
    user_name = request.form.get('username')
    password = request.form.get('password')
    logged_in = check_user_login(user_name, password)
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
    data = request.json
    print(data['age'])
    if data['name'] != '' and data['age'] != 0:
        return jsonify(f'{data["name"]} has been created successfully')
    else:
        return jsonify(f'Record has not been created successfully')


@app.route('/create_record', methods=['POST'])
def create_record():
    """

    Returns:

    """
    record = json.loads(request.data)
    print(record)
    with open('src/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('src/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)


@app.route('/get_records/<name>', methods=['GET'])
def get_records(name):
    """

    Args:
        name:

    Returns:

    """
    # name = request.args.get('name')
    name = name
    print(f'{name}')
    with open('src/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                print(record)
                return jsonify(record)
        return jsonify({'error': 'data not found'})


@app.route('/get_all_records', methods=['GET'])
def get_all_records():
    """

    Returns:

    """
    with open('src/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        return jsonify(records)
        # return jsonify({'error': 'data not found'})


@app.route('/update_record', methods=['PUT'])
def update_record():
    """

    Returns:

    """
    record = json.loads(request.data)
    new_records = []
    with open('src/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('src/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


@app.route('/delete_record', methods=['DELETE'])
def delete_record():
    """

    Returns:

    """
    record = json.loads(request.data)
    new_records = []
    with open('src/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('src/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


@app.route('/create_employee', methods=['POST'])
def create_employee():
    """

    Returns:


    """
    my_response=make_response('Response')
    try:
        data = request.json
        print('Hu H1')
        if data['name']=='' or data['email']=='' or data['age']=='':
            print('Hu H1')
            raise ValueError('Value is blank')
        #id, message=insert_employee(data)
        id=1
        message='OK'
        my_response.status_code = 200
    except ValueError as ve:
        print('Hu Ha')
        id=0
        # message=ve.args
        message='Value is blank'
        my_response.status_code=400
    finally:
        return jsonify({'id': id,'message':message,'code':my_response.status_code})




@app.route('/get_all_employees', methods=['GET'])
def get_all_employees():
    """

    Returns:


    """
    data = fetch_all_employees()
    if data is not None:
        return jsonify(data)
    else:
        return jsonify({'message': 'No records found'})


@app.route('/get_employee_detail_by_id/<employee_id>', methods=['GET'])
def get_employee_detail_by_id(employee_id):
    """

    Returns:


    """
    data = fetch_employee_detail_by_employee_id(employee_id)
    if data is not None:
        return jsonify(data)
    else:
        return jsonify({'message': 'No records found'})


@app.route('/update_employee_detail_by_id', methods=['PUT'])
def update_employee_detail_by_id():
    """

    Returns:

    """
    data = request.json
    update_employee_email(data)
    return jsonify(data)


@app.route('/delete_employee_detail_by_id', methods=['DELETE'])
def delete_employee_detail_by_id():
    """

    Returns:

    """
    data = request.json
    delete_employee(data)
    return jsonify({'message':'Employee deleted successfully'})


if __name__ == '__main__':
    app.run()
# https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask
# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# https://flask.palletsprojects.com/en/2.1.x/api/
# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
# https://www.imaginarycloud.com/blog/flask-python/

# https://pythonbasics.org/flask-rest-api/
