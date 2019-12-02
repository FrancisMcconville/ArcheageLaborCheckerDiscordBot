from bot.archeage_labor_tracker import bot
from dotenv import load_dotenv
import os


def run_app():
    load_dotenv()
    token = os.getenv('ARCHEAGE_LABOR_TRACKER_DISCORD_TOKEN')
    bot.run(token)


if __name__ == '__main__':
    run_app()
