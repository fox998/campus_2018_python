from random import randint as rint
from dg_logging import DG_loger as log


game_map_size = 10
cell_free = '-'
cell_trap = '#'
cell_treasure = '@'
cell_player = 'P'


def fill_free_cell(game_map, cell_type):
    log.debug(f'fill_free_cell function was called wit cell type : {cell_type}')
    while (True):
        log.debug(f'looking for free cell')
        i = rint(1, game_map_size)
        j = rint(1, game_map_size)

        if game_map[i][j] == cell_free:
            game_map[i][j] = cell_type
            log.debug(f'free cell is is found with cordinate : x = {j}, y = {i}')
            return [j, i]


def find_player_position(game_map):
    log.debug(f'find_player_position function was called')
    for i in range(1, game_map_size + 2):
        for j in range(1, game_map_size + 2):
            if game_map[i][j] == cell_player:
                log.debug(f'find_player_position: player position is x = {j}, y = {i}')
                return [j, i]
    log.error(f'find_player_position: player wasn`t found')



def new_map():
    log.debug(f'new_map function was called')
    game_map = [[cell_free for j in range(game_map_size + 2)] for i in range(game_map_size + 2)]
    
    for i in range(game_map_size + 2):
        game_map[i][0] = cell_trap
        game_map[0][i] = cell_trap

        game_map[i][game_map_size + 1] = cell_trap
        game_map[game_map_size + 1][i] = cell_trap
    
    for i in range((game_map_size**2) // 20):
        fill_free_cell(game_map, cell_trap)
        fill_free_cell(game_map, cell_trap)
        fill_free_cell(game_map, cell_treasure)

    return game_map
