import discord
import os

TOKEN = os.getenv("MTUyNTY5MjI0MTM1MDIzNDExMg.GK2HOV.gbUfq1BoTrx6-ZtfkVRcmzMI6nnvVs_nXU2a78")

intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} が起動しました")


client.run(TOKEN)
