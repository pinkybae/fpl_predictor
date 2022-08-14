import json

class EventsContext:
    
    def __init__(self, payload: dict = None) -> None:
        if payload:
            self.from_payload(payload)
    
    def from_payload(self, payload: dict) -> None:
        self.id = payload.get('id', None)
        self.name = payload.get('name', None)
        self.deadline_time = payload.get('deadline_time', None)
        self.average_entry_score = payload.get('average_entry_score', None)
        self.finished = payload.get('finished', None)
        self.data_checked = payload.get('data_checked', None)
        self.highest_scoring_entry = payload.get('highest_scoring_entry', None)
        self.deadline_time_epoch = payload.get('deadline_time_epoch', None)
        self.deadline_time_game_offset = payload.get('deadline_time_game_offset', None)
        self.highest_score = payload.get('highest_score', None)
        self.is_previous = payload.get('is_previous', None)
        self.is_current = payload.get('is_current', None)
        self.is_next = payload.get('is_next', None)
        self.cup_leagues_created = payload.get('cup_leagues_created', None)
        self.h2h_ko_matches_created = payload.get('h2h_ko_matches_created', None)
        self.chip_plays = payload.get('chip_plays', None)
        self.most_selected = payload.get('most_selected', None)
        self.most_transferred_in = payload.get('most_transferred_in', None)
        self.top_element = payload.get('top_element', None)
        self.top_element_info = payload.get('top_element_info', None)
        self.transfers_made = payload.get('transfers_made', None)
        self.most_captained = payload.get('most_captained', None)
        self.most_vice_captained = payload.get('most_vice_captained', None)
    
    def display(self) -> None:
        print(
            json.dumps(
                {
                    'id' : self.id,
                    'name' : self.name,
                    'deadline_time' : self.deadline_time,
                    'average_entry_score' : self.average_entry_score,
                    'finished' : self.finished,
                    'data_checked' : self.data_checked,
                    'highest_scoring_entry' : self.highest_scoring_entry,
                    'deadline_time_epoch' : self.deadline_time_epoch,
                    'deadline_time_game_offset' : self.deadline_time_game_offset,
                    'highest_score' : self.highest_score,
                    'is_previous' : self.is_previous,
                    'is_current' : self.is_current,
                    'is_next' : self.is_next,
                    'cup_leagues_created' : self.cup_leagues_created,
                    'h2h_ko_matches_created' : self.h2h_ko_matches_created,
                    'chip_plays' : self.chip_plays,
                    'most_selected' : self.most_selected,
                    'most_transferred_in' : self.most_transferred_in,
                    'top_element' : self.top_element,
                    'top_element_info' : self.top_element_info,
                    'transfers_made' : self.transfers_made,
                    'most_captained' : self.most_captained,
                    'most_vice_captained' : self.most_vice_captained,
                },
                indent=4
            )
        )