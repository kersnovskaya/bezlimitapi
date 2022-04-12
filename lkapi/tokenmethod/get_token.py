from lkapi.base_app import baseapp as ba


def get_access_token(phone: int, password: str) -> str:
    """
    Function for getting access token of user's account before every request to any protected API endpoint.

    :param phone: phone number with format 9XXXXXXXXX
    :param password: password of user's account
    :return: the string of access token. Add this string to header of next request.
    """

    data = {'phone': phone,
            'password': password}

    request_for_get_token = ba.Request("POST", endpoint='/user/auth/login',
                                       data=data)

    response = request_for_get_token.make_request_to_endpoint()

    if response.get_status_code() == 200:
        return response.get_content()['access_token']
    else:
        raise AttributeError
