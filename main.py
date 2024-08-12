import time

def getRIMFAXData():
    """ 
    Fetches the RIMFAX data

    Returns: str: The RIMFAX data. 
    """
    data = {"Radar": 423525234, "Lidar": 4563455234, "Camera": 756723453}
    return data
def getNSSData():
    """ 
    Fetches the NSS data

    Returns: str: The NSS data. 
    """
    data = {"Radar": 423525234, "Lidar": 4563455234, "Camera": 756723453}
    return data

def getTempData():
    """ 
    Fetches the temperature data

    Returns: str: The temperature data. 
    """
    data = {"RIMFAX": 423525234, "NSS": 4563455234, "Chassis": 756723453, "Power": 234234234, "CDH": 234234234}
    return data

def getTelemetryData():
    """ 
    Fetches the telemetry data

    Returns: str: The telemetry data. 
    """
    data = {"RIMFAX": 423525234, "NSS": 4563455234, "Chassis": 756723453, "Power": 234234234, "CDH": 234234234}
    return data
def satelliteAbove():
    """ 
    Determines if the satellite is above the horizon

    Returns: bool: True if the satellite is above the horizon, False otherwise. 
    """
    return True
def calcRedundantBits(m):
    """ 
    Determines the number of redundant bits 'r' needed for Hamming Code given 'm' data bits. 

    Returns: int: Number of redundant bits required. 
    """
    for i in range(m):
        if(2**i >= m + i + 1):
            return i
def sendDataToSatellite(data):
    """ 
    Sends the data to the satellite. 

    Returns: None
    """
    pass
def posRedundantBits(data, r):
    """ 
    Inserts redundant bits at positions that are powers of two in the data sequence. 

    Returns: str: Bit sequence with placeholders for redundant bits. 
    """
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r+1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
    return res[::-1]

def calcParityBits(arr, r):
    """ 
    Computes and inserts parity bits at their respective redundant positions in the sequence. 

    Returns: str: Bit sequence with calculated parity bits in place. 
    """
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr

def detectError(arr, nr):
    """ 
    Identifies the position of a single-bit error in the received Hamming Code sequence. 

    Returns: int: Position of the error (0 if no error is detected). 
    """
    n = len(arr)
    res = 0
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        res = res + val*(10**i)
    return int(str(res), 2)
def setupHamming(data):
    """ 
    Initializes the Hamming Code sequence with redundant bits and parity bits. 

    Returns: str: The Hamming Code sequence. 
    """
    m = len(data)
    r = calcRedundantBits(m)
    arr = posRedundantBits(data, r)
    arr = calcParityBits(arr, r)
    return arr
def currentAcceptable():
    """ 
    Checks if the current flow is within the safe limits. 

    Returns: bool: True if the current flow is within limits, False otherwise. 
    """
    return True
def storeData(data):
    """ 
    Stores the data in the database. 

    Returns: None
    """
    

    pass
AllData = {"Instrument": {}, "Temperature": {}, "Telemetry": {}}

while(1):
    if not currentAcceptable():
        pass # wait for current to be within limits
    InstrumentData = {"RIMFAX": [], "NSS": []}
    # Fetching data from the instruments
    for i in range(15):
        time.sleep(1000)
        RIMFAXdata = getRIMFAXData()
        RIMFAXdata = setupHamming(RIMFAXdata)
        NSSdata = getNSSData()
        NSSdata = setupHamming(NSSdata)
        InstrumentData["RIMFAX"].append(RIMFAXdata)
        InstrumentData["NSS"].append(NSSdata)
    AllData["Instrument"] = InstrumentData
    
    # Fetching temperature data
    TemperatureData = {"RIMFAX": [], "NSS": [], "Chassis": [], "Power": []}
    tempData = getTempData()
    for key in tempData:
        temp = tempData[key]
        temp = setupHamming(temp)
        TemperatureData[key].append(temp)
    AllData["Temperature"] = TemperatureData
    
    # Fetching data from the instruments
    for i in range(15):
        time.sleep(1000)
        RIMFAXdata = getRIMFAXData()
        RIMFAXdata = setupHamming(RIMFAXdata)
        NSSdata = getNSSData()
        NSSdata = setupHamming(NSSdata)
        InstrumentData["RIMFAX"].append(RIMFAXdata)
        InstrumentData["NSS"].append(NSSdata)
    AllData["Instrument"] = InstrumentData
    
    # Fetching temperature data
    TemperatureData = {"RIMFAX": [], "NSS": [], "Chassis": [], "Power": []}
    tempData = getTempData()
    for key in tempData:
        temp = tempData[key]
        temp = setupHamming(temp)
        TemperatureData[key].append(temp)
    AllData["Temperature"] = TemperatureData
    
    # Fetching telemetry data
    TelemetryData = {"RIMFAX": [], "NSS": [], "Chassis": [], "Power": [], "CDH": []}
    telemData = getTelemetryData()
    for key in tempData:
        telem= telemData[key]
        telem = setupHamming(telem)
        TelemetryData[key].append(temp)
    AllData["Telemetry"] = TelemetryData
    
    # Sending data to satellite
    if satelliteAbove():
        sendDataToSatellite(AllData)
        storeData(AllData)
        AllData = {"Instrument": {}, "Temperature": {}, "Telemetry": {}}
        
