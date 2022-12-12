import os
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption, ChannelType
import nextcord
import statCalculator
import statConverter
from dotenv import load_dotenv
import json

hidethelb = True

with open("userData.json", "r") as f:
    userData = json.load(f)
    f.close()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = nextcord.Client()

testing_server = [1040516185613148180]

@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Game(name="/leaderboard"))
    print("bot is ready")

@client.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        print("Missing permissions lol")

@client.slash_command(guild_ids=testing_server)
@application_checks.has_role(1040523350381965343 or 1044337379428806661)
async def leaderboard(interaction: Interaction, lbtype: str = SlashOption(
    name="type",
    choices={"Fist Strength": "statFS", "Body Toughness":"statBT", "Psychic Power": "statPS", "Total Power": "statTP"}
)):
    if lbtype == "statFS":
        statFS = statCalculator.fistLeaderboard()
        finalFSlb = ""
        lbPlacement = 1
        
        for i in statFS:
            if statCalculator.statHidden(i[0]) == True:
                finalFSlb += f"{lbPlacement}. <@{i[0]}> - \n"
            else:
                finalFSlb += f"{lbPlacement}. <@{i[0]}> - {statCalculator.simplifyStat(i[1])} \n"
            lbPlacement += 1
        
        print(f"{interaction.user} has used FS Leaderboard")
        
        fistembed = nextcord.Embed(title=":droplet:H2O Fist Strength Leaderboard:droplet:", description=finalFSlb, color=0x00FFFF) 
        fistembed.set_footer(text="Hide your stats from LB's with /hidestat :)")
        await interaction.response.send_message(embed=fistembed, ephemeral=hidethelb)
        
    elif lbtype == "statBT":
        statBT = statCalculator.bodyLeaderboard()
        finalBTlb = ""
        lbPlacement = 1
        
        for i in statBT:
            if statCalculator.statHidden(i[0]) == True:
                finalBTlb += f"{lbPlacement}. <@{i[0]}> - \n"
            else:
                finalBTlb += f"{lbPlacement}. <@{i[0]}> - {statCalculator.simplifyStat(i[1])} \n"
            lbPlacement += 1
        
        print(f"{interaction.user} has used BT Leaderboard")
        
        bodyembed = nextcord.Embed(title=":droplet:H2O Body Toughness Leaderboard:droplet:", description=finalBTlb, color=0x00FFFF) 
        bodyembed.set_footer(text="Hide your stats from LB's with /hidestat :)")
        await interaction.response.send_message(embed=bodyembed, ephemeral=hidethelb)
        
    elif lbtype == "statPS":
        statPS = statCalculator.psychicLeaderboard()
        finalPSlb = ""
        lbPlacement = 1
        
        for i in statPS:
            if statCalculator.statHidden(i[0]) == True:
                finalPSlb += f"{lbPlacement}. <@{i[0]}> - \n"
            else:
                finalPSlb += f"{lbPlacement}. <@{i[0]}> - {statCalculator.simplifyStat(i[1])} \n"
            lbPlacement += 1
        
        print(f"{interaction.user} has used PS Leaderboard")
        
        psychicembed = nextcord.Embed(title=":droplet:H2O Psychic Power Leaderboard:droplet:", description=finalPSlb, color=0x00FFFF) 
        psychicembed.set_footer(text="Hide your stats from LB's with /hidestat :)")
        await interaction.response.send_message(embed=psychicembed, ephemeral=hidethelb)
    
    elif lbtype == "statTP":
        statTP = statCalculator.totalLeaderboard()
        finalTPlb = ""
        lbPlacement = 1
        
        for i in statTP:
            if statCalculator.statHidden(i[0]) == True:
                finalTPlb += f"{lbPlacement}. <@{i[0]}> - \n"
            else:
                finalTPlb += f"{lbPlacement}. <@{i[0]}> - {statCalculator.simplifyStat(i[1])} \n"
            lbPlacement += 1
        
        print(f"{interaction.user} has used TP Leaderboard")
        
        totalembed = nextcord.Embed(title=":droplet:H2O Total Power Leaderboard:droplet:", description=finalTPlb, color=0x00FFFF) 
        totalembed.set_footer(text="Hide your stats from LB's with /hidestat :)")
        await interaction.response.send_message(embed=totalembed, ephemeral=hidethelb)
        

