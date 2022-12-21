import bot_modules.webpage_handling as webp
import sys

if __name__ == '__main__':

    print("\033[1m\033[1;32mStarting bot...\033[0m", end = '\t')
    sys.stdout.flush()

    current_session = webp.webpage()
    current_session.login()
    print('\033[0;32m You man enter commands now \033[0m')
    print()

    while(1):
        print("\033[1;36m\033[1m$\033[0m ", end = '')
        sys.stdout.flush()
        cses_cmd = input()
        current_session.run(cses_cmd)
