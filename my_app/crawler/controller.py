from my_app.crawler.model import Model
from datetime import datetime
from datetime import timedelta
from dateutil import parser


class Controller:

    @staticmethod
    def find_all(type_return):
        """
        --> Search All News
        :param type_return:
        :return: return of Convert function
        """

        return Model.convert(Model.run(), type_return)

    @staticmethod
    def find_by_title(type_return, title):
        """
        --> Filter news by keyword in title
        :param type_return:
        :param title:
        :return: return of Convert function
        """
        run = []
        for item in Model.run():
            if title in item['title'][0]:
                run.append(item)

        return Model.convert(run, type_return)

    @staticmethod
    def find_by_range_date(type_return, date_start, date_finish):
        """
        --> Filter news by date (start - end)
        :param type_return:
        :param date_start:
        :param date_finish:
        :return: return of Convert function
        """
        run = []
        for item in Model.run():
            pubdate_object = parser.parse(item['pubdate'][0])
            date_start_object = parser.parse(date_start)
            date_finish_object = parser.parse(date_finish)
            if (pubdate_object >= date_start_object) and (pubdate_object <= date_finish_object):
                run.append(item)

        return Model.convert(run, type_return)

    @staticmethod
    def count_news(type_return):
        """
        --> Count you how much news you had in the last hour
        :param type_return:
        :return: return of Convert function
        """
        now = datetime.today()
        before = now - timedelta(minutes=60)
        run = []
        for item in Model.run():
            pubdate_object = parser.parse(item['pubdate'][0])
            if pubdate_object >= before:
                run.append(item)
        string = 'They had ' + str(len(run)) + ' news in the last hour.'

        return Model.convert([string], type_return, True)
