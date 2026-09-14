from fastapi import FastAPI
from pydantic import BaseModel, ValidationError
from typing import Optional
from datetime import datetime

app = FastAPI()


class BusEvent(BaseModel):
    Timestamp: str
    Route: str
    Bus: str
    Passengers: int
    Speed_kmh: float
    Status: str


def get_occupancy_category(passengers):
    if passengers <= 10:
        return "LOW"
    elif passengers <= 20:
        return "MEDIUM"
    elif passengers <= 30:
        return "HIGH"
    else:
        return "OVER_CAPACITY"


def validate_event(event):
    errors = []

    try:
        datetime.strptime(event.Timestamp, "%H:%M")
    except ValueError:
        errors.append("Invalid timestamp format. Use HH:MM.")

    if event.Passengers < 0:
        errors.append("Passengers must be non-negative.")


    if event.Speed_kmh < 0 or event.Speed_kmh > 120:
        errors.append("Speed must be between 0 and 120 km/h.")


    if event.Status not in ["ON_ROUTE", "STOPPED"]:
        errors.append("Status must be ON_ROUTE or STOPPED.")

    return errors

@app.post("/events")
def create_event(event: BusEvent):

    errors = validate_event(event)

    if errors:
        return {
            "status": "rejected",
            "validation_errors": errors,
            "occupancy_category": None
        }

    category = get_occupancy_category(event.Passengers)

    return {
        "status": "accepted",
        "validation_errors": [],
        "occupancy_category": category,
        "event": event.model_dump()
    }

