import json


class PlayersContext:
    def __init__(self, payload: dict = None) -> None:
        if payload:
            self.from_payload(payload)
    
    def from_payload(self, payload: dict) -> None:
        self.chance_of_playing_next_round = payload.get('chance_of_playing_next_round', None)
        self.chance_of_playing_this_round = payload.get('chance_of_playing_this_round', None)
        self.code = payload.get('code', None)
        self.cost_change_event = payload.get('cost_change_event', None)
        self.cost_change_event_fall = payload.get('cost_change_event_fall', None)
        self.cost_change_start = payload.get('cost_change_start', None)
        self.cost_change_start_fall = payload.get('cost_change_start_fall', None)
        self.dreamteam_count = payload.get('dreamteam_count', None)
        self.element_type = payload.get('element_type', None)
        self.ep_next = payload.get('ep_next', None)
        self.ep_this = payload.get('ep_this', None)
        self.event_points = payload.get('event_points', None)
        self.first_name = payload.get('first_name', None)
        self.form = payload.get('form', None)
        self.id = payload.get('id', None)
        self.in_dreamteam = payload.get('in_dreamteam', None)
        self.news = payload.get('news', None)
        self.news_added = payload.get('news_added', None)
        self.now_cost = payload.get('now_cost', None)
        self.photo = payload.get('photo', None)
        self.points_per_game = payload.get('points_per_game', None)
        self.second_name = payload.get('second_name', None)
        self.selected_by_percent = payload.get('selected_by_percent', None)
        self.special = payload.get('special', None)
        self.squad_number = payload.get('squad_number', None)
        self.status = payload.get('status', None)
        self.team = payload.get('team', None)
        self.team_code = payload.get('team_code', None)
        self.total_points = payload.get('total_points', None)
        self.transfers_in = payload.get('transfers_in', None)
        self.transfers_in_event = payload.get('transfers_in_event', None)
        self.transfers_out = payload.get('transfers_out', None)
        self.transfers_out_event = payload.get('transfers_out_event', None)
        self.value_form = payload.get('value_form', None)
        self.value_season = payload.get('value_season', None)
        self.web_name = payload.get('web_name', None)
        self.minutes = payload.get('minutes', None)
        self.goals_scored = payload.get('goals_scored', None)
        self.assists = payload.get('assists', None)
        self.clean_sheets = payload.get('clean_sheets', None)
        self.goals_conceded = payload.get('goals_conceded', None)
        self.own_goals = payload.get('own_goals', None)
        self.penalties_saved = payload.get('penalties_saved', None)
        self.penalties_missed = payload.get('penalties_missed', None)
        self.yellow_cards = payload.get('yellow_cards', None)
        self.red_cards = payload.get('red_cards', None)
        self.saves = payload.get('saves', None)
        self.bonus = payload.get('bonus', None)
        self.bps = payload.get('bps', None)
        self.influence = payload.get('influence', None)
        self.creativity = payload.get('creativity', None)
        self.threat = payload.get('threat', None)
        self.ict_index = payload.get('ict_index', None)
        self.influence_rank = payload.get('influence_rank', None)
        self.influence_rank_type = payload.get('influence_rank_type', None)
        self.creativity_rank = payload.get('creativity_rank', None)
        self.creativity_rank_type = payload.get('creativity_rank_type', None)
        self.threat_rank = payload.get('threat_rank', None)
        self.threat_rank_type = payload.get('threat_rank_type', None)
        self.ict_index_rank = payload.get('ict_index_rank', None)
        self.ict_index_rank_type = payload.get('ict_index_rank_type', None)
        self.corners_and_indirect_freekicks_order = payload.get('corners_and_indirect_freekicks_order', None)
        self.corners_and_indirect_freekicks_text = payload.get('corners_and_indirect_freekicks_text', None)
        self.direct_freekicks_order = payload.get('direct_freekicks_order', None)
        self.direct_freekicks_text = payload.get('direct_freekicks_text', None)
        self.penalties_order = payload.get('penalties_order', None)
        self.penalties_text = payload.get('penalties_text', None)

    def display(self) -> None:
        print(
            json.dumps(
                {
                    'chance_of_playing_next_round' : self.chance_of_playing_next_round,
                    'chance_of_playing_this_round' : self.chance_of_playing_this_round,
                    'code' : self.code,
                    'cost_change_event' : self.cost_change_event,
                    'cost_change_event_fall' : self.cost_change_event_fall,
                    'cost_change_start' : self.cost_change_start,
                    'cost_change_start_fall' : self.cost_change_start_fall,
                    'dreamteam_count' : self.dreamteam_count,
                    'element_type' : self.element_type,
                    'ep_next' : self.ep_next,
                    'ep_this' : self.ep_this,
                    'event_points' : self.event_points,
                    'first_name' : self.first_name,
                    'form' : self.form,
                    'id' : self.id,
                    'in_dreamteam' : self.in_dreamteam,
                    'news' : self.news,
                    'news_added' : self.news_added,
                    'now_cost' : self.now_cost,
                    'photo' : self.photo,
                    'points_per_game' : self.points_per_game,
                    'second_name' : self.second_name,
                    'selected_by_percent' : self.selected_by_percent,
                    'special' : self.special,
                    'squad_number' : self.squad_number,
                    'status' : self.status,
                    'team' : self.team,
                    'team_code' : self.team_code,
                    'total_points' : self.total_points,
                    'transfers_in' : self.transfers_in,
                    'transfers_in_event' : self.transfers_in_event,
                    'transfers_out' : self.transfers_out,
                    'transfers_out_event' : self.transfers_out_event,
                    'value_form' : self.value_form,
                    'value_season' : self.value_season,
                    'web_name' : self.web_name,
                    'minutes' : self.minutes,
                    'goals_scored' : self.goals_scored,
                    'assists' : self.assists,
                    'clean_sheets' : self.clean_sheets,
                    'goals_conceded' : self.goals_conceded,
                    'own_goals' : self.own_goals,
                    'penalties_saved' : self.penalties_saved,
                    'penalties_missed' : self.penalties_missed,
                    'yellow_cards' : self.yellow_cards,
                    'red_cards' : self.red_cards,
                    'saves' : self.saves,
                    'bonus' : self.bonus,
                    'bps' : self.bps,
                    'influence' : self.influence,
                    'creativity' : self.creativity,
                    'threat' : self.threat,
                    'ict_index' : self.ict_index,
                    'influence_rank' : self.influence_rank,
                    'influence_rank_type' : self.influence_rank_type,
                    'creativity_rank' : self.creativity_rank,
                    'creativity_rank_type' : self.creativity_rank_type,
                    'threat_rank' : self.threat_rank,
                    'threat_rank_type' : self.threat_rank_type,
                    'ict_index_rank' : self.ict_index_rank,
                    'ict_index_rank_type' : self.ict_index_rank_type,
                    'corners_and_indirect_freekicks_order' : self.corners_and_indirect_freekicks_order,
                    'corners_and_indirect_freekicks_text' : self.corners_and_indirect_freekicks_text,
                    'direct_freekicks_order' : self.direct_freekicks_order,
                    'direct_freekicks_text' : self.direct_freekicks_text,
                    'penalties_order' : self.penalties_order,
                    'penalties_text' : self.penalties_text,
                },
                indent=4
            )
        )

