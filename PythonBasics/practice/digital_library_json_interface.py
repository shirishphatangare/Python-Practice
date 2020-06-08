import json
import os

LIBRARY_JSON_FILE = "resources/digital_library.json"


# Just opening file in append mode will create that file without deleting existing data
def create_library_database():
    with open(LIBRARY_JSON_FILE, "a") as file:
        # json file should have empty object either a dict or a list to start with. It can not be empty
        if os.stat(LIBRARY_JSON_FILE).st_size == 0:   # Check if file is empty
            json.dump([], file)


def insert_record(record):
    records = get_all_records()
    record.update({'read': False})
    records.append(record)
    _save_all_records(records)


def get_all_records():
    with open(LIBRARY_JSON_FILE,"r") as file:
        return json.load(file)


def update_record(record_name):
    records = get_all_records()

    for record in records:
        if record['name'].casefold() == record_name.casefold():
            record['read'] = True

    _save_all_records(records)


def _save_all_records(records):
    # Using File context manager which takes care of file closure
    with open(LIBRARY_JSON_FILE, "w") as file:
        json.dump(records, file)

        # OR
        # for record in records:
        #     json.dump(record, file)


def delete_record(record_name):
    records = get_all_records()

    for record in records:
        if record['name'].casefold() == record_name.casefold():
            records.remove(record)

    _save_all_records(records)