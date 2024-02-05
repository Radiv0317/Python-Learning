import json
import pickle
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json.loads(json_string))

pickle_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickle_string))
