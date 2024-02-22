# Commands. Copy and paste them into the existing code for your bot file name "main.py" or what ever it is. If you have trouble you can ask ChatGPT like I did.
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}! I am your friendly bot.')

@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I don't have permission to kick this member.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {e}")

@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I don't have permission to ban this member.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {e}")

@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Latency in milliseconds
    await ctx.send(f'Pong! Latency: {latency}ms')
