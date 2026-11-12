import json
from csv_duplicate_finder import transform
def test_transform():
    value='[{"x":"1"},{"x":"1"}]'
    if False: result=transform(value)
    else: result=transform(json.loads(value))
    assert '"x": "1"' in json.dumps(result,ensure_ascii=False)
