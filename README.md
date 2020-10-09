# YOLO

> ./darknet detector train build/darknet/x64/data/obj.data build/darknet/x64/cfg/yolo-obj2.cfg build/darknet/x64/yolov4.conv.137 -map

## How to implement Darknet to train my own data

## conf
- 4 class

- obj.data
> classes = 80

> train = /darknet/train.txt

> valid = /darknet/valid.txt

> names = /darknet/obj.names

> backup = /darknet/backup/

- obj.cfg

- weight file

- obj.names
> class name 0

> class name 1

> class name 2

> class name 3

- images

- annotation

- train.txt, valid.txt
