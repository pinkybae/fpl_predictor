import json


class TeamsContext:
    def __init__(self, payload: dict = None) -> None:
        if payload:
            self.from_payload(payload)
    
    def from_payload(self, payload: dict) -> None:
        self.code = payload.get('code', None)
        self.draw = payload.get('draw', None)
        self.form = payload.get('form', None)
        self.id = payload.get('id', None)
        self.loss = payload.get('loss', None)
        self.name = payload.get('name', None)
        self.played = payload.get('played', None)
        self.points = payload.get('points', None)
        self.position = payload.get('position', None)
        self.short_name = payload.get('short_name', None)
        self.strength = payload.get('strength', None)
        self.team_division = payload.get('team_division', None)
        self.unavailable = payload.get('unavailable', None)
        self.win = payload.get('win', None)
        self.strength_overall_home = payload.get('strength_overall_home', None)
        self.strength_overall_away = payload.get('strength_overall_away', None)
        self.strength_attack_home = payload.get('strength_attack_home', None)
        self.strength_attack_away = payload.get('strength_attack_away', None)
        self.strength_defence_home = payload.get('strength_defence_home', None)
        self.strength_defence_away = payload.get('strength_defence_away', None)
        self.pulse_id = payload.get('pulse_id', None)
    
    def display(self) -> None:
        print(
            json.dumps(
                {
                    'code' : self.code,
                    'draw' : self.draw,
                    'form' : self.form,
                    'id' : self.id,
                    'loss' : self.loss,
                    'name' : self.name,
                    'played' : self.played,
                    'points' : self.points,
                    'position' : self.position,
                    'short_name' : self.short_name,
                    'strength' : self.strength,
                    'team_division' : self.team_division,
                    'unavailable' : self.unavailable,
                    'win' : self.win,
                    'strength_overall_home' : self.strength_overall_home,
                    'strength_overall_away' : self.strength_overall_away,
                    'strength_attack_home' : self.strength_attack_home,
                    'strength_attack_away' : self.strength_attack_away,
                    'strength_defence_home' : self.strength_defence_home,
                    'strength_defence_away' : self.strength_defence_away,
                    'pulse_id' : self.pulse_id,
                },
                indent=4
            )
        )