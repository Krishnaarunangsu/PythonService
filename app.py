# Python Flask Microframework
from flask import Flask, request,make_response,json, jsonify
from src.middleware.data_processing_1 import get_module_subject
from src.middleware.user_data import check_user_login
from src.python_crud.python_crud import insert_employee, fetch_all_employees, fetch_employee_detail_by_employee_id, \
    update_employee_email,delete_employee

app = Flask(__name__)  # Flask Constructor

@app.route('/create_employee', methods=['POST'])
def create_employee():
    """

    Returns:

    """
    my_response = make_response('Response')
    message = None
    try:
        data = request.json
        if data['name'] == '' or data['email'] == '' or data['age'] == '':
            raise ValueError('Value is blank')
        id, row_Count, message = insert_employee(data)
    except ValueError as ve:
        message = 'Value is blank'
        error_code = 100
    finally:
        return jsonify(
            {'error_code': error_code, 'message': message, 'http_status_code': my_response.status_code})


@app.route('/get_all_employees', methods=['GET'])
def get_all_employees():
    """

    Returns:

    """
    row_count, emp_records = fetch_all_employees()
    if row_count is not None:
        message = f'Some problem has happened'
        return jsonify({'message': message})
    else:
        if len(emp_records) > 0:
            return jsonify(emp_records)
        elif len(emp_records) = 0:
            return jsonify({'message': 'No records found'})


@app.route('/get_employee_detail_by_id/<employee_id>', methods=['GET'])
def get_employee_detail_by_id(employee_id):
    """

    Returns:

    """
    data_count, data = fetch_employee_detail_by_employee_id(employee_id)
    message = None
    print(f'Data Count:{data_count}')
    if data_count is None:
        message = f'Some problem has happened'
        return jsonify({'message': message})
    else:
        if data_count == 1:
            return jsonify(data)
        elif data_count == 0:
            message = f'No Data Found for the Employee Id:{employee_id}'
            return jsonify({'message': message})


@app.route('/update_employee_detail_by_id', methods=['PUT'])
def update_employee_detail_by_id():
    """

    Returns:

    """
    my_response = make_response('Response')
    response = None
    try:
        data = request.json
        row_updated = update_employee_email(data)
        if row_updated is not None:
            if row_updated > 0:
                response = f'{row_updated} employee updated successfully'
            elif row_updated == 0:
                response = f'No employee updated'
        else:
            raise ValueError
    except ValueError as ve:
        response = f'Some problem has happened'
        error_code = 100
    finally:
        return jsonify(
            {'error_code': error_code, 'message': response, 'http_status_code': my_response.status_code})


@app.route('/delete_employee_detail_by_id', methods=['DELETE'])
def delete_employee_detail_by_id():
    """

    Returns:

    """
    my_response = make_response('Response')
    response = None
    try:
        data = request.json
        row_deleted = delete_employee(data)
        if row_deleted is not None:
            if row_deleted > 0:
                response = f'{row_deleted} employee deleted successfully'
            elif row_deleted == 0:
                response = f'No employee deleted'
        else:
            raise ValueError
    except ValueError as ve:
        response = f'Some problem has happened'
        error_code = 100
    finally:
        return jsonify(
            {'error_code': error_code, 'message': response, 'http_status_code': my_response.status_code})


if __name__ == '__main__':
    app.run()
