import json
data = {
    "originalRequest": {
        "category": {}
    },
    "totalResultSize": 209,
    "products": [
        {
            "id": "1000004006560322",
            "ean": "0828768235928",
            "gpc": "music",
            "title": "title",
            "specsTag": "tag",
            "summary": "summary",
            "rating": 45,
            "urls": [
                {
                    "key": "DESKTOP",
                    "value": "http://www.url.com"
                },
                {
                    "key": "MOBILE",
                    "value": "https://m.url.com"
                }
            ]
        }
    ]
}
data1 = json.dumps(data)
data2 = json.loads(data1)
print (data2 [1][1][1][1])

for url in data2["products"][0]["urls"]:
    if url["key"] == "MOBILE":
        value = url["value"]
        print (value)
