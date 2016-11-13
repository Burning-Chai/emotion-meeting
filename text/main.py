#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import wave

import rethinkdb as r

import api.speech
from util.config import ConfigUtil


def get_dirs(path):
    dirs = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            dirs.append(item)
    return dirs


def join_waves(inputs, output):
    """
    :param inputs: list of filenames
    :param output: output filename
    """
    try:
        fps = [wave.open(f, 'r') for f in inputs]
        fpw = wave.open(output, 'w')

        fpw.setnchannels(fps[0].getnchannels())
        fpw.setsampwidth(fps[0].getsampwidth())
        fpw.setframerate(fps[0].getframerate())

        for fp in fps:
            fpw.writeframes(fp.readframes(fp.getnframes()))
            fp.close()
        fpw.close()
    except wave.Error, e:
        print e
    except Exception, e:
        print 'unexpected error -> ' + str(e)


def get_text_from_wavs(company_directly):
    """
    :param company_directly: ${PROJECT_ROOT}/upload/${companyId}
    :return:
    """
    for start_time in os.listdir(company_directly):
        print start_time

        save_directly = os.path.join(company_directly, start_time)

        wav_file_list = []
        for f in sorted(os.listdir(save_directly)):
            wav_file_list.append(os.path.join(save_directly, f))

        output_wav_file = os.path.join(company_directly, 'concat.wav')
        join_waves(wav_file_list, output_wav_file)
        api.speech.call(company_directly, 'concat')

        print 'Finish'


if __name__ == "__main__":
    r.connect("localhost", 28015).repl()

    upload_directly = ConfigUtil.get('FILE', 'upload_directly')
    company_id_list = get_dirs(upload_directly)

    for company_id in company_id_list:
        get_text_from_wavs(os.path.join(upload_directly, company_id))
