
BASE_COMMANDS = [
    '',
    'quit',
    'open',
    'submit',
]

ATTR_LISTS = {
    BASE_COMMANDS[0] : [1, None],
    BASE_COMMANDS[1] : [1, None],
    BASE_COMMANDS[2] : [2, int],
    BASE_COMMANDS[3] : [3, int, str]
}

def parse(cmd) -> tuple:
    if cmd[0] in ATTR_LISTS:
        if (len(cmd) == ATTR_LISTS[cmd[0]][0]):
            # Can include additional checking here later
            return cmd, True
        else: 
            return None, False
    else:
        return None, False


