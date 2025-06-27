import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    guild = bot.guilds[0]  # أول سيرفر البوت فيه
    print(f"Working on guild: {guild.name}")

@bot.command()
@commands.has_permissions(administrator=True)
async def clean(ctx):
    await ctx.send("جاري حذف جميع القنوات وطرد جميع الأعضاء...")
    guild = ctx.guild

    # حذف جميع القنوات بدون تأخير
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"Deleted channel: {channel.name}")
        except Exception as e:
            print(f"Failed to delete {channel.name}: {e}")

    # طرد جميع الأعضاء (عدا نفسك) بدون تأخير
    for member in guild.members:
        if member == bot.user:
            continue
        try:
            await member.kick(reason="تنظيف السيرفر")
            print(f"Kicked member: {member}")
        except Exception as e:
            print(f"Failed to kick {member}: {e}")

    await ctx.send("تم حذف كل الرومات وطرد كل الأعضاء.")

# ضع التوكن الخاص بك هنا
bot.run("MTM4Nzk1NDk3MzM2MjYxODQ0OQ.G7r-pQ.wmAJwl9eXUNRIkLfNWd8OF6j3-MNIOmZ4n2UQ0")
