from game_states import GameStates


def kill_player(player, colors):
    player.char = '%'
    player.color = colors.get('dark_red')

    return 'You died!', GameStates.PLAYER_DEAD


def kill_monster(monster, colors):
    death_message = '{0} is dead!'.format(monster.name.capitalize())

    monster.char = '%'
    monster.color = colors.get('dark_red')
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name

    return death_message