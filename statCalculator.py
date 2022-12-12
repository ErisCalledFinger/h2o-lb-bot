"""
Stat calculator script for the H2O leaderboard bot
"""
import math
import os
import json

def simplifyStat(n):
    """
    Simplify numbers in an easier to read format
    
    - note this does round to 5 significant figures to hinders the accuracy of the numbers.
    """
    try:
        if n < 1000:
            n = n
        elif n < 1000000:
            n = float(n)/1000
            n = f"{n:.5g}K"
        elif n < 1000000000:
            n = float(n)/1000000
            n = f"{n:.5g}M"
        elif n < 1000000000000:
            n = float(n)/1000000000
            n = f"{n:.5g}B"
        elif n < 1000000000000000:
            n = float(n)/1000000000000
            n = f"{n:.5g}T"
        elif n < 1000000000000000000:
            n = float(n)/1000000000000000
            n = f"{n:.5g}Qa"
        elif n < 1000000000000000000000:
            n = float(n)/1000000000000000000
            n = f"{n:.5g}Qi"  
        return n
    except:
        return
    

def getData(id):
    with open("userData.json", "r") as f:
        userData = dict(json.load(f))
        f.close()
    idInfo = {}    
    for i in userData:
        idUser = userData[i]
        idInfo[i] = idUser[id]
        
    idInfo = sorted(idInfo.items(), key=lambda x: x[1], reverse=True)
    
    return idInfo

def statHidden(i):
    with open("userData.json", "r") as f:
        userData = dict(json.load(f))
        f.close()
    if userData[i]["hidden"] == True:
        return True
    else:
        return False
    

def psychicLeaderboard():
    """
    Grab each users psychic power data from the database
    """
    
    statPS = getData("statPS")
    
    return statPS

def bodyLeaderboard():
    """
    Grab each users body toughness data from the database
    """

    statBT = getData("statBT")
    
    return statBT

def fistLeaderboard():
    """
    Grab each users fist strength data from the database
    """

    statFS = getData("statFS")
    
    return statFS
    
def movementLeaderboard():

    statMS = getData("statMS")
    
    return statMS
        
def jumpForceLeaderboard():

    statJF = getData("statJF")
    
    return statJF
    

def totalLeaderboard():
    """
    Calculate each users total power using the database
    """
    
    with open("userData.json", "r") as f:
        userData = json.load(f)
        f.close()

    statFS = {}
    statBT = {}
    statPS = {}
    statTP = {}
    
    for i in userData:
        userFS = userData[i]["statFS"] 
        userBT = userData[i]["statBT"]
        userPS = userData[i]["statPS"]
        statFS[i] = userFS
        statBT[i] = userBT
        statPS[i] = userPS
        statTP[i] = statFS[i] + statBT[i] + statPS[i]
        
    statTP = sorted(statTP.items(), key=lambda x: x[1], reverse=True)
        
    return statTP