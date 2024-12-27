from discord.ext import commands

bot = commands.Bot(command_prefix="!") 

@bot.command()
async def repeat(ctx, times: int, *, content='repeating...'):
    """Repite un mensaje varias veces."""
    if times > 10:  
        await ctx.send("⚠️ No puedo repetir más de 10 veces.")
        return

    for _ in range(times):
        await ctx.send(content)

@bot.command(name="_bot")
async def bot_info(ctx):
    """Muestra información sobre el bot."""
    bot_name = bot.user.name
    bot_id = bot.user.id
    server_count = len(bot.guilds)

    await ctx.send(
        f"🤖 **Información del Bot:**\n"
        f"- Nombre: {bot_name}\n"
        f"- ID: {bot_id}\n"
        f"- Servidores: {server_count}"
    )

bot.run("TU_TOKEN_AQUÍ")
