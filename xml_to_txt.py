import xml.etree.ElementTree as ET
import os, glob

path = "./xmls/"
txtpath = "./xmls/txts/"
file_list = os.listdir(path)
file_list_xml = [file for file in file_list if file.endswith(".xml")]

for allfile in file_list_xml:
    file_name, _ = os.path.splitext(allfile)
    tree = ET.parse(path+allfile)
    root = tree.getroot()
    width = root.find('size').find('width').text
    height = root.find('size').find('height').text
    for mesh_heading in root.findall('object'):
        name = mesh_heading.find('name').text
        xmin = mesh_heading.find('bndbox').find('xmin').text
        ymin = mesh_heading.find('bndbox').find('ymin').text
        xmax = mesh_heading.find('bndbox').find('xmax').text
        ymax = mesh_heading.find('bndbox').find('ymax').text
        
        xcen=(int(xmax)+int(xmin))/(2*int(width))
        ycen=(int(ymax)+int(ymin))/(2*int(height))
        ratiowidth = (int(xmax)-int(xmin))/int(width)
        ratioheight = (int(ymax)-int(ymin))/int(height)
        line_to_write = "0 " + str(xcen) + ' ' + str(ycen) + ' ' + str(ratiowidth)+ ' '+str(ratioheight) + '\n'
        with open(txtpath+file_name +'.txt', 'a') as f:
            f.write(line_to_write)
