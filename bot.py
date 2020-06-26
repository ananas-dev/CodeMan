#!/usr/bin/env python3

import discord
from discord.ext import commands
from db import insertNewPlayer, findCode, findDiscordId

TOKEN = "ENTERTOKENHERE"

client = commands.Bot(command_prefix="&")

@client.event
async def on_ready():
    print(":: Bot launched")
    await client.change_presence(activity=discord.Game("&howto"))

@client.command(pass_context=True)
async def howto(ctx):
    embed = discord.Embed(
        title="CodeMan",
        description="CodeMan is a BOT to manage slippi connect codes for ssbm.",
        color=0x44a963
    )
    embed.add_field(name="&add", value="Adds your connect code to the database.", inline=False)
    embed.add_field(name="&code", value="Shows your code or the one of someone else.", inline=False)
    embed.add_field(name="&whois", value="Finds a discord username from a code.", inline=False)
    embed.add_field(name="&ask", value="Asks for you if someone want to play.", inline=False)
    embed.add_field(name="&howto", value="Shows this message.", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def add(ctx, code = None):
    if code is None:
        await ctx.send("You must enter a code !")
    else:
        author = ctx.message.author.id
        insertNewPlayer(author, code)
        await ctx.send("Done !")

@client.command()
async def code(ctx,user: discord.User = None):
    if user is None:
        author = ctx.message.author.id
        code = findCode(author)
        await ctx.send(code)
    else:
        code = findCode(user.id)
        if code is None:
            await ctx.send("This user has no connect code !")
        else:
            await ctx.send(code)

@client.command(pass_context=True)
async def ask(ctx, role: discord.Role = None):
        author = ctx.message.author.id
        author_name = ctx.message.author.name
        await ctx.message.delete()
        code = findCode(author)
        if role is None:
            await ctx.send("{} wants to play, code: {}".format(author_name, code))
        else:
            await ctx.send("{} {} wants to play, code: {}".format(role.mention, author_name, code))

@client.command()
async def whois(ctx, code = None):
    if code is None:
        await ctx.send("You must enter a code !")
    else:
        discord_id = findDiscordId(code)
        if discord_id is None:
            await ctx.send("This code has no player attached to it :/")
        else:
            discord_name = client.get_user(discord_id)
            await ctx.send("{} is {}".format(code, discord_name))

client.run(TOKEN)