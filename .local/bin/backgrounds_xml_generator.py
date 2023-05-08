#!/usr/bin/env python3

import os
import xml.etree.ElementTree as ET


def generate_xml(directory_path, xml_file_path):
    # remove the file if it already exists
    if os.path.exists(xml_file_path):
        os.remove(xml_file_path)

    # create root element
    root = ET.Element("background")

    # get the list of files in the directory
    file_list = os.listdir(directory_path)

    # iterate through each file in the directory
    for i in range(len(file_list)):
        # create static element
        static = ET.SubElement(root, "static")

        # create duration element
        duration = ET.SubElement(static, "duration")
        duration.text = "600.0"

        # create file element
        file_path = os.path.join(directory_path, file_list[i])
        file = ET.SubElement(static, "file")
        file.text = file_path

        # create transition element
        transition = ET.SubElement(root, "transition")
        transition_duration = ET.SubElement(transition, "duration")
        transition_duration.text = "0.5"

        # create from and to elements
        from_path = os.path.join(directory_path, file_list[i])
        to_index = (i + 1) % len(file_list)
        to_path = os.path.join(directory_path, file_list[to_index])
        from_elem = ET.SubElement(transition, "from")
        from_elem.text = from_path
        to_elem = ET.SubElement(transition, "to")
        to_elem.text = to_path

    # create and write the XML file
    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='UTF-8', xml_declaration=True)


# example usage
home_path = os.path.expanduser("~")
directory_path = os.path.join(home_path, "Pictures", "Backgrounds")
xml_file_path = os.path.join(directory_path, "backgrounds.xml")
generate_xml(directory_path, xml_file_path)
