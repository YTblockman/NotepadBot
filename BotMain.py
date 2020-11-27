import discord;
import asyncio;
import pyfiglet;
import pyt as p
from discord.ext import commands;
prefix = "."
bot = commands.Bot(command_prefix = prefix)
tkn = "TOKEN" #PASTE TOKEN HERE
#await ctx.message.channel.send(embed=embedVar)
bot.remove_command('help')

def PRINT(p):
    print(p)
    
def INPUT(p):
    return input(p);

@bot.event
async def on_ready():
    print(">Successfully logged in!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help"))
@bot.command()
async def whereami(ctx):
    try:
        link = await ctx.channel.create_invite(max_age = 300)
        #message = f'You are in {ctx.message.channel} in the {ctx.message.channel.mention} channel with an invite link of {link}'
        #wait ctx.message.author.send(message)
        embedVar = discord.Embed(title="Your server location!", description="sends you server path where you sended message!", color=0x00ff00)
        embedVar.add_field(name="Server", value=link, inline=False)
        embedVar.add_field(name="Channel", value=ctx.message.channel.mention, inline=False)
        embedVar.set_footer(text=f"Triggered by [{ctx.message.author}]")
        embedVar.set_author(name=ctx.author.display_name, url="https://github.com/YTblockman/", icon_url=ctx.author.avatar_url)
        await ctx.message.author.send(embed=embedVar)
        await ctx.message.author.send(link)
    except:
        message = f'You are in DMchannel so i can\'t create link!' 
        await ctx.message.author.send(message)
#https://media.discordapp.net/attachments/725702778839629847/781784448785842186/clip.png?width=365&height=468

@bot.command(pass_context = True)
async def clear(ctx, number=100):
    try:
        number = int(number) #Converting the amount of messages to delete to an integer1
        number +=1;
        counter = 0
        async for x in ctx.message.channel.history(limit = number):
            if counter < number:
                await x.delete()
                counter += 1
                #await asyncio.sleep(0.2) #1.2 second timer so the deleting process can be even
    except:
        embedVar = discord.Embed(title="Error", description=f"{prefix}clear <number>", color=0x00ff00)
        embedVar.add_field(name="Please Try Again", value=f"like *{prefix}clear 1*", inline=False)
        await ctx.message.author.send(embed=embedVar)
@bot.command()
async def ascii(ctx, *what):
    for word in what:
        word.replace("\n", "`\n")
        ascii_banner = pyfiglet.figlet_format(word) #font="slant"
        ascii_banner = ascii_banner.replace("`", ".")
        print(f"`{ascii_banner}`")
        await ctx.message.channel.send(f"`{ascii_banner}`")
    
    pass
    
@bot.command()
async def ping(ctx, what):
    try:
        val = p.ping(what)
        embedVar = discord.Embed(title="Ping! ... Pong?", description=f"You pinged Successfully {what}!", color=0x00ff00)
        embedVar.add_field(name="Ping detatils", value=val, inline=False)
        embedVar.set_footer(text=f"Triggered by [{ctx.message.author}]")
        embedVar.set_author(name=ctx.author.display_name, url="https://github.com/YTblockman/", icon_url=ctx.author.avatar_url)
        embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/725702778839629847/781784448785842186/clip.png?width=365&height=468")
        await ctx.message.channel.send(embed=embedVar)
    except:
        embedVar = discord.Embed(title="Ping! ... Pong?", description=f"Your ping to {what} failed!", color=0xff0000)
        embedVar.add_field(name="Ping detatils", value="None", inline=False)
        embedVar.set_footer(text=f"Triggered by [{ctx.message.author}]")
        embedVar.set_author(name=ctx.author.display_name, url="https://github.com/YTblockman/", icon_url=ctx.author.avatar_url)
        embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/725702778839629847/781784448785842186/clip.png?width=365&height=468")
        await ctx.message.channel.send(embed=embedVar)
        pass
    pass
bot.run(tkn);
