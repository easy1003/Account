from flask import Response

from utils.serializer import obj_to_json
from flask import send_file


def succ_json(msg=""):
    """
    return success json
    :param msg:
    :return:
    """
    resp = {'code': 0, 'msg': msg}
    return Response(obj_to_json(resp), mimetype='application/json')


def return_json(code=0, msg=""):
    """

    :param code:
    :param msg:
    :return:
    """
    resp = {'code': code, 'msg': msg}
    return Response(obj_to_json(resp), mimetype='application/json')


def return_excel(filename):
    """

    :param filename:
    :return:
    """
    return send_file(filename,
                     as_attachment=True,
                     attachment_filename=filename,
                     mimetype="application/vnd.ms-excel")