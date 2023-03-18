menu = {
    "breakfast": {
        "hours": "7-11",
        "items": {
            "breakfast burritos": "$6.00",
            "pancakes": "$4.00"
            }
        },
    "lunch" : {
        "hours": "11-3",
        "items": {
            "hamburger": "$5.00"
            }
        },
    "dinner": {
        "hours": "3-10",
        "items": {
            "spaghetti": "$8.00"
            }
        }
}

# encoding dict to json string
import json
menu_json = json.dumps(menu)
print(menu_json, type(menu_json))

# decoding json string to dict
menu2 = json.loads(menu_json)
print(menu2, type(menu2))

# creating new json encoder that can process data types, unknown to normal one
from time import mktime
import datetime
now = datetime.datetime.utcnow()

class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)

print(json.dumps(now, cls=DTEncoder))
print(json.dumps(now, default=str))

