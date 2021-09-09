import discord
from discord.ext import commands
import asyncio
from io import BytesIO
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=['!', '-'], intents=intents)

@bot.event
async def on_ready():
    activity = discord.Game(name="Sanheco's Discord. Made by ProfessorAdams#0322.", type=3)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Sanheco's Discord. Made by ProfessorAdams#0322."))
    print("Ready.")

@bot.command()
@commands.has_permissions(administrator=True)
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    try:
        await user.send(message)
        await ctx.send('DM Sent Succesfully.')
    except:
        await ctx.send('User has DMs turned off or blocked the bot.')

        
@bot.command(pass_context = True)
async def early(ctx):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, id=int("832774053793234984")) #Early role
    if role in member.roles:
        await ctx.send(f"{ctx.author.mention} you already have the Early Supporters role!")
    else:
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention} you have succesfully claimed the free Early Supporters rank! Thank you for using our server!")
        easterconfirm = bot.get_channel(832774772000555028)
        await easterconfirm.send(f"{ctx.author.mention} has claimed the free Early Supporters rank! Claim yours by typing `!early` in <#713359144295596084>!")

@bot.command(pass_context = True)
async def Early(ctx):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, id=int("832774053793234984")) #Early role
    if role in member.roles:
        await ctx.send(f"{ctx.author.mention} you already have the Early Supporters role!")
    else:
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention} you have succesfully claimed the free Early Supporters rank! Thank you for using our server!")
        easterconfirm = bot.get_channel(832774772000555028)
        await easterconfirm.send(f"{ctx.author.mention} has claimed the free Early Supporters rank! Claim yours by typing `!early` in <#713359144295596084>!")
        
@bot.event
async def on_member_join(member):
    welcomechannel = bot.get_channel(764501344287457340)
    await welcomechannel.send (f"Hey {member}, welcome to **Sanheco's Server**!")

@bot.event
async def on_member_remove(member):
    leavechannel = bot.get_channel(764501344287457340)
    await leavechannel.send(f"{member} just left the server.")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
    
@bot.command()
@commands.has_permissions(administrator=True)
async def staffchange (ctx, *, message):
    await ctx.message.delete()
    channel =bot.get_channel(813702229172420619)
    embed=discord.Embed(title="Staff Change", description = message, color=0x120a8f)
    stafflog = await channel.send(embed=embed)
    await ctx.send(f"{ctx.message.author.mention} - Staff log added to <#813702229172420619>.")
    await stafflog.add_reaction('👍')

@bot.command(pass_context = True)
async def report(ctx, member: discord.Member = None, *, reason = None):
    author = ctx.author

    if member == None:
        await ctx.send('Please mention the user you are reporting after the -report command. EG: -report @user (reason).')
        return
    if reason == None:
        await ctx.send('Please include a reason for the report, after mentioning the user. EG: -report @user (reason).')
        return
    try:
        await asyncio.sleep(1)
        await ctx.message.delete()
        reportschannel=bot.get_channel(818879113245753385)
        await reportschannel.send(f"<@&814079773864624148> The user {ctx.message.author.mention} has reported the user {member.mention}, with the reason of `{reason}`. Please deal with this promptly.")
        await ctx.message.author.send(f"Thanks for making a report {ctx.message.author.mention}. You have reported `{member}`, with the reason of `{reason}`. The staff team have been alerted, and will deal with your report shortly.")
    except:
        await ctx.message.channel.send(f"Thanks for making a report {ctx.message.author.mention}. Your report has been forwarded on to the staff team, however as your DM's are disabled, I'm unable to send you the details of your report via DM's.")
        await ctx.message.delete()
        reportschannel=bot.get_channel(818879113245753385)
        await reportschannel.send(f"<@&814079773864624148> The user {ctx.message.author.mention} has reported the user {member.mention}, with the reason of `{reason}`. Please deal with this promptly.")


adminbancooldown = []

