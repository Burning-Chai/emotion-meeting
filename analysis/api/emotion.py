# -*- coding: utf-8 -*-
import requests

from util.config import ConfigUtil


def call(file_path):
    url = ConfigUtil.get('API', 'url')
    files = {'data.wav': open(file_path, 'rb')}

    print "[POST] " + url + ", " + file_path
    r = requests.post(url, files=files)
    response_body = r.json()

    return response_body["results"]
