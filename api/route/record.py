# -*- coding: utf-8 -*-
import os
import zipfile

from flask import Blueprint, request

from util.config import ConfigUtil
from util.response import ResponseUtil

app = Blueprint('record', __name__, url_prefix='')


@app.route('/record', methods=['POST'])
def record():
    # TODO should get companyId from header. header has token data.
    company_id = 'yanou'

    upload_directly = os.path.join(ConfigUtil.get('FILES', 'upload_directly'), company_id)

    print request.form
    print '-' * 30
    print request.headers
    print '-' * 30
    print request.files

    # validate request
    if 'file' not in request.files:
        print "request.files doesn't have file"
        return ResponseUtil.create_response(400, {'code': 1})

    start_time = request.form['startTime']
    save_directly = prepare_directly(upload_directly, start_time)
    if save_directly == '':
        print "Failed to create save directoly"
        return ResponseUtil.create_response(400, {'code': 2})

    tmp_archive_file_path = os.path.join(upload_directly, "record.zip")

    archive_file = request.files['file']
    archive_file.save(tmp_archive_file_path)

    with zipfile.ZipFile(tmp_archive_file_path, 'r') as zip_file:
        zip_file.extractall(path=save_directly)
        if os.path.isdir(os.path.join(save_directly, "__MACOSX")):
            os.rmdir(os.path.join(save_directly, "__MACOSX"))
    os.remove(tmp_archive_file_path)

    return ResponseUtil.create_response(200, {})


def prepare_directly(upload_directly, start_time):
    if not os.path.isdir(upload_directly):
        os.mkdir(upload_directly)

    save_directly = os.path.join(upload_directly, start_time)
    if os.path.isdir(save_directly):
        return ""
    else:
        os.mkdir(save_directly)

    return save_directly
