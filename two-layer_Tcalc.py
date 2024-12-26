import math              as m 
import numpy             as np
import matplotlib.pyplot as plt

ea = float(input('E_a:'))
eb = float(input('E_b:'))

S0 = 1366.0
a  = 0.3

eTOA= S0/4 *(1-a)
TOA = m.sqrt(m.sqrt(eTOA/(5.67E-8)))

eTs = eTOA * ( (4-(ea*eb)) / ((2-ea)*(2-eb)) ) ##without+2*ea*eb
Ts  = m.sqrt(m.sqrt(eTs/(5.67E-8)))

eTa = eTs * ( (2-eb) / (4-ea*eb) )
Ta  = m.sqrt(m.sqrt(eTa/(5.67E-8)))

eTb = eTs * ( (2+ea-ea*eb) / (4-ea*eb) )
Tb  = m.sqrt(m.sqrt(eTb/(5.67E-8)))

print('my version')
print('Ta:', Ta)
print('Tb:', Tb)
print('Ts:', Ts, '\n')

eTOA= S0/4 *(1-a)
TOA = m.sqrt(m.sqrt(eTOA/(5.67E-8)))

eTs = eTOA * ( (4-(ea*eb)) / ((2-ea)*(2-eb)+2*ea*eb) ) ##+2*ea*eb
Ts  = m.sqrt(m.sqrt(eTs/(5.67E-8)))

eTa = eTs * ( (2-eb) / (4-ea*eb) )
Ta  = m.sqrt(m.sqrt(eTa/(5.67E-8)))

eTb = eTs * ( (2+ea-ea*eb) / (4-ea*eb) )
Tb  = m.sqrt(m.sqrt(eTb/(5.67E-8)))

print('functions of textbook')
print('Ta:', Ta)
print('Tb:', Tb)
print('Ts:', Ts)
