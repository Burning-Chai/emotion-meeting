# -*- coding: utf-8 -*-
import rethinkdb as r


def get_summary_by_start_time(start_time, company_id):
    conn = r.connect("localhost", 28015, db='main').repl()

    resp = r.table('emotion').get_all(int(start_time), index="startTime").run(conn)

    conn.close()

    return resp
