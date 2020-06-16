#Example: Convert Python primitive types into JSON equivalent
import json

sampleDict = {
    "colorList": ["Red", "Green", "Blue"],
    "carTuple": ("BMW", "Audi", "range rover"),
    "sampleString": "pynative.com",
    "sampleInteger": 457,
    "sampleFloat": 225.48,
    "booleantrue": True,
    "booleanfalse": False,
    "nonevalue": None
}
print("Converting Python primitive types into JSON")
resultJSON = json.dumps(sampleDict)
print("Done converting Python primitive types into JSON")
print(resultJSON)