"""Converts stats to a database saveable form"""

def rt3(stat):
    if "k" in stat[1]:
        abv = "k"
        abvlen = 1
    elif "m" in stat[1]:
        abv = "m"
        abvlen = 1
    elif "b" in stat[1]:
        abv = "b"
        abvlen = 1
    elif "t" in stat[1]:
        abv = "t"
        abvlen = 1
    elif "qa" in stat[1]:
        abv = "qa"
        abvlen = 2
    elif "qi" in stat[1]:
        abv = "qi"
        abvlen = 2
    else:
        abv = ""
        abvlen = 0

    countn = 0
    ntoadd = 0
    
    for i in stat[1]:
        countn += 1
    
    tempstat = stat[1]
    addon = str(abv)
    tempstat = tempstat.replace(addon, "")
    if abvlen == 0:
        while countn < 3:
            if countn < 3:
                countn += 1
                ntoadd += 1
        for i in range (ntoadd):
            tempstat = str(tempstat) + "0"
        if countn > 3:
            ntoremove = countn - 3
            updatestat = ""
            for i in range(3):
                updatestat += tempstat[i]
            tempstat = updatestat
        tempstat = str(tempstat) + addon  
    elif abvlen == 1:
        while countn < 4:
            if countn < 4:
                countn += 1
                ntoadd += 1
        for i in range (ntoadd):
            tempstat = str(tempstat) + "0"
        if countn > 4:
            ntoremove = countn - 4
            updatestat = ""
            for i in range(3):
                updatestat += tempstat[i]
            tempstat = updatestat
        tempstat = str(tempstat) + addon
    elif abvlen == 2:
        while countn < 5:
            if countn < 5:
                countn += 1
                ntoadd += 1
        for i in range (ntoadd):
            tempstat = str(tempstat) + "0"
        if countn > 5:
            ntoremove = countn - 5
            updatestat = ""
            for i in range(3):
                updatestat += tempstat[i]
            tempstat = updatestat
        tempstat = str(tempstat) + addon
    return(tempstat)

def convert(stat):
    stat = stat.lower()
    try:
        stat = stat.split(".")
        
        stat[1] = rt3(stat)
        
        if "k" in stat[1]:
            stat[1] = str(stat[1]).replace("k", "")
            stat[0] = str(stat[0])+"k"
        elif "m" in stat[1]:
            stat[1] = str(stat[1]).replace("m", "000")
            stat[0] = str(stat[0])+"m"
        elif "b" in stat[1]:
            stat[1] = str(stat[1]).replace("b", "000000")
            stat[0] = str(stat[0])+"b"
        elif "t" in stat[1]:
            stat[1] = str(stat[1]).replace("t", "000000000")
            stat[0] = str(stat[0])+"t"
        elif "qa" in stat[1]:
            stat[1] = str(stat[1]).replace("qa", "000000000000")
            stat[0] = str(stat[0])+"qa"
        elif "qi" in stat[1]:
            stat[1] = str(stat[1]).replace("qi", "000000000000000")
            stat[0] = str(stat[0])+"qi"
        else:
            pass
    except:
        pass
    
    if "k" in stat[0]:
        stat[0] = stat[0].replace("k", "000")
    elif "m" in stat[0]:
        stat[0] = stat[0].replace("m", "000000")
    elif "b" in stat[0]:
        stat[0] = stat[0].replace("b", "000000000")
    elif "t" in stat[0]:
        stat[0] = stat[0].replace("t", "000000000000")
    elif "qa" in stat[0]:
        stat[0] = stat[0].replace("qa", "000000000000000")
    elif "qi" in stat[0]:
        stat[0] = stat[0].replace("qi", "000000000000000000")
    else:
        pass
    try:
        stat = int(stat[0])+int(stat[1])
    except:
        stat = int(stat[0])
    return stat