#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
import random
import os
import datetime

CATEGORIES = (
    ('1', "Bollywood/Indian"),
    ('2' , "Chillout/Ambient"),
    ('3' , "Classical"),
    ('4' , "Country"),
    ('5' , "D'n'B/Jungle"),
    ('6' , "Dance/Trance"),
    ('7' , "Fanny"),
    ('8' , "International"),
    ('9' , "Latin"),
    ('10' , "Miscellaneous"),
    ('11' , "Oldies"),
    ('12' , "Original"),
    ('13' , "Pop/Rock"),
    ('14' , "Rap/Hip Hop"),
    ('15' , "Reggae"),
    ('16' , "RnB/Garage"),
    ('17' , "SMS Alert"),
    ('18' , "Sound Effects"),
    ('19' , "TV/Film Themes"),
    ('20' , "Video Game Music"),
)

RINGTONES = (
    ('1', "Lion"),
    ('2', "Leopard"),
    ('3', "Panda"),
    ('4', "Tiger"),
    ('5', "Wolf"),
    ('6', "Zebra"),
    ('7', "Bull"),
    ('8', "Cow"),
    ('9', "Calf"),
    ('10', "Buffalo"),
    ('11', "Goat"),
    ('12', "Sheep"),
    ('13', "Lamb"),
    ('14', "Bear"),
    ('15', "Camel"),
    ('16', "Deer"),
    ('17', "Elephant"),
    ('18', "Fox"),
    ('19', "Giraffe"),
    ('20', "Horse"),
    ('21', "Pig"),
    ('22', "Dog"),
    ('23', "Monkey"),
    ('24', "Bat"),
    ('25', "Cat"),
    ('26', "Kangaroo"),
    ('27', "Hedgehog"),
    ('28', "Squirrel"),
    ('29', "Rabbit"),
    ('30', "Dolphin"),
)

fiture_list = []
for category in CATEGORIES:
    category_dict = {
        "pk" : category[0],
        "model" : "services.Category",
        "fields" : {
            "name" : category[1],
            "icon_url" : "http://services.wallyringtone.com/media/image/icon.png",
            "content_level" : 0,
            "last_modify" : str(datetime.datetime(2011, 7, random.randint(1, 10), random.randint(1, 23), 0))
        }
    }
    fiture_list.append(category_dict)

for ringtone in RINGTONES:
    duration = random.randint(10, 300)
    file_size = duration * random.randint(10, 20) * 1024
    ringtone_dict = {
        "pk" : ringtone[0],
        "model" : "services.Ringtone",
        "fields" : {
            "name" : ringtone[1],
            "mime_type" : "audio/x-mpeg",
            "file_size" : file_size,
            "duration" : duration,
            "url" : "http://services.wallyringtone.com/media/audio/demo.mp3",
            "last_modify" : str(datetime.datetime(2011, 6, random.randint(1, 30), random.randint(1, 23), 0)),
            "view_count" : random.randint(400, 500),
            "preview_count" : random.randint(300, 400),
            "download_count" : random.randint(200, 300),
            "set_as_count" : random.randint(100, 200),
            "category" : random.randint(1, 20),
            "upload_user" : 1,
        }
    }
    fiture_list.append(ringtone_dict)

json_data = json.dumps(fiture_list, separators=(',',':'))

cwd = os.getcwd()
fixture_path = os.path.split(cwd)[0] + os.path.sep + "ringtone" + os.path.sep + "services" + os.path.sep + "fixtures" + os.path.sep + "initial_data.json"
open(fixture_path, 'w').write(json_data)
print "Generating test data completed."

    

