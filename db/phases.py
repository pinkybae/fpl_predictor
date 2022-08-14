import json


class PhasesContext:
    def __init__(self, payload: dict = None) -> None:
        if payload:
            self.from_payload(payload)
    
    def from_payload(self, payload: dict) -> None:
        self.id = payload.get('id', None)
        self.name = payload.get('name', None)
        self.start_event = payload.get('start_event', None)
        self.stop_event = payload.get('stop_event', None)

    def display(self) -> None:
        print(
            json.dumps(
                {
                    'id' : self.id,
                    'name' : self.name,
                    'start_event' : self.start_event,
                    'stop_event' : self.stop_event
                },
                indent=4
            )
        )