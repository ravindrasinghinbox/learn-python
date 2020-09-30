import json
# load
x = '{"name":"Jhon","age":30,"city":"New Your"}'
y = json.loads(x)
print(y["age"])
# convert from ptython to json
x = {
    "name": "Jhon",
    "age": 30,
    "city":"New York"
}
y = json.dumps(x)
print(y)
# python into json
print(json.dumps({"name":"John","age":30}))
print(json.dumps(["apple","bananas"]))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
# format the result
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x,indent=4))
print(json.dumps(x,indent=4,separators=(". "," = ")))
# order the result
print(json.dumps(x,indent=4,sort_keys=True))