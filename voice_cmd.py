"""voice_cmd.py - demo mapping of speech to safe commands
This example shows how to map safe commands (play, pause, status) to functions.
"""
def play_song(name):
    return f"Playing {name} (demo)"

def system_status():
    return "All systems operational"

COMMAND_MAP = {
    'play': play_song,
    'status': system_status
}

def handle_command(cmd, arg=None):
    fn = COMMAND_MAP.get(cmd)
    if not fn:
        return 'Unknown command'
    return fn(arg) if arg else fn()

if __name__ == '__main__':
    print(handle_command('status'))
    print(handle_command('play','Ngoma'))
