# RealTime_DA_and_DE

## Important Information

- The project was developed and tested in Google Colab.
- The shuttle events are stored as a list of Python dictionaries.
- Each event contains the following fields:
  - `Timestamp`
  - `Route`
  - `Bus`
  - `Passengers`
  - `Speed_kmh`
  - `Status`
- The `validate_event()` function checks whether the event contains the required fields and whether the passenger and speed values are valid.
- The `event_stream()` function uses a generator and the `yield` statement to produce events one at a time.
- A one-second delay is used to simulate real-time event arrival.
- The events in the dataset are arranged in chronological order.
- The FastAPI endpoint is available at `POST /events`.
- The FastAPI documentation can be opened at:

  `http://127.0.0.1:8000/docs`

- The project is intended for educational purposes. AITU2026
