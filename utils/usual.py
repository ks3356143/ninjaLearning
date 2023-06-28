# -*- coding: utf-8 -*-

from ninjiaDemo.settings import SECRET_KEY
from .chen_jwt import ChenJwt

def get_user_info_from_token(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    token = token.split(" ")[1]
    jwt = ChenJwt(SECRET_KEY)
    value = jwt.decode(SECRET_KEY, token)
    user_info = value.payload
    return user_info
