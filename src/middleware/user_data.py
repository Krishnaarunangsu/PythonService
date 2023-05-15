def check_user_login(user_name:str,password:str)->bool:
    """

    Args:
        user_name:
        password:

    Returns:
        boolean
    """
    if user_name=="Tom" and password=="abc123":
        return True
    else:
        return False