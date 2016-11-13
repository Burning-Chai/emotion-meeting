# -*- coding: utf-8 -*-
import os

import requests
from util.config import ConfigUtil


def call(input_file_dir, input_file_name):
    os.system('/usr/local/bin/flac -f ' + input_file_dir + '/' + input_file_name + '.wav')

    url = 'https://www.google.com/speech-api/v2/recognize' \
                        '?xjerr=1' \
                        '&client=chromium' \
                        '&lang=ja-JP' \
                        '&maxresults=10' \
                        '&pfilter=0' \
                        '&xjerr=1' \
                        '&key=' + ConfigUtil.get('GOOGLE', 'api_key')
    headers = {
        # "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7",
        'Content-type': 'audio/x-flac; rate=16000'
    }

    f = open(input_file_dir + '/' + input_file_name + '.flac', 'rb')
    flac_cont = f.read()
    f.close()

    print url
    print "[POST] Google Speech API"
    r = requests.post(url, headers=headers, data=flac_cont)

    print r.json()

    # response_body = r.json()
    # return response_body["results"]
    return ""