class PlayerStatsContext:
    def __init__(self, payload: dict = None) -> None:
        if payload:
            self.from_payload(payload)
    
    def from_payload(self, payload: dict) -> None:
        self.label = payload.get('label', None)
        self.name = payload.get('name', None)

    def display(self) -> None:
        print(
            json.dumps(
                {
                    'label' : self.label,
                    'name' : self.name,
                },
                indent=4
            )
        )
        

class PlayerTypesContext:
    def __init__(self, payload: dict = None) -> None:
        if payload:
            self.from_payload(payload)
    
    def from_payload(self, payload: dict) -> None:
        self.id = payload.get('id', None)
        self.plural_name = payload.get('plural_name', None)
        self.plural_name_short = payload.get('plural_name_short', None)
        self.singular_name = payload.get('singular_name', None)
        self.singular_name_short = payload.get('singular_name_short', None)
        self.squad_select = payload.get('squad_select', None)
        self.squad_min_play = payload.get('squad_min_play', None)
        self.squad_max_play = payload.get('squad_max_play', None)
        self.ui_shirt_specific = payload.get('ui_shirt_specific', None)
        self.sub_positions_locked = payload.get('sub_positions_locked', None)
        self.element_count = payload.get('element_count', None)

    def display(self) -> None:
        print(
            json.dumps(
                {
                    'id' : self.id,
                    'plural_name' : self.plural_name,
                    'plural_name_short' : self.plural_name_short,
                    'singular_name' : self.singular_name,
                    'singular_name_short' : self.singular_name_short,
                    'squad_select' : self.squad_select,
                    'squad_min_play' : self.squad_min_play,
                    'squad_max_play' : self.squad_max_play,
                    'ui_shirt_specific' : self.ui_shirt_specific,
                    'sub_positions_locked' : self.sub_positions_locked,
                    'element_count' : self.element_count,
                },
                indent=4
            )
        )