import discord
from discord.ext import commands

TOKEN = 'NTIyNTc3ODM1MTEwNjk0OTEz.DvN3Jw.LT4rkUlLmguqg0JlqxKbYYIR-ek'

client = commands.Bot(command_prefix = "//")
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is now ready.')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='video games'))


@client.command()
async def say(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member , role)



@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )

    embed.set_author(name = 'Help')
    embed.add_field(name = '//help', value='Shows this message.', inline=False)
    embed.add_field(name = '//ping', value='Returns Pong!', inline=False)
    embed.add_field(name = '//say', value='Echo your message.', inline=False)
    embed.add_field(name = '//clear', value='Clear how many messages, please put in a interger.', inline=False)

    await client.send_message(author, embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title="Pong! :ping_pong:")
    await client.say(embed=embed)


client.run(TOKEN)
