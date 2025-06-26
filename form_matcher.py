from tinydb import TinyDB
from validators import detect_type

def find_matching_template(db_path: str, input_fields: dict) -> str | dict:
    db = TinyDB(db_path)
    templates = db.all()

    for template in templates:
        tpl_name = template.get("name")
        required_fields = {k: v for k, v in template.items() if k != "name"}

        if all(k in input_fields and detect_type(input_fields[k]) == v for k, v in required_fields.items()):
            return tpl_name

    return {k: detect_type(v) for k, v in input_fields.items()}