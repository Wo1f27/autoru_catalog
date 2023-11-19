import xml.etree.ElementTree as ET

from .models import Mark, ModelAuto


# Get mark of car
def update_autoru_catalog():
    Mark.objects.all().delete()
    ModelAuto.objects.all().delete()
    file_xml = 'catalog/xml/cars.xml'
    tree = ET.parse(file_xml)
    root = tree.getroot()
    for mark in root.findall('mark'):
        last_mark = Mark.objects.create(name=mark.attrib['name'].replace(' ', '_'))
        for model in mark.findall('folder'):
            ModelAuto.objects.get_or_create(name=model.attrib['name'].split(', ')[0], mark_id=last_mark)

update_autoru_catalog()