@bot.command(pass_context = True)
@commands.has_any_role('SrMod', 'Admin', 'Senior-Admin', 'Developer', 'Head-Developer', 'Manager', 'Owner/Youtuber')
async def ban(ctx, member: discord.Member = None, *, reason = None):
    author = ctx.author
    
    if author in adminbancooldown:
        await ctx.send('Please wait.')
        return
    
    if member == None:
        await ctx.send('Please mention a member to ban.')
        return
    if reason == None:
        await ctx.send('Please include a ban reason after the user mention.')
        return
        
    
    try:
        await ctx.send(f'Please wait, processing...')
        await member.send(f'You have been banned from **{ctx.guild.name}** for **{reason}**')
        await asyncio.sleep(1)
        await member.send(f'.\nAs we believe in second chances, you can choose to appeal this punishment. You can either admit to the offence, and potentially be unbanned as we believe in second chances. You can also appeal and claim the ban was unfair or not deserved. To do either of those options, please join our appeals server using the invite below:')
        await asyncio.sleep(1)
        await member.send(f'not including our appeals invite in this sample, add your own here please')
        await asyncio.sleep(1)
        await ctx.send(f'A DM has been sent to the user explaining why they have been banned, now banning the user...')

    except:
        await ctx.send(f'A DM explaining why they have been banned **could not** be sent to the user. The user either has their DM\'s turned off, or has blocked the bot. \n\nProceeding with the ban anyway.')
    await member.ban(reason = f"Banned by {ctx.message.author} for " + reason)
    await asyncio.sleep(3)
    await ctx.send(f'The user has been banned succesfully from the server.')
    punishmentschannel = bot.get_channel(818878491054964736)
    await punishmentschannel.send(f"The user {member.mention} has just been banned by {ctx.message.author.mention}, with the reason of " + reason)
    adminbancooldown.append(author)
    await asyncio.sleep(1)
    adminbancooldown.remove(author)


@bot.command()
@commands.has_permissions(administrator=True)
async def poll (ctx, *, message):
    channel=bot.get_channel(818878417436409867)
    await channel.send("Hey @everyone, there's a new poll! Vote below!")
    embed=discord.Embed(title="New Poll!", description = message, color=0xff00ee)
    await asyncio.sleep(1)
    message = await channel.send(embed=embed)
    await asyncio.sleep(2)
    await message.add_reaction('👍')
    await asyncio.sleep(2)
    await message.add_reaction('👎')

@bot.event
async def on_message_edit(message_before, message_after):
    embed=discord.Embed(title="{} edited a message".format(message_before.author.name), description="", color=0xcdf2f2)
    embed.add_field(name= message_before.content ,value="This is the message before the edit ^^", inline=True)
    embed.add_field(name= message_after.content ,value="This is the message after the edit ^^", inline=True)
    embed.add_field(name= "Credits:" ,value="Message logging and bot coded by ProfessorAdams#0322.", inline=True)
    channel=bot.get_channel(818878599393312808)
    await channel.send(embed=embed)

@bot.event
async def on_message_delete(message):
    embed=discord.Embed(title="{} deleted a message".format(message.author), description=" ", color=0x55246c)
    embed.add_field(name= message.content ,value="Message logging and bot coded by ProfessorAdams#0322.", inline=True)
    channel=bot.get_channel(818878599393312808)
    await channel.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, *, message=None):
    message = message or "This is an announcement."
    channel=bot.get_channel(789493048530173982)
    await channel.send(message) 
    
@bot.command()
@commands.has_permissions(administrator=True)
async def event(ctx, *, message=None):
    message = message or "This is an event."
    channel=bot.get_channel(822928823044669521)
    await channel.send(message)
    
    
@bot.command()
@commands.has_permissions(administrator=True)
async def partner(ctx, *, message):
    partnerchannel = bot.get_channel(821126234581762118)
    embed=discord.Embed(title="New Partnership!", description=(message), color=0x0085FF)
    partnerembed=await partnerchannel.send(embed=embed)
    pingpong=await partnerchannel.send("<@&821404518117933127>")
    await ctx.send("Sent to <#821126234581762118>")
    await partnerembed.add_reaction('👍')
    await asyncio.sleep(1)
    await pingpong.delete()


cooldown1 = []

