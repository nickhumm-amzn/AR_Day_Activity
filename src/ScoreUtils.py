import json
import pygame
import time
from src.GameConfig import GAME_LEVELS, WINDOW_DIMENSIONS, SCORE_BANNER_HEIGHT
from src.PygameGraphicsUtils import BLACK, WHITE, SCORE_FONT


def sum_score_for_all_completed_levels(score_dict):
    total = 0
    for level in score_dict.keys():
        if isinstance(score_dict[level], int):
            total += score_dict[level]
        else:
            break
    return total

def get_best_agents_and_score_aggregations(results_dict):
    # Sort first by number of levels completed:
    max_levels_completed = 0
    max_levels_completed_agents = []
    last_level_completed = None
    for agent in results_dict.keys():
        completed_levels = 0
        for i, level in enumerate(GAME_LEVELS, start=1):
            if not isinstance(results_dict[agent][level.name], int):
                break
            else:
                completed_levels = i
        if completed_levels > max_levels_completed:
            max_levels_completed = completed_levels
            max_levels_completed_agents = [agent]
        elif completed_levels == max_levels_completed:
            max_levels_completed_agents.append(agent)
    
    if max_levels_completed > 0:
        best_agents_dict = {}
        last_level_name = GAME_LEVELS[max_levels_completed-1].name
        for agent in max_levels_completed_agents:
            best_agents_dict[agent] = {
                'last_level_score': results_dict[agent][GAME_LEVELS[max_levels_completed-1].name], 
                'total_score': sum_score_for_all_completed_levels(results_dict[agent]), 
                'last_level_name': last_level_name
            }
        best_agents = sorted(best_agents_dict, key=lambda k: (best_agents_dict[k]['last_level_score'], best_agents_dict[k]['total_score']))
        return best_agents, best_agents_dict
    else:
        return {}

def render_text_wrapping_lines(text, screen):
    words = text.split(' ')
    lines = []
    center_x = WINDOW_DIMENSIONS[0]//2
    center_y = WINDOW_DIMENSIONS[1]//2
    while len(words) > 0:
        line_words = []
        while len(words) > 0:
            next_word = words.pop(0)
            if '\n' in next_word:
                next_word = next_word.replace('\n','')
                line_words.append(next_word)
                break
            else:
                line_words.append(next_word)
                w, h = SCORE_FONT.size(' '.join(line_words + words[:1]))
                if w > WINDOW_DIMENSIONS[0]:
                    break
        line = ' '.join(line_words)
        lines.append(line)

    y_offset = -len(lines)//2
    for line in lines:
        w, h = SCORE_FONT.size(line)
        x = center_x - w / 2
        y = center_y + y_offset
        y_offset += h

        font_surface = SCORE_FONT.render(line, True, WHITE)
        screen.blit(font_surface, (x, y))

def prettify_score_dict_to_string(score_dict):
    out_str = ''
    for k in score_dict.keys():
        formatted_dict = score_dict[k]
        del formatted_dict['last_level_name']
        out_str = out_str + k.split('.', 1)[1] + ': ' + json.dumps(formatted_dict) + ' \n '
    return out_str

def show_end_screen(best_agents_scores):
    pygame.display.set_caption('AR Simulator Game Results')

    game_window = pygame.display.set_mode((WINDOW_DIMENSIONS[0], WINDOW_DIMENSIONS[1] + SCORE_BANNER_HEIGHT))

    game_window.fill(BLACK)
    if len(best_agents_scores.keys()) > 0:
        for k in best_agents_scores.keys():
            last_level_name = best_agents_scores[k]['last_level_name']
            break
    else:
        last_level_name = 'Null'
    end_game_text = f'Game Complete! Highest Level Completed: {last_level_name} \n Best Agent(s): {prettify_score_dict_to_string(best_agents_scores)}'
    render_text_wrapping_lines(end_game_text, game_window)

    pygame.display.update()
    time.sleep(100)
