import bot_modules.webpage_handling as webp

if __name__ == '__main__':

    print("Starting bot...")

    current_session = webp.webpage()
    current_session.login()