@bot.command(pass_context = True)
async def publicpoll (ctx, *, message):
    author = str(ctx.author)
    if author in cooldown1:
        await ctx.send(ctx.message.author.mention+' Please wait, you can only run one public poll every 2 hours.')
        return

    try:
        channel=bot.get_channel(818913776752787546)
        await channel.send("Poll ran by "+ctx.message.author.mention)
        embed=discord.Embed(title="New Public Poll!", description = message, color=0xff00ee)
        embed.set_footer(text="You can run your own poll here by typing \"-publicpoll (Your question here)\" in any channel!")
        message = await channel.send(embed=embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await ctx.message.delete()
        await ctx.send(ctx.message.author.mention+" Your poll has been posted in <#818913776752787546>!")
        cooldown1.append(author)
        await asyncio.sleep(2 * 60 * 60)    #The argument is in seconds. 2hr = 7200s
        cooldown1.remove(author)
    except:
        await ctx.send('Error, check you are running the command correctly, \"!poll (question here)\"')

        
@bot.command()
@commands.has_permissions(administrator=True)
async def streaming(ctx):
    streamingchannel = bot.get_channel(789493048530173982)
    await streamingchannel.send("Hey @everyone / <@&814433284489740288> : Santaz has just gone live on Twitch! Go check him out! \n\nhttps://twitch.tv/sanheco38")
    await ctx.send(ctx.message.author.mention+" Stream live announcement has been succesfully been sent in <#789493048530173982>. Good luck with streaming! ||-ProfessorAdams :D||")


@tasks.loop(seconds=60)
async def hourlystats():
    if datetime.now().minute == 00:
        channel = bot.get_channel(869361401922224260)
        guild = bot.get_guild(732916164673405008)
        jack = bot.get_user(335076634908426252)
        membercount = 0
        for member in guild.members:
            if not member.bot:
                membercount = membercount +1
        embed = discord.Embed(title="Current Member Count:", description = f"{membercount}", color=0x000000)
        msg = await channel.fetch_message(id=int("877632970599571517"))
        await msg.edit(embed=embed)
        ####
        await asyncio.sleep(1)
        srmodembed = discord.Embed(title="Current Senior Mods:", description = "", color=0xff7b00)
        srmodrole = discord.utils.get(guild.roles, id=int("855512338744475688"))
        for member in srmodrole.members:
            if not member == jack:
                srmodembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632977478230056"))
        await msg.edit(embed=srmodembed)
        ####
        await asyncio.sleep(1)
        modrole = discord.utils.get(guild.roles, id=int("828665485754630254"))
        modembed = discord.Embed(title="Current Mods:", description = "", color=0xe1ff00)
        for member in modrole.members:
            if srmodrole in member.roles:
                print("SrMod")
            else:
                modembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632982612062288"))
        await msg.edit(embed=modembed)
        ####
        await asyncio.sleep(1)
        helperembed = discord.Embed(title="Current Helpers:", description = "", color=0x37ff00)
        helperrole = discord.utils.get(guild.roles, id=int("828665388434063452"))
        for member in helperrole.members:
            helperembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632987657805854"))
        await msg.edit(embed=helperembed)
        ####
        await asyncio.sleep(1)
        communitysupportrole = discord.utils.get(guild.roles, id=int("861372790921887754"))
        communitysupportembed = discord.Embed(title="Community Support People:", description="", color=0x00ffbf)
        for member in communitysupportrole.members:
            if not member == jack:
                communitysupportembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632993173311508"))
        await msg.edit(embed=communitysupportembed)
        ####
        await asyncio.sleep(1)
        contentcreatorsrole = discord.utils.get(guild.roles, id=int("826617659566587935"))
        contentcreatorsembed = discord.Embed(title="Content Creators:", description="", color=0xFFFFFF)
        for member in contentcreatorsrole.members:
            contentcreatorsembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632998537846855"))
        await msg.edit(embed=contentcreatorsembed)
        ####
        await asyncio.sleep(1)
        botrole = discord.utils.get(guild.roles, id=int("733230717525557369"))
        botembed = discord.Embed(title="Bots:", description = "", color=0x0008ff)
        for member in botrole.members:
            botembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877633003596169217"))
        await msg.edit(embed=botembed)
        ####
        await asyncio.sleep(1)
        serverboosterrole = discord.utils.get(guild.roles, id=int("807770503501578251"))
        serverboosterembed = discord.Embed(title="Server Boosters:", description="", color=0xff00e1)
        for member in serverboosterrole.members:
            serverboosterembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877633009019416586"))
        await msg.edit(embed=serverboosterembed)
    if datetime.now().minute == 15:
        channel = bot.get_channel(869361401922224260)
        guild = bot.get_guild(732916164673405008)
        jack = bot.get_user(335076634908426252)
        membercount = 0
        for member in guild.members:
            if not member.bot:
                membercount = membercount +1
        embed = discord.Embed(title="Current Member Count:", description = f"{membercount}", color=0x000000)
        msg = await channel.fetch_message(id=int("877632970599571517"))
        await msg.edit(embed=embed)
        ####
        await asyncio.sleep(1)
        srmodembed = discord.Embed(title="Current Senior Mods:", description = "", color=0xff7b00)
        srmodrole = discord.utils.get(guild.roles, id=int("855512338744475688"))
        for member in srmodrole.members:
            if not member == jack:
                srmodembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632977478230056"))
        await msg.edit(embed=srmodembed)
        ####
        await asyncio.sleep(1)
        modrole = discord.utils.get(guild.roles, id=int("828665485754630254"))
        modembed = discord.Embed(title="Current Mods:", description = "", color=0xe1ff00)
        for member in modrole.members:
            if srmodrole in member.roles:
                print("SrMod")
            else:
                modembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632982612062288"))
        await msg.edit(embed=modembed)
        ####
        await asyncio.sleep(1)
        helperembed = discord.Embed(title="Current Helpers:", description = "", color=0x37ff00)
        helperrole = discord.utils.get(guild.roles, id=int("828665388434063452"))
        for member in helperrole.members:
            helperembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632987657805854"))
        await msg.edit(embed=helperembed)
        ####
        await asyncio.sleep(1)
        communitysupportrole = discord.utils.get(guild.roles, id=int("861372790921887754"))
        communitysupportembed = discord.Embed(title="Community Support People:", description="", color=0x00ffbf)
        for member in communitysupportrole.members:
            if not member == jack:
                communitysupportembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632993173311508"))
        await msg.edit(embed=communitysupportembed)
        ####
        await asyncio.sleep(1)
        contentcreatorsrole = discord.utils.get(guild.roles, id=int("826617659566587935"))
        contentcreatorsembed = discord.Embed(title="Content Creators:", description="", color=0xFFFFFF)
        for member in contentcreatorsrole.members:
            contentcreatorsembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632998537846855"))
        await msg.edit(embed=contentcreatorsembed)
        ####
        await asyncio.sleep(1)
        botrole = discord.utils.get(guild.roles, id=int("733230717525557369"))
        botembed = discord.Embed(title="Bots:", description = "", color=0x0008ff)
        for member in botrole.members:
            botembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877633003596169217"))
        await msg.edit(embed=botembed)
        ####
        await asyncio.sleep(1)
        serverboosterrole = discord.utils.get(guild.roles, id=int("807770503501578251"))
        serverboosterembed = discord.Embed(title="Server Boosters:", description="", color=0xff00e1)
        for member in serverboosterrole.members:
            serverboosterembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877633009019416586"))
        await msg.edit(embed=serverboosterembed)
    if datetime.now().minute == 30:
        channel = bot.get_channel(869361401922224260)
        guild = bot.get_guild(732916164673405008)
        jack = bot.get_user(335076634908426252)
        membercount = 0
        for member in guild.members:
            if not member.bot:
                membercount = membercount +1
        embed = discord.Embed(title="Current Member Count:", description = f"{membercount}", color=0x000000)
        msg = await channel.fetch_message(id=int("877632970599571517"))
        await msg.edit(embed=embed)
        ####
        await asyncio.sleep(1)
        srmodembed = discord.Embed(title="Current Senior Mods:", description = "", color=0xff7b00)
        srmodrole = discord.utils.get(guild.roles, id=int("855512338744475688"))
        for member in srmodrole.members:
            if not member == jack:
                srmodembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632977478230056"))
        await msg.edit(embed=srmodembed)
        ####
        await asyncio.sleep(1)
        modrole = discord.utils.get(guild.roles, id=int("828665485754630254"))
        modembed = discord.Embed(title="Current Mods:", description = "", color=0xe1ff00)
        for member in modrole.members:
            if srmodrole in member.roles:
                print("SrMod")
            else:
                modembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632982612062288"))
        await msg.edit(embed=modembed)
        ####
        await asyncio.sleep(1)
        helperembed = discord.Embed(title="Current Helpers:", description = "", color=0x37ff00)
        helperrole = discord.utils.get(guild.roles, id=int("828665388434063452"))
        for member in helperrole.members:
            helperembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632987657805854"))
        await msg.edit(embed=helperembed)
        ####
        await asyncio.sleep(1)
        communitysupportrole = discord.utils.get(guild.roles, id=int("861372790921887754"))
        communitysupportembed = discord.Embed(title="Community Support People:", description="", color=0x00ffbf)
        for member in communitysupportrole.members:
            if not member == jack:
                communitysupportembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632993173311508"))
        await msg.edit(embed=communitysupportembed)
        ####
        await asyncio.sleep(1)
        contentcreatorsrole = discord.utils.get(guild.roles, id=int("826617659566587935"))
        contentcreatorsembed = discord.Embed(title="Content Creators:", description="", color=0xFFFFFF)
        for member in contentcreatorsrole.members:
            contentcreatorsembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632998537846855"))
        await msg.edit(embed=contentcreatorsembed)
        ####
        await asyncio.sleep(1)
        botrole = discord.utils.get(guild.roles, id=int("733230717525557369"))
        botembed = discord.Embed(title="Bots:", description = "", color=0x0008ff)
        for member in botrole.members:
            botembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877633003596169217"))
        await msg.edit(embed=botembed)
        ####
        await asyncio.sleep(1)
        serverboosterrole = discord.utils.get(guild.roles, id=int("807770503501578251"))
        serverboosterembed = discord.Embed(title="Server Boosters:", description="", color=0xff00e1)
        for member in serverboosterrole.members:
            serverboosterembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877633009019416586"))
        await msg.edit(embed=serverboosterembed)
    if datetime.now().minute == 45:
        channel = bot.get_channel(869361401922224260)
        guild = bot.get_guild(732916164673405008)
        jack = bot.get_user(335076634908426252)
        membercount = 0
        for member in guild.members:
            if not member.bot:
                membercount = membercount +1
        embed = discord.Embed(title="Current Member Count:", description = f"{membercount}", color=0x000000)
        msg = await channel.fetch_message(id=int("877632970599571517"))
        await msg.edit(embed=embed)
        ####
        await asyncio.sleep(1)
        srmodembed = discord.Embed(title="Current Senior Mods:", description = "", color=0xff7b00)
        srmodrole = discord.utils.get(guild.roles, id=int("855512338744475688"))
        for member in srmodrole.members:
            if not member == jack:
                srmodembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632977478230056"))
        await msg.edit(embed=srmodembed)
        ####
        await asyncio.sleep(1)
        modrole = discord.utils.get(guild.roles, id=int("828665485754630254"))
        modembed = discord.Embed(title="Current Mods:", description = "", color=0xe1ff00)
        for member in modrole.members:
            if srmodrole in member.roles:
                print("SrMod")
            else:
                modembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632982612062288"))
        await msg.edit(embed=modembed)
        ####
        await asyncio.sleep(1)
        helperembed = discord.Embed(title="Current Helpers:", description = "", color=0x37ff00)
        helperrole = discord.utils.get(guild.roles, id=int("828665388434063452"))
        for member in helperrole.members:
            helperembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632987657805854"))
        await msg.edit(embed=helperembed)
        ####
        await asyncio.sleep(1)
        communitysupportrole = discord.utils.get(guild.roles, id=int("861372790921887754"))
        communitysupportembed = discord.Embed(title="Community Support People:", description="", color=0x00ffbf)
        for member in communitysupportrole.members:
            if not member == jack:
                communitysupportembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632993173311508"))
        await msg.edit(embed=communitysupportembed)
        ####
        await asyncio.sleep(1)
        contentcreatorsrole = discord.utils.get(guild.roles, id=int("826617659566587935"))
        contentcreatorsembed = discord.Embed(title="Content Creators:", description="", color=0xFFFFFF)
        for member in contentcreatorsrole.members:
            contentcreatorsembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877632998537846855"))
        await msg.edit(embed=contentcreatorsembed)
        ####
        await asyncio.sleep(1)
        botrole = discord.utils.get(guild.roles, id=int("733230717525557369"))
        botembed = discord.Embed(title="Bots:", description = "", color=0x0008ff)
        for member in botrole.members:
            botembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877633003596169217"))
        await msg.edit(embed=botembed)
        ####
        await asyncio.sleep(1)
        serverboosterrole = discord.utils.get(guild.roles, id=int("807770503501578251"))
        serverboosterembed = discord.Embed(title="Server Boosters:", description="", color=0xff00e1)
        for member in serverboosterrole.members:
            serverboosterembed.add_field(name=f"{member.display_name}", value=f"{member.mention}")
        msg = await channel.fetch_message(id=int("877633009019416586"))
        await msg.edit(embed=serverboosterembed)

@hourlystats.before_loop
async def before():
    await bot.wait_until_ready()

hourlystats.start()

bot.run("INSERT_TOKEN_HERE")