from flask import jsonify


def get_module_subject(module:int)->dict:
    """

    Args:
        module:int

    Returns:
        subject:json

    Raises:
          ValueError

    """
    try:
        if module==15:
            return dict(module=module, subject='Big data and Analytics')
        elif module==16:
            return dict(module=module, subject='Data Science and AI')
        else:
            if (module > 16) & (module < 20):
                return dict(module=module,message='Subject yet not tagged')
            else:
                raise ValueError('No Subject exist')
    except ValueError as ve:
        print(ve)
        return {
                'message': "Bad request!",
                'status': 400,
                'Error': str(ve),
            },400

# raise AssertionError(f'No Subject Found')
