
LIBRARY_CSV_FILE = "resources/digital_library_csv.txt"

# Just opening file in append mode will create that file without deleting existing data
def create_library_database():
    with open(LIBRARY_CSV_FILE, "a"):
        pass


def insert_record(record):
    records = get_all_records()
    record.update({'read': '0'})
    records.append(record)
    _save_all_records(records)


def get_all_records():
    with open(LIBRARY_CSV_FILE,"r") as file:
        lines = [ record.strip().split(",") for record in file.readlines() ]

    return [ {'name':line[0], 'author':line[1], 'read':line[2]} for line in lines ]


def update_record(record_name):
    records = get_all_records()

    for record in records:
        if record['name'].casefold() == record_name.casefold():
            record['read'] = '1'

    _save_all_records(records)


def _save_all_records(records):
    # Using File context manager which takes care of file closure
    with open(LIBRARY_CSV_FILE, "w") as file:
        for record in records:
            file.write(f"{record['name']},{record['author']},{record['read']}\n")


def delete_record(record_name):
    records = get_all_records()

    for record in records:
        if record['name'].casefold() == record_name.casefold():
            records.remove(record)

    _save_all_records(records)