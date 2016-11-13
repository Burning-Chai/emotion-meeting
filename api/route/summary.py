# -*- coding: utf-8 -*-

from flask import Blueprint

import service.emotion
from util.response import ResponseUtil

app = Blueprint('summaries', __name__, url_prefix='')


@app.route('/summaries/<start_time>', methods=['GET'])
def get_summary(start_time):
    a = service.emotion.get_summary_by_start_time(start_time, 'yanou')

    print type(a)

    return ResponseUtil.create_response(200, {
        "summary": "アメリカは変わろうとしている！トランプですよ！！日本はこれでいいのかー！？",
        "emotions": {
            "joy": 12,
            "anger": 34,
            "normal": 100
        }
    })
