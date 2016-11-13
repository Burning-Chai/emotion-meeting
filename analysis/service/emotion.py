# -*- coding: utf-8 -*-
import rethinkdb as r


def save(company_id, emotion, start_time, index):
    r.db('main').table("emotion").insert({
        'companyId': company_id,
        'emotion': emotion,
        'startTime': int(start_time),
        'index': index + 1,
    }).run()
