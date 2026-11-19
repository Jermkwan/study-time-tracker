import json
from pathlib import Path


RECORDS_FILE = Path(__file__).with_name("study_records.json")


def load_records(file_path=RECORDS_FILE):
    """Load saved study records, returning an empty list for a new store."""
    path = Path(file_path)
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as records_file:
        records = json.load(records_file)

    if not isinstance(records, list) or any(
        not isinstance(record, dict) for record in records
    ):
        raise ValueError("Study records file must contain a JSON list of records.")
    return records


def save_record(record, file_path=RECORDS_FILE):
    """Append one record and persist the full history as JSON."""
    records = load_records(file_path)
    records.append(record)

    path = Path(file_path)
    with path.open("w", encoding="utf-8") as records_file:
        json.dump(records, records_file, ensure_ascii=False, indent=2)