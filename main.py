import json
import random
import traceback
from importlib import import_module

# Initialize pygame library
import pygame
pygame.init()

from src.GameConfig import GAME_LEVELS
from src.GameSimulationOrchestrator import GameSimulationOrchestrator

def get_agent_class_from_str(class_str):
    try:
        module_path, class_name = class_str.rsplit('.', 1)
        module = import_module(module_path)
        return getattr(module, class_name)
    except (ImportError, AttributeError) as e:
        raise ImportError(class_str)

RANDOM_SEED = 0

agent_class_string_list = []
with open('player_agents_list.txt', 'r') as f:
    for line in f:
        agent_class_string_list.append(line.rstrip())

agent_results_dict = {}
for agent_class_str in agent_class_string_list:
    print(f'Starting simulator for agent = {agent_class_str}, with random seed = {RANDOM_SEED}')
    score_dict = {}
    has_failed = False
    for level in GAME_LEVELS:
        if not has_failed:
            # Lock random behavior for all levels to be the same
            random.seed(RANDOM_SEED)

            score = -1
            try:
                simulator = GameSimulationOrchestrator(get_agent_class_from_str(agent_class_str), level)
                score = simulator.run_game()
            except Exception as e:
                print(f'Failed to run simulator for agent: {agent_class_str}. Exception: {e}')
                print(traceback.format_exc())
                    
            if score == -1:
                has_failed = True
                score_dict[level.name] = 'Level Failed'
            else:
                score_dict[level.name] = score
        else:
            score_dict[level.name] = 'Level Not Attempted'

    print(f'Results for agent = {agent_class_str}: {score_dict}')
    agent_results_dict[agent_class_str] = score_dict

print(f'Simulation complete, results: {json.dumps(agent_results_dict, indent=2)}')

output_file_name = 'results.json'
with open(output_file_name, 'w') as output_file:
    json.dump(agent_results_dict, output_file)
    print(f'results saved to {output_file_name}')
