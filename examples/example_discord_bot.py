import discord
from discord.ext import commands
from captcha_generator import generate_3d_captcha
import io
import asyncio

intents = discord.Intents.default()
intents.members = True

bot_token = 'YOUR_BOT_TOKEN'
bot_prefix = '/'

bot = commands.Bot(command_prefix=bot_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.slash_command(name="verify", description="Verify yourself with a CAPTCHA")
async def verify(ctx: discord.ApplicationContext):
    captcha_image, captcha_text = generate_3d_captcha(use_russian=False)

    byte_io = io.BytesIO()
    captcha_image.save(byte_io, 'PNG')
    byte_io.seek(0)

    await ctx.respond(file=discord.File(byte_io, 'captcha.png'))
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg_response = await bot.wait_for('message', check=check, timeout=30.0)
        
        if msg_response.content.strip() == captcha_text:
            role_name = 'Verified'  # Change this to your desired role name
            role = discord.utils.get(ctx.guild.roles, name=role_name)
            if role:
                await ctx.author.add_roles(role)
                await ctx.send(f'You have been verified and given the {role_name} role!')
            else:
                await ctx.send(f'Role "{role_name}" not found. Please check the role name.')
        
        else:
            await ctx.send('Incorrect CAPTCHA. Please try again using /verify.')

    except asyncio.TimeoutError:
        await ctx.send('You took too long to respond! Please try again using /verify.')

bot.run(bot_token)
