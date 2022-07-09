#import needed tools
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as anim
import random



def Conversion_GPS_to_Coordinates(GPS_Coordinates:str)-> float:

    GPS_list = []
    GPS = None
    O_index = None
    m_index = None
    sec_index = None


    for x in range(len(GPS_Coordinates)):
        if GPS_Coordinates[x] == '°':
            O_index = x

        elif GPS_Coordinates[x] == '’':
            m_index = x

        elif GPS_Coordinates[x] == '”':
            sec_index =x

    GPS_list.append(GPS_Coordinates[0:O_index])
    GPS_list.append(GPS_Coordinates[(O_index+1):(m_index)])
    GPS_list.append(GPS_Coordinates[(m_index+1):(sec_index)])


    GPS = float(GPS_list[0]) + (float(GPS_list[1])/60) + (float(GPS_list[2])/3600)

    return GPS


GPS  ="121°8’10”"
print(Conversion_GPS_to_Coordinates(GPS))
