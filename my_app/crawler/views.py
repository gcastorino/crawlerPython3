from flask import Blueprint, jsonify
from my_app.crawler.controller import Controller
from my_app.crawler.authentication import Authentication

views = Blueprint('views', __name__)


@views.route('/news/<string:auth>/<string:type_return>')
def all_news(auth, type_return):
    """
    --> Search All News
    :route: /news/<string:auth>/<string:type_return>
    :param auth: str
    :param type_return: str - json or xml
    :return: return of find_all function or error
    """
    validation = Authentication.validate(auth, type_return)
    if validation:

        return jsonify(validation)

    return Controller.find_all(type_return)


@views.route('/news/<string:auth>/<string:type_return>/<string:title>')
def find_by_title(auth, type_return, title):
    """
    --> Filter news by keyword in title
    :param auth: str
    :param type_return: str - json or xml
    :param title: str
    :return: return of find_by_title function or error
    """
    validation = Authentication.validate(auth, type_return)
    if validation:

        return jsonify(validation), 404

    return Controller.find_by_title(type_return, title), 200


@views.route('/news/<string:auth>/<string:type_return>/<string:date_start>/<string:date_finish>')
def find_by_range_date(auth, type_return, date_start, date_finish):
    """
    --> Filter news by date (start - end)
    :param auth: str
    :param type_return: str - json or xml
    :param date_start: str
    :param date_finish: str
    :return: return of find_by_range_date function or error
    """
    validation = Authentication.validate(auth, type_return)
    if validation:

        return jsonify(validation), 404

    return Controller.find_by_range_date(type_return, date_start, date_finish), 200


@views.route('/news_count/<string:auth>/<string:type_return>')
def count_news(auth, type_return):
    """
    --> Count you how much news you had in the last hour
    :param auth: str
    :param type_return: str - json or xml
    :return: return of count_news function or error
    """
    validation = Authentication.validate(auth, type_return)
    if validation:

        return jsonify(validation), 404

    return Controller.count_news(type_return), 200
