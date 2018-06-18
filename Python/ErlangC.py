import math
from bisect import bisect_left

def takeClosest(num,collection):
   return min(collection,key=lambda x:abs(x-num))

def calc_SummationEc(m, u):
    result = 0.0
    for i in range(0, m-1):
        result += math.pow(u, i) / math.factorial(i)
    return result

def AAR (calls):
    "Avarage Arrival Calls, P: Calls"
    result = 0.0
    result = calls/1800
    return result

def TI(calls, aht):
    "Traffic Intensity, P: Calls and AHT"
    result = 0.0
    ans = AAR(calls)
    result = ans*aht
    return result

def Utilisation(calls, aht, agents):
    "Agents Occupancy, P: Calls, AHT, # Agents"
    result = 0.0
    ans = TI(calls, aht)
    result = ans/agents
    return result


def ErlangC(calls, aht, agents):
    "ErlangC Factor, P: Calls, AHT, # Agents"
    result = 0.0
    ans1 = TI(calls, aht)
    ans2 = Utilisation(calls, aht, agents)
    result =(math.pow(ans1, agents)/math.factorial(agents))/((math.pow(ans1, agents)/math.factorial(agents))+(1-ans2)*calc_SummationEc(agents,ans1))
    return result

def ASA(calls, aht, agents):
    "Average Speed of Answer, P: Calls, AHT, #Agents"
    result = 0.0
    ans1 = ErlangC(calls, aht, agents)
    ans2 = Utilisation(calls, aht, agents)
    result = (ans1*aht)/(agents*(1-ans2))
    return result

def SLA(calls, aht, agents, t):
    "Service Level, P: Calls, AHT, #Agents, target time"
    result = 0.0
    ans1 = TI(calls, aht)
    result = (1-ErlangC(calls, aht, agents)*math.exp((ans1 - agents)*(t/aht)))
    return result

def Agents(calls, aht, SL, t):
    "This function will find the best number of agents for a given SLA"
    agts = []
    serv = []
    j = 1
    ans1 = 0.0
    while (ans1 < 0.99):
        ans1 = SLA(calls, aht, j, 15)
        serv.append(ans1)
        agts.append(j)
        j = j + 1
    result = agts[int(serv.index(takeClosest(SL,serv)))]
    return result
