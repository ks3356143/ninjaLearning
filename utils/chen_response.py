# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from .chen_jwt import DateEncoder

## 重写django的HttpResponse
class ChenResponse(HttpResponse):
    def __init__(self, data=None, message='success', code=200, *args, **kwargs):
        if data is None:
            data = {}
        std_data = {
            "code": code,
            "data": data,
            "message": message,
            "success": True
        }
        data = json.dumps(std_data, cls=DateEncoder)
        super().__init__(data, *args, **kwargs)
