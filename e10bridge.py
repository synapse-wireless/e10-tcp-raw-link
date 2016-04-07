'''E10 bridge script - show traffic status on the "A" LED'''

from synapse.platforms import *

GRN_LED = GPIO_0
RED_LED = GPIO_1

STAT_PKTSER_RX = 7
STAT_PKTSER_TX = 8
STAT_RADIO_RX  = 9
STAT_RADIO_TX  = 10

@setHook(HOOK_STARTUP)
def init():
    setPinDir(GRN_LED, True)
    setPinDir(RED_LED, True)
    
    writePin(GRN_LED, True)
    writePin(RED_LED, False)

@setHook(HOOK_100MS)
def tick():
    if getStat(STAT_RADIO_RX) > 0 or getStat(STAT_RADIO_TX) > 0:
        pulsePin(RED_LED, 50, True)

