from discord.ext import commands
from dotenv import load_dotenv
import os
from labor_tracker import tracker_logic

COMMAND_PREFIX = '!alt-'

load_dotenv()
token = os.getenv('')


bot = commands.Bot(command_prefix=COMMAND_PREFIX)


@bot.command(name='add')
async def add_account(ctx, account: str, labor: int):
    try:
        tracker_logic.add_account(ctx.author, account, labor, ctx.message.created_at)
        await ctx.send(f"@{ctx.author} added account {account} with {labor} labor")
    except Exception as e:
        await ctx.send(f"@{ctx.author} failed to add account {account}: {e}")


@bot.command(name='remove')
async def remove_account(ctx, account: str):
    try:
        tracker_logic.remove_account(ctx.author, account)
        await ctx.send(f"@{ctx.author} removed account {account}")
    except Exception as e:
        await ctx.send(f"@{ctx.author} failed to remove account {account}: {e}")


@bot.command(name='update')
async def set_account_labor(ctx, account: str, labor: int):
    try:
        tracker_logic.set_labor(ctx.author, account, labor, ctx.message.created_at)
        await ctx.send(f"@{ctx.author} set {account} labor to {labor}")
    except Exception as e:
        await ctx.send(f"@{ctx.author} failed to set account {account} labor: {e}")


@bot.command(name='show')
async def show_accounts(ctx):
    try:
        message = tracker_logic.print_accounts(ctx.author, ctx.message.created_at)
        await ctx.send(f"```{message}```")
    except Exception as e:
        await ctx.send(f"@{ctx.author} failed to view accounts: {e}")
