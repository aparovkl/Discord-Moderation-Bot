import discord
from discord.ext import commands
from bot_token import token
import time

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'Мы вошли как {client.user}')

@client.command()
@commands.has_permissions(administrator=True)
async def отчистить(ctx, amount: int = 1):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'Удаление сообщений произошло успешно! Удалено: {amount}')
    time.sleep(3)
    await ctx.channel.purge(limit=1)

@client.command()
@commands.has_permissions(administrator = True)
async def мьют(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name='замьючен')
    await member.add_roles(mute_role)
    await ctx.channel.purge(limit=1)
    await ctx.send(f'У {member.mention} мьют по решению администратора.', )
    time.sleep(3)
    await ctx.channel.purge(limit=1)

@client.command()
@commands.has_permissions(administrator = True)
async def кик(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{member.mention} был кикнут, по решению администратора')
    await member.kick()
    time.sleep(3)
    await ctx.channel.purge(limit=1)

@client.command()
@commands.has_permissions(administrator = True)
async def бан(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{member.mention} был забанен, по решению администратора')
    await member.ban()
    time.sleep(3)
    await ctx.channel.purge(limit=1)

client.run(token)
