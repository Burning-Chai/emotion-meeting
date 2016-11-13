#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import rethinkdb as r

import api.emotion
import service.emotion
from util.config import ConfigUtil


def get_dirs(path):
    dirs = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            dirs.append(item)
    return dirs


def analytics_emotion(save_directly):
    """
    :param save_directly: ${PROJECT_ROOT}/upload/${companyId}/${startTime}
    :return:
    """
    sorted_list = sorted(os.listdir(save_directly))
    for index, name in enumerate(sorted_list):
        wav_file = os.path.join(save_directly, name)
        if os.path.isdir(wav_file):
            continue

        emotion = api.emotion.call(wav_file)
        service.emotion.save(company_id, emotion, start_time, index)


if __name__ == "__main__":
    r.connect("localhost", 28015).repl()

    upload_directly = ConfigUtil.get('FILE', 'upload_directly')
    company_id_list = get_dirs(upload_directly)

    for company_id in company_id_list:
        company_directly = os.path.join(upload_directly, company_id)
        for start_time in os.listdir(company_directly):
            analytics_emotion(os.path.join(company_directly, start_time))
