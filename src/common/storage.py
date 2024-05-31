import decouple

from typing import Dict


def aggregate(*args) -> Dict:
    result = {"sum": 0, "avg": 0, "min": 0, "max": 0}
    agg_data = {"sum": [], "avg": [], "min": [], "max": []}
    ...  # Agg logic here

    return result


def sender(agg_result: Dict) -> int:
    arg_time_end = decouple.config("ARG_TIME_END")
    arg_time_start = decouple.config("ARG_TIME_START")
    recipient_type = decouple.config("RECIPIENT_TYPE", default="POSTGRES")

    status = 1  # The status of sending

    if recipient_type == "POSTGRES":
        ...  # If we must send the result to the database
    elif recipient_type == "KAFKA":
        ...  # If we must send the result as broker
    else:
        ...  # If we get an unknown type

    return status