@client.slash_command(guild_ids=testing_server)
@application_checks.has_role(1040522303697596477)
async def adduser(interaction: Interaction, discordid: str, fiststrength: str, bodytoughness: str, psychicpower: str, movementspeed: str, jumpforce: str):
    fiststrengthconv = statConverter.convert(fiststrength)
    bodytoughnessconv = statConverter.convert(bodytoughness)
    psychicpowerconv = statConverter.convert(psychicpower)
    movementspeedconv = statConverter.convert(movementspeed)
    jumpforceconv = statConverter.convert(jumpforce)
    
    displayn = await client.fetch_user(discordid)
    channel = client.get_channel(1046369055369597024)
    
    with open("userData.json", "r") as f:
        userData = dict(json.load(f))
        f.close()
    
    userData.update({discordid: {"statFS": int(fiststrengthconv), "statBT": int(bodytoughnessconv),"statJF": int(jumpforceconv), "statMS": int(movementspeedconv), "statPS": int(psychicpowerconv)}})
    
    print(f"""USER UPDATED\nID: {discordid} {displayn.display_name}
          Fist Strength: {fiststrength} --> {fiststrengthconv} --> {statCalculator.simplifyStat(fiststrengthconv)}
          Body Toughness: {bodytoughness} --> {bodytoughnessconv} --> {statCalculator.simplifyStat(bodytoughnessconv)}
          Movement Speed: {movementspeed} --> {movementspeedconv} --> {statCalculator.simplifyStat(movementspeedconv)}
          Jump Force: {jumpforce} --> {jumpforceconv} --> {statCalculator.simplifyStat(jumpforceconv)}
          Psychic Power: {psychicpower} --> {psychicpowerconv} --> {statCalculator.simplifyStat(psychicpowerconv)}""")
    
    await interaction.response.send_message(f"""USER UPDATED\nID: {discordid}, Username: {displayn.name}
          Fist Strength: {fiststrength} --> {fiststrengthconv} --> {statCalculator.simplifyStat(fiststrengthconv)}
          Body Toughness: {bodytoughness} --> {bodytoughnessconv} --> {statCalculator.simplifyStat(bodytoughnessconv)}
          Movement Speed: {movementspeed} --> {movementspeedconv} --> {statCalculator.simplifyStat(movementspeedconv)}
          Jump Force: {jumpforce} --> {jumpforceconv} --> {statCalculator.simplifyStat(jumpforceconv)}
          Psychic Power: {psychicpower} --> {psychicpowerconv} --> {statCalculator.simplifyStat(psychicpowerconv)}""", delete_after=20.0)
    
    print("attempted")
    
    await channel.send(f"""USER UPDATED\nID: {discordid}, Username: {displayn.name}, Updated by {interaction.author.name}
          Fist Strength: {fiststrength} --> {fiststrengthconv} --> {statCalculator.simplifyStat(fiststrengthconv)}
          Body Toughness: {bodytoughness} --> {bodytoughnessconv} --> {statCalculator.simplifyStat(bodytoughnessconv)}
          Movement Speed: {movementspeed} --> {movementspeedconv} --> {statCalculator.simplifyStat(movementspeedconv)}
          Jump Force: {jumpforce} --> {jumpforceconv} --> {statCalculator.simplifyStat(jumpforceconv)}
          Psychic Power: {psychicpower} --> {psychicpowerconv} --> {statCalculator.simplifyStat(psychicpowerconv)}""")  
    
    with open("userData.json", "w") as f:
        json.dump(userData, f, indent=4)
        f.close()

@client.slash_command(guild_ids=testing_server)
async def hidestats(interaction: Interaction, arg: bool):
    
    commandUser = f"{interaction.user.id}"
    
    with open("userData.json", "r") as f:
        userData = dict(json.load(f))
        f.close()
    
    if arg == True:
        userData[f"{commandUser}"]["hidden"] = True
        await interaction.response.send_message("Stats are hidden from leaderboard", ephemeral=True)
    elif arg == False:
        userData[f"{commandUser}"]["hidden"] = False
        await interaction.response.send_message("Stats are shown on leaderboard", ephemeral=True)
    else:
        await interaction.response.send_message("Sorry that wasn't an option", ephemeral=True)
        
    with open("userData.json", "w") as f:
        json.dump(userData, f, indent=4)
        f.close()
        
client.run(TOKEN)