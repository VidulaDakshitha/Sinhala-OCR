
import xml.etree.ElementTree as ET


def xml_string_to_json(xml_string):
    try:
        root = ET.fromstring(xml_string)
        data_json = {}

        for child in root:
            data_json[child.tag] = child.text

        return data_json

    except Exception as ex:
        print("ERROR: XMLto JSON - ", str(ex))
        return False

