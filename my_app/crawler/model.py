import json
from lxml import etree

class Model:

    @staticmethod
    def run():
        """
        --> Find all news
        :return: Object news
        """
        from my_app.crawler.crawler import curl
        return Model.hydrator(curl())

    @staticmethod
    def hydrator(resp):
        convert = [n.contents for n in resp.findAll('item')]
        title = [n.contents for n in resp.findAll('title')]
        pubdate = [n.contents for n in resp.findAll('pubdate')]
        lang = []
        for key, value in enumerate(convert):
            if title[key]:
                item = {
                    "title": title[key],
                    "link": value[4],
                    "pubdate": pubdate[key],
                }
                lang.append(item)
        return lang

    @staticmethod
    def convert(resp, type_return, count=False):
        """
        --> Update return for param_return required
        :param count: true or false
        :param resp: list of return curl
        :param type_return: str json or xml
        :return: resp convert in type json or xml
        """
        if type_return == 'json':

            return json.dumps(resp)

        # create XML
        xml = etree.Element('data')

        for item in resp:
            element = etree.SubElement(xml, 'item')
            if count:
                # another new with text
                child = etree.SubElement(element, 'count')
                child.text = item
            else:
                # another new with text
                child = etree.SubElement(element, 'news')
                child.text = item['title'][0]
                # another child with text
                child = etree.SubElement(element, 'link')
                child.text = item['link']
                # another child with text
                child = etree.SubElement(element, 'pubdate')
                child.text = item['pubdate'][0]
            xml.append(element)
            # pretty string
        return etree.tostring(xml, pretty_print=True)


