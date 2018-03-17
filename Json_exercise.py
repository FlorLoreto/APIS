import json
from pprint import pprint
data={
    "maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": {
        "id": "valore"
    },
    "om_points": "value",
    "parameters": {
        "id": "valore"
    }
}
data1 = json.dumps(data)
data2 = json.loads(data1)
pprint(data2)
print (data2["maps"][0]["id"])
print (data2["maps"][1]["id"])
print (data2["masks"]["id"])
