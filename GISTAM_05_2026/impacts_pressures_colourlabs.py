# -*- coding: utf-8 -*-
# Land_cover_plotting.py
"""
Plotting and animating Digital Earth Australia Land Cover data.

License: The code in this notebook is licensed under the Apache License,
Version 2.0 (https://www.apache.org/licenses/LICENSE-2.0). Digital Earth
Australia data is licensed under the Creative Commons by Attribution 4.0
license (https://creativecommons.org/licenses/by/4.0/).

Contact: If you need assistance, please post a question on the Open Data
Cube Slack channel (http://slack.opendatacube.org/) or on the GIS Stack
Exchange (https://gis.stackexchange.com/questions/ask?tags=open-data-cube)
using the `open-data-cube` tag (you can view previously asked questions
here: https://gis.stackexchange.com/questions/tagged/open-data-cube).

If you would like to report an issue with this script, you can file one
on Github (https://github.com/GeoscienceAustralia/dea-notebooks/issues/new).

Last modified: January 2022
"""

import numpy as np
import pandas as pd
import ast
import sys

from IPython.display import Image

import matplotlib.pyplot as plt
from matplotlib import colors as mcolours
from matplotlib import patheffects
from matplotlib.animation import FuncAnimation

# Define colour schemes for each land cover measurement
lc_colours = {    
    'impacts_colour_scheme': {0: (255, 255, 255, 255, "No change:0"),
                             1: (205, 133, 63, 255, "Accretion: 1)"),
                             2: (0, 255, 0, 255, "Algal bloom: 2)"),
                             3: (210, 105, 30, 255, "Algal dieback: 3)"),
                             4: (119, 63, 26, 255, "Bare soil exposure: 4)"),
                             5: (61, 7, 52, 255, "Blackwater event: 5)"),
                             6: (255, 228, 181, 255, "Browning (vegetation): 6)"),
                             7: (147, 112, 219, 255, "Building or infrastructure abandonment: 7)"),
                             8: (218, 165, 32, 255, "Compaction: 8)"),
                             9: (250, 250, 210, 255, "Coral bleaching: 9)"),
                            10: (199, 21, 133, 255, "Coral damage: 10)"),
                            11: (248, 131, 121, 255, "Coral recovery: 11)"),
                            12: (255, 182, 30, 255, "Crop change in cultivated lands: 12)"),
                            13: (184, 115, 51, 255, "Crop damage: 13)"),
                            14: (167, 252, 0, 255, "Crop establishment: 14)"),
                            15: (255, 240, 0, 255, "Cropland gain: 15)"),
                            16: (123, 63, 0, 255, "Cropland loss: 16)"),
                            17: (205, 149, 117, 255, "Deglaciation: 17)"),
                            18: (242, 240, 230, 255, "Desalinisation: 18)"),
                            19: (255, 174, 66, 255, "Desertification: 19)"),
                            20: (159, 129, 112, 255, "Elevation change: 20)"),
                            21: (150, 0, 24, 255, "Erosion: 21)"),
                            22: (111, 0, 255, 255, "Flooding: 22)"),
                            23: (141, 43, 11, 255, "Geomorphological change: 23)"),
                            24: (176, 224, 230, 255, "Glaciation: 24)"),
                            25: (154, 205, 50, 255, "Greening: 25)"),
                            26: (184, 134, 11, 255, "Increased sediment load: 26)"),
                            27: (30, 144, 255, 255, "Inundation: 27)"),
                            28: (207, 16, 32, 255, "Lava flow: 28)"),
                            29: (196, 98, 16, 255, "Leaf scorch: 29)"),
                            30: (179, 68, 108, 255, "Mine abandonment: 30)"),
                            31: (196, 174, 173, 255, "Mine expansion: 31)"),
                            32: (255, 218, 191, 255, "Natural surface gain: 32)"),
                            33: (102, 51, 153, 255, "Natural surface loss: 33)"),
                            34: (255, 250, 250, 255, "Net snow gain (amount): 34)"),
                            35: (182, 170, 153, 255, "Net snow loss (amount): 35)"),               
                            36: (245, 245, 245, 255, "Net snow gain (extent): 36)"),
                            37: (192, 192, 192, 255, "Net snow loss (extent): 37)"),
                            38: (255, 250, 240, 255, "Net snow gain (hydroperiod): 38)"),
                            39: (220, 220, 220, 255, "Net snow loss (hydroperiod): 39)"),
                            40: (218, 165, 32, 255, "Phenological change: 40)"),
                            41: (75, 0, 130, 255, "Railway or road abandonment: 41)"),
                            42: (240, 128, 128, 255, "Railway or road construction: 42)"),
                            43: (255, 165, 0, 255, "Receding Flood: 43)"),
                            44: (238, 130, 238, 255, "Salinisation: 44)"),
                            45: (176, 196, 222, 255, "Sea ice decrease: 45)"),
                            46: (215, 246, 245, 255, "Sea ice increase: 46)"),
                            47: (0, 139, 139, 255, "Sea level fall: 47)"),
                            48: (0, 191, 255, 255, "Sea level rise: 48)"),
                            49: (233, 150, 122, 255, "Sedimentation: 49)"),
                            50: (240, 255, 240, 255, "Sink hole: 50)"),
                            51: (240, 248, 255, 255, "Snow accumulation: 51)"),
                            52: (169, 169, 169, 255, "Snow melt: 52)"),
                            53: (199, 21, 133, 255, "Urban area loss: 53)"),
                            54: (159, 0, 255, 255, "Urban damage: 54)"),
                            55: (204, 152, 152, 255, "Urban decay: 55)"),
                            56: (229, 43, 80, 255, "Urban densification: 56)"),
                            57: (254, 111, 94, 255, "Urban development: 57)"),
                            58: (227, 66, 52, 255, "Urban growth: 58)"),
                            59: (255, 182, 193, 255, "Urban renewal: 59)"),
                            60: (204, 51, 51, 255, "Urban sprawl: 60)"),
                            61: (240, 96, 0, 255, "Vegetation damage: 61)"),
                            62: (255, 213, 128, 255, "Vegetation dieback: 62)"),
                            63: (99, 169, 80, 255, "Vegetation gain (amount): 63)"),
                            64: (1, 117, 94, 255, "Vegetation gain (extent): 64)"), 
                            65: (238, 232, 170, 255, "Vegetation health deterioration: 65)"),
                            66: (0, 204, 153, 255, "Vegetation health improvement: 66)"),
                            67: (255, 140, 0, 255, "Vegetation loss (extent): 67)"), 
                            68: (220, 140, 0, 255, "Vegetation reduction (amount): 68)"),
                            69: (178, 140, 0, 255, "Vegetation reduction in understorey (amount): 69)"),
                            70: (245, 255, 250, 255, "Vegetation species change: 70)"),
                            71: (175, 238, 238, 255, "Water depth decrease: 71)"),
                            72: (148, 0, 211, 255, "Water depth increase: 72)"),
                            73: (0, 255, 255, 255, "Water gain (extent): 73)"),
                            74: (255, 182, 193, 255, "Water loss (extent): 74)"),
                            75: (255, 255, 255, 255, "Water quality change: 75)")},
 
    'impacts_colour_scheme_labels': {0: (255, 255, 255, 255, "No change:0"),
                             1: (205, 133, 63, 255, "Accretion: 1)"),
                             2: (0, 255, 0, 255, "Algal bloom: 2)"),
                             3: (210, 105, 30, 255, "Algal dieback: 3)"),
                             4: (119, 63, 26, 255, "Bare soil exposure: 4)"),
                             5: (61, 7, 52, 255, "Blackwater event: 5)"),
                             6: (255, 228, 181, 255, "Browning (vegetation): 6)"),
                             7: (147, 112, 219, 255, "Building or infrastructure abandonment: 7)"),
                             8: (218, 165, 32, 255, "Compaction: 8)"),
                             9: (250, 250, 210, 255, "Coral bleaching: 9)"),
                            10: (199, 21, 133, 255, "Coral damage: 10)"),
                            11: (248, 131, 121, 255, "Coral recovery: 11)"),
                            12: (255, 182, 30, 255, "Crop change in cultivated lands: 12)"),
                            13: (184, 115, 51, 255, "Crop damage: 13)"),
                            14: (167, 252, 0, 255, "Crop establishment: 14)"),
                            15: (255, 240, 0, 255, "Cropland gain: 15)"),
                            16: (123, 63, 0, 255, "Cropland loss: 16)"),
                            17: (205, 149, 117, 255, "Deglaciation: 17)"),
                            18: (242, 240, 230, 255, "Desalinisation: 18)"),
                            19: (255, 174, 66, 255, "Desertification: 19)"),
                            20: (159, 129, 112, 255, "Elevation change: 20)"),
                            21: (150, 0, 24, 255, "Erosion: 21)"),
                            22: (111, 0, 255, 255, "Flooding: 22)"),
                            23: (141, 43, 11, 255, "Geomorphological change: 23)"),
                            24: (176, 224, 230, 255, "Glaciation: 24)"),
                            25: (154, 205, 50, 255, "Greening: 25)"),
                            26: (184, 134, 11, 255, "Increased sediment load: 26)"),
                            27: (30, 144, 255, 255, "Inundation: 27)"),
                            28: (207, 16, 32, 255, "Lava flow: 28)"),
                            29: (196, 98, 16, 255, "Leaf scorch: 29)"),
                            30: (179, 68, 108, 255, "Mine abandonment: 30)"),
                            31: (196, 174, 173, 255, "Mine expansion: 31)"),
                            32: (255, 218, 191, 255, "Natural surface gain: 32)"),
                            33: (102, 51, 153, 255, "Natural surface loss: 33)"),
                            34: (255, 250, 250, 255, "Net snow gain (amount): 34)"),
                            35: (182, 170, 153, 255, "Net snow loss (amount): 35)"),               
                            36: (245, 245, 245, 255, "Net snow gain (extent): 36)"),
                            37: (192, 192, 192, 255, "Net snow loss (extent): 37)"),
                            38: (255, 250, 240, 255, "Net snow gain (hydroperiod): 38)"),
                            39: (220, 220, 220, 255, "Net snow loss (hydroperiod): 39)"),
                            40: (218, 165, 32, 255, "Phenological change: 40)"),
                            41: (75, 0, 130, 255, "Railway or road abandonment: 41)"),
                            42: (240, 128, 128, 255, "Railway or road construction: 42)"),
                            43: (255, 165, 0, 255, "Receding Flood: 43)"),
                            44: (238, 130, 238, 255, "Salinisation: 44)"),
                            45: (176, 196, 222, 255, "Sea ice decrease: 45)"),
                            46: (215, 246, 245, 255, "Sea ice increase: 46)"),
                            47: (0, 139, 139, 255, "Sea level fall: 47)"),
                            48: (0, 191, 255, 255, "Sea level rise: 48)"),
                            49: (233, 150, 122, 255, "Sedimentation: 49)"),
                            50: (240, 255, 240, 255, "Sink hole: 50)"),
                            51: (240, 248, 255, 255, "Snow accumulation: 51)"),
                            52: (169, 169, 169, 255, "Snow melt: 52)"),
                            53: (199, 21, 133, 255, "Urban area loss: 53)"),
                            54: (159, 0, 255, 255, "Urban damage: 54)"),
                            55: (204, 152, 152, 255, "Urban decay: 55)"),
                            56: (229, 43, 80, 255, "Urban densification: 56)"),
                            57: (254, 111, 94, 255, "Urban development: 57)"),
                            58: (227, 66, 52, 255, "Urban growth: 58)"),
                            59: (255, 182, 193, 255, "Urban renewal: 59)"),
                            60: (204, 51, 51, 255, "Urban sprawl: 60)"),
                            61: (240, 96, 0, 255, "Vegetation damage: 61)"),
                            62: (255, 213, 128, 255, "Vegetation dieback: 62)"),
                            63: (99, 169, 80, 255, "Vegetation gain (amount): 63)"),
                            64: (1, 117, 94, 255, "Vegetation gain (extent): 64)"), 
                            65: (238, 232, 170, 255, "Vegetation health deterioration: 65)"),
                            66: (0, 204, 153, 255, "Vegetation health improvement: 66)"),
                            67: (255, 140, 0, 255, "Vegetation loss (extent): 67)"), 
                            68: (220, 140, 0, 255, "Vegetation reduction (amount): 68)"),
                            69: (178, 140, 0, 255, "Vegetation reduction in understorey (amount): 69)"),
                            70: (245, 255, 250, 255, "Vegetation species change: 70)"),
                            71: (175, 238, 238, 255, "Water depth decrease: 71)"),
                            72: (148, 0, 211, 255, "Water depth increase: 72)"),
                            73: (0, 255, 255, 255, "Water gain (extent): 73)"),
                            74: (255, 182, 193, 255, "Water loss (extent): 74)"),
                            75: (255, 255, 255, 255, "Water quality change: 75)")},

    'all_impacts_pressures_colour_scheme': {0: (255, 255, 255, 255, "No change"),
                                   1: (205, 133, 63, 255, "Accretion (sediment transport): 1111)"),
                                   2: (0, 255, 0, 255, "Algal bloom (eutrophication): 2036)"),
                                   3: (173, 255, 47, 255, "Algal bloom (high inland water temperatures): 2057)"),
                                   4: (124, 252, 0, 255, "Algal bloom (increased temperature): 2064)"),
                                   5: (210, 105, 30, 255, "Algal dieback (decreased temperature): 3026)"),
                                   6: (119, 63, 26, 255, "Bare soil exposure (burning): 4011)"),
                                   7: (244, 164, 96, 255, "Bare soil exposure (erosion): 4035)"),
                                   8: (184, 134, 11, 255, "Bare soil exposure (ploughing): 4091)"),
                                   9: (169, 169, 169, 255, "Bare soil exposure (tillage): 4126)"),
                                  10: (61, 7, 52, 255, "Blackwater event (inundation following extended drought): 5069)"),
                                  11: (255, 228, 181, 255, "Browning (vegetation) (decreased precipitation): 6025)"),
                                  12: (147, 112, 219, 255, "Building or infrastructure abandonment (dam removal): 7021)"),
                                  13: (123, 104, 238, 255, "Building or infrastructure abandonment (flooding): 7044)"),
                                  14: (70, 130, 180, 255, "Building or infrastructure abandonment (increased wind): 7066)"),
                                  15: (148, 0, 211, 255, "Building or infrastructure abandonment (urban fire): 7131)"),
                                  16: (218, 165, 32, 255, "Compaction (increased traffic): 8065)"),
                                  17: (240, 230, 140, 255, "Compaction (overgrazing (natural)): 8086)"),
                                  18: (222, 184, 135, 255, "Compaction (overgrazing (stock)): 8087)"),
                                  19: (250, 250, 210, 255, "Coral bleaching (increased acidity): 9059)"),
                                  20: (250, 240, 230, 255, "Coral bleaching (prolonged temperature increase): 9097)"),
                                  21: (199, 21, 133, 255, "Coral damage (invasive or exotic species): 10070)"),
                                  22: (255, 228, 225, 255, "Coral damage (pathogens): 10088)"),
                                  23: (255, 222, 173, 255, "Coral damage (sedimentation): 10112)"),
                                  24: (248, 131, 121, 255, "Coral recovery (decreased acidity): 11022)"),
                                  25: (255, 127, 80, 255, "Coral recovery (prolonged temperature decrease): 11096)"),
                                  26: (255, 182, 30, 255, "Crop change in cultivated lands (crop rotation): 12019)"),
                                  27: (184, 115, 51, 255, "Crop damage (drought): 13030)"),
                                  28: (205, 149, 117, 255, "Crop damage (excess precipitation): 13038)"),
                                  29: (145, 95, 109, 255, "Crop damage (excess rain): 13039)"),
                                  30: (18, 97, 128, 255, "Crop damage (flooding): 13044)"),
                                  31: (244, 164, 96, 255, "Crop damage (grazing (natural)): 13048)"),
                                  32: (160, 82, 45, 255, "Crop damage (grazing (stock)): 13049)"),
                                  33: (184, 125, 73, 255, "Crop damage (increased wind): 13066)"),
                                  34: (255, 218, 185, 255, "Crop damage (insect herbivory): 13067)"),
                                  35: (184, 115, 51, 255, "Crop damage (strong winds): 13120)"),
                                  36: (167, 252, 0, 255, "Crop establishment (planting): 14090)"),
                                  37: (255, 240, 0, 255, "Cropland gain (agricultural expansion): 15003)"),
                                  38: (255, 182, 30, 255, "Cropland gain (farmland creation): 15042)"),
                                  39: (123, 63, 0, 255, "Cropland loss (agricultural loss): 16004)"),
                                  40: (88, 41, 0, 255, "Cropland loss (animal stock change): 16007)"),
                                  41: (204, 119, 34, 255, "Cropland loss (fallowing): 16040)"),
                                  42: (138, 121, 93, 255, "Cropland loss (farmland abandonment): 16041)"),
                                  43: (245, 222, 179, 255, "Cropland loss (idle or fallow in rotation): 16058)"),
                                  44: (205, 149, 117, 255, "Deglaciation (prolonged temperature increase): 17097)"),
                                  45: (242, 240, 230, 255, "Desalinisation (gypsum application): 18054)"),
                                  46: (255, 174, 66, 255, "Desertification (prolonged temperature increase): 19097)"),
                                  47: (159, 129, 112, 255, "Elevation change (deposition): 20028)"),
                                  48: (222, 184, 135, 255, "Elevation change (earthquake): 20032)"),
                                  49: (255, 228, 196, 255, "Elevation change (landslide): 20073)"),
                                  50: (210, 105, 30, 255, "Elevation change (mining): 20080)"),
                                  51: (119, 63, 26, 255, "Elevation change (subsidence): 20122)"),
                                  52: (170, 64, 105, 255, "Elevation change (waste dumping): 20138)"),
                                  53: (150, 0, 24, 255, "Erosion (construction): 21016)"),
                                  54: (145, 95, 109, 255, "Erosion (excess precipitation): 21038)"),
                                  55: (162, 162, 208, 255, "Erosion (frost): 21046)"),
                                  56: (212, 112, 162, 255, "Erosion (increased traffic): 21065)"),
                                  57: (153, 102, 204, 255, "Erosion (increased wind): 21066)"),
                                  58: (162, 173, 208, 255, "Erosion (sea level fluctuation): 21110)"),
                                  59: (115, 54, 53, 255, "Erosion (topsoil removal): 21127)"),
                                  60: (26, 72, 118, 255, "Erosion (water movement change): 21140)"),
                                  61: (106, 90, 205, 255, "Erosion (wave action): 21139)"),
                                  62: (111, 0, 255, 255, "Flooding (excess rain): 22039)"),
                                  63: (135, 206, 235, 255, "Flooding (excess snow): 22123)"),
                                  64: (141, 43, 11, 255, "Geomorphological change (mining): 23080)"),
                                  65: (176, 224, 230, 255, "Glaciation (prolonged temperature decrease): 24096)"),
                                  66: (154, 205, 50, 255, "Greening (increased precipitation): 25063)"),
                                  67: (184, 134, 11, 255, "Increased sediment load (sediment transport): 26111)"),
                                  68: (30, 144, 255, 255, "Inundation (flooding): 27044)"),
                                  69: (0, 206, 209, 255, "Inundation (sea level fluctuation): 27068)"),
                                  70: (207, 16, 32, 255, "Lava flow (volcanic eruption): 28137)"),
                                  71: (196, 98, 16, 255, "Leaf scorch (strong winds): 29120)"),
                                  72: (179, 68, 108, 255, "Mine abandonment (reduced investment): 30098)"),
                                  73: (196, 174, 173, 255, "Mine expansion (increased investment): 31061)"),
                                  74: (255, 218, 191, 255, "Natural surface gain (deposition): 32028)"),
                                  75: (240, 230, 140, 255, "Natural surface gain (urban rehabilitation): 32133)"),
                                  76: (102, 51, 153, 255, "Natural surface loss (mining): 33080)"),
                                  77: (255, 250, 250, 255, "Net snow gain (amount) (snowfall): 34121)"),
                                  78: (119, 136, 153, 255, "Net snow loss (amount) (snowmelt): 35123)"),
                                  79: (245, 245, 245, 255, "Net snow gain (extent) (snowfall): 36116)"),
                                  80: (192, 192, 192, 255, "Net snow loss (extent) (snowmelt): 37117)"),
                                  81: (255, 250, 240, 255, "Net snow gain (hydroperiod) (prolonged temperature decrease): 38096)"),
                                  82: (220, 220, 220, 255, "Net snow loss (hydroperiod) (prolonged temperature increase): 39097)"),
                                  83: (218, 165, 32, 255, "Phenological change (natural diurnal and seasonal cycles): 40082)"),
                                  84: (75, 0, 130, 255, "Railway or road abandonment (reduced investment): 41098)"),
                                  85: (240, 128, 128, 255, "Railway or road construction (increased investment): 42061)"),
                                  86: (255, 165, 0, 255, "Receding Flood (reduced runoff post flood): 43100)"),
                                  87: (221, 160, 221, 255, "Salinisation (evaporation): 44037)"),
                                  88: (238, 130, 238, 255, "Salinisation (sea level fluctuation): 44110)"),
                                  89: (176, 196, 222, 255, "Sea ice decrease (prolonged temperature increase): 45097)"),
                                  90: (255, 255, 255, 255, "Sea ice increase (prolonged temperature decrease): 46096)"),
                                  91: (0, 139, 139, 255, "Sea level fall (ocean-atmosphere oscillations): 47085)"),
                                  92: (0, 191, 255, 255, "Sea level rise (melting ice sheets/glaciers): 48076)"),
                                  93: (32, 178, 170, 255, "Sea level rise (thermal expansion): 48124)"),
                                  94: (233, 150, 122, 255, "Sedimentation (dredging): 49029)"),
                                  95: (240, 255, 240, 255, "Sink hole (subsidence): 50122)"),
                                  96: (240, 248, 255, 255, "Snow accumulation (snowfall): 51116)"),
                                  97: (169, 169, 169, 255, "Snow melt (increased temperature): 52064)"),
                                  98: (199, 21, 133, 255, "Urban area loss (earthquake): 53032)"),
                                  99: (90, 79, 207, 255, "Urban area loss (flooding): 53044)"),
                                 100: (70, 130, 180, 255, "Urban area loss (tropical cyclone): 53128)"),
                                 101: (159, 0, 255, 255, "Urban damage (flooding): 54044)"),
                                 102: (200, 80, 155, 255, "Urban damage (increased wind): 54066)"),
                                 103: (90, 79, 207, 255, "Urban damage (urban fire): 54131)"),
                                 104: (156, 81, 182, 255, "Urban decay (dam failure): 55020)"),
                                 105: (147, 112, 219, 255, "Urban decay (mine abandonment): 55077)"),
                                 106: (105, 53, 156, 255, "Urban decay (subsidence): 55122)"),
                                 107: (229, 43, 80, 255, "Urban densification (construction): 56016)"),
                                 108: (254, 111, 94, 255, "Urban development (levelling): 57074)"),
                                 109: (227, 66, 52, 255, "Urban growth (construction): 58016)"),
                                 110: (255, 182, 193, 255, "Urban renewal (repairing damage): 59107)"),
                                 111: (204, 51, 51, 255, "Urban sprawl (construction): 60016)"),
                                 112: (236, 88, 0, 255, "Vegetation damage (bushfire): 61012)"),
                                 113: (21, 96, 189, 255, "Vegetation damage (excess precipitation): 61038)"),
                                 114: (25, 25, 112, 255, "Vegetation damage (excess rain): 61039)"),
                                 115: (216, 191, 216, 255, "Vegetation damage (flooding): 61044)"),
                                 116: (124, 185, 232, 255, "Vegetation damage (frost): 61046)"),
                                 117: (110, 174, 161, 255, "Vegetation damage (increased wind): 61066)"),
                                 118: (220, 20, 60, 255, "Vegetation damage (mechanical intervention): 61075)"),
                                 119: (255, 130, 67, 255, "Vegetation damage (prescribed burn): 61093)"),
                                 120: (170, 240, 209, 255, "Vegetation damage (prolonged snow cover): 61095)"),
                                 121: (255, 69, 0, 255, "Vegetation damage (severe thunderstorm): 61114)"),
                                 122: (255, 228, 225, 255, "Vegetation damage (strong winds): 61120)"),
                                 123: (128, 255, 159, 255, "Vegetation dieback (anchoring): 62006)"),
                                 124: (64, 224, 208, 255, "Vegetation dieback (cold snap): 62014)"),
                                 125: (234, 215, 160, 255, "Vegetation dieback (drought): 62030)"),
                                 126: (255, 215, 0, 255, "Vegetation dieback (heatwave): 62056)"),
                                 127: (196, 195, 208, 255, "Vegetation dieback (increased wind): 62066)"),
                                 128: (252, 108, 133, 255, "Vegetation dieback (non-insect herbivory (natural)): 62083)"),
                                 129: (250, 235, 215, 255, "Vegetation dieback (pathogens): 62088)"),
                                 130: (255, 53, 94, 255, "Vegetation dieback (pollution): 62092)"),
                                 131: (18, 97, 128, 255, "Vegetation dieback (prolonged inundation): 62094)"),
                                 132: (234, 224, 200, 255, "Vegetation dieback (prolonged snow cover): 62095)"),
                                 133: (78, 130, 180, 255, "Vegetation dieback (sea level fluctuation): 62110)"),
                                 134: (255, 235, 205, 255, "Vegetation dieback (soil salinisation): 62118)"),
                                 135: (231, 172, 207, 255, "Vegetation dieback (water salinisation): 62141)"),
                                 136: (99, 169, 80, 255, "Vegetation gain (amount) (afforestation): 63002)"),
                                 137: (128, 128, 0, 255, "Vegetation gain (amount) (bushfire recovery): 63013)"),
                                 138: (0, 255, 127, 255, "Vegetation gain (amount) (ecological restoration): 63033)"),
                                 139: (86, 130, 3, 255, "Vegetation gain (amount) (encroachment): 63034)"),
                                 140: (168, 228, 160, 255, "Vegetation gain (amount) (farmland abandonment): 63041)"),
                                 141: (78, 135, 32, 255, "Vegetation gain (amount) (fertiliser application): 63043)"),
                                 142: (127, 255, 0, 255, "Vegetation gain (amount) (growth): 63053)"),
                                 143: (250, 250, 210, 255, "Vegetation gain (amount) (reduced or cessation of grazing): 63099)"),
                                 144: (48, 186, 143, 255, "Vegetation gain (amount) (reforestation (natural)): 63102)"),
                                 145: (43, 93, 52, 255, "Vegetation gain (amount) (reforestation (plantations)): 63103)"),
                                 146: (147, 197, 114, 255, "Vegetation gain (amount) (regrowth): 63104)"),
                                 147: (176, 191, 26, 255, "Vegetation gain (amount) (removal of herbivores): 63106)"),
                                 148: (209, 226, 49, 255, "Vegetation gain (amount) (revegetation): 63108)"),
                                 149: (215, 59, 62, 255, "Vegetation gain (amount) (thinning): 63125)"),
                                 150: (0, 127, 92, 255, "Vegetation gain (amount) (urban greening): 63132)"),
                                 151: (133, 117, 78, 255, "Vegetation gain (amount) (vegetation thickening): 63136)"),
                                 152: (0, 117, 94, 255, "Vegetation gain (extent) (afforestation): 64002)"),
                                 153: (0, 255, 0, 255, "Vegetation gain (extent) (colonisation): 64015)"),
                                 154: (0, 73, 83, 255, "Vegetation gain (extent) (decreased wave action): 64027)"),
                                 155: (0, 128, 0, 255, "Vegetation gain (extent) (ecological restoration): 64033)"),
                                 156: (124, 252, 0, 255, "Vegetation gain (extent) (greenspace construction): 64050)"),
                                 157: (34, 139, 34, 255, "Vegetation gain (extent) (mine site rehabilitation): 64078)"),
                                 158: (50, 205, 50, 255, "Vegetation gain (extent) (planting): 64090)"),
                                 159: (0, 128, 128, 255, "Vegetation gain (extent) (rehabilitation): 64105)"),
                                 160: (0, 100, 0, 255, "Vegetation gain (extent) (revegetation): 64108)"),
                                 161: (255, 245, 238, 255, "Vegetation gain (extent) (snowmelt): 64117)"),
                                 162: (238, 232, 170, 255, "Vegetation health deterioration (abandonment of fertilizer application): 65001)"),
                                 163: (245, 245, 220, 255, "Vegetation health deterioration (decreased nutrient supply in soil): 65024)"),
                                 164: (0, 204, 153, 255, "Vegetation health improvement (fertiliser application): 66043)"),
                                 165: (103, 146, 103, 255, "Vegetation health improvement (increased nutrient supply in soil): 66065)"),
                                 166: (227, 11, 92, 255, "Vegetation health improvement (irrigation): 66071)"),
                                 167: (255, 140, 0, 255, "Vegetation loss (extent) (bushfire): 67012)"),
                                 168: (255, 0, 0, 255, "Vegetation loss (extent) (deforestation): 67027)"),
                                 169: (61, 7, 52, 255, "Vegetation loss (extent) (drought): 67030)"),
                                 170: (255, 250, 205, 255, "Vegetation loss (extent) (excess rain): 67039)"),
                                 171: (105, 105, 105, 255, "Vegetation loss (extent) (farmland abandonment): 67041)"),
                                 172: (46, 45, 136, 255, "Vegetation loss (extent) (flooding): 67044)"),
                                 173: (255, 255, 0, 255, "Vegetation loss (extent) (land reclamation): 67072)"),
                                 174: (25, 25, 112, 255, "Vegetation loss (extent) (sea defence construction): 67109)"),
                                 175: (255, 0, 255, 255, "Vegetation loss (extent) (severe thunderstorm): 67114)"),
                                 176: (255, 20, 147, 255, "Vegetation loss (extent) (strong winds): 67120)"),
                                 177: (138, 43, 226, 255, "Vegetation loss (extent) (vegetation clearance): 67135)"),
                                 178: (127, 255, 212, 255, "Vegetation loss (extent) (wave action): 67139)"),
                                 179: (255, 140, 0, 255, "Vegetation reduction (amount) (bushfire): 68012)"),
                                 180: (250, 240, 230, 255, "Vegetation reduction (amount) (coppicing): 68018)"),
                                 181: (139, 0, 0, 255, "Vegetation reduction (amount) (decreased nutrient supply in soil): 68024)"),
                                 182: (128, 128, 128, 255, "Vegetation reduction (amount) (farmland abandonment): 68041)"),
                                 183: (165, 42, 42, 255, "Vegetation reduction (amount) (fuelwood collection): 68047)"),
                                 184: (139, 0, 139, 255, "Vegetation reduction (amount) (harvesting): 68055)"),
                                 185: (252, 108, 133, 255, "Vegetation reduction (amount) (insect herbivory): 68067)"),
                                 186: (255, 163, 67, 255, "Vegetation reduction (amount) (mowing): 68081)"),
                                 187: (255, 160, 0, 255, "Vegetation reduction (amount) (non-insect herbivory (natural)): 68083)"),
                                 188: (227, 37, 107, 255, "Vegetation reduction (amount) (overgrazing (natural)): 68086)"),
                                 189: (217, 0, 0, 255, "Vegetation reduction (amount) (overgrazing (stock)): 68087)"),
                                 190: (255, 160, 122, 255, "Vegetation reduction (amount) (pesticide application): 68093)"),
                                 191: (255, 99, 71, 255, "Vegetation reduction (amount) (prescribed burn): 68093)"),
                                 192: (226, 114, 91, 255, "Vegetation reduction (amount) (sedimentation): 68112)"),
                                 193: (255, 105, 180, 255, "Vegetation reduction (amount) (selective logging): 68113)"),
                                 194: (182, 49, 108, 255, "Vegetation reduction (amount) (stubble burn): 68121)"),
                                 195: (178, 34, 34, 255, "Vegetation reduction (amount) (thinning): 68125)"),
                                 196: (255, 105, 180, 255, "Vegetation reduction in understorey (amount) (grazing (natural)): 69048)"),
                                 197: (227, 11, 92, 255, "Vegetation reduction in understorey (amount) (grazing (stock)): 69049)"),
                                 198: (200, 162, 200, 255, "Vegetation reduction in understorey (amount) (non-insect herbivory (natural)): 69083)"),
                                 199: (245, 255, 250, 255, "Vegetation species change (amenity development): 70005)"),
                                 200: (85, 93, 80, 255, "Vegetation species change (atmospheric deposition): 70010)"),
                                 201: (232, 97, 0, 255, "Vegetation species change (burning): 70011)"),
                                 202: (252, 90, 141, 255, "Vegetation species change (control of invasive or exotic species): 70017)"),
                                 203: (244, 164, 96, 255, "Vegetation species change (decreased acidity): 70022)"),
                                 204: (65, 105, 225, 255, "Vegetation species change (decreased alkalinity): 70023)"),
                                 205: (255, 160, 122, 255, "Vegetation species change (decreased nutrient supply in soil): 70024)"),
                                 206: (95, 158, 160, 255, "Vegetation species change (flooding): 70044)"),
                                 207: (255, 255, 224, 255, "Vegetation species change (grazing (natural)): 70048)"),
                                 208: (255, 67, 164, 255, "Vegetation species change (grazing (stock)): 70049)"),
                                 209: (139, 69, 19, 255, "Vegetation species change (ground water extraction): 70051)"),
                                 210: (28, 169, 201, 255, "Vegetation species change (ground water recharge): 70052)"),
                                 211: (255, 105, 180, 255, "Vegetation species change (increased acidity): 70059)"),
                                 212: (153, 50, 204, 255, "Vegetation species change (increased alkalinity): 70060)"),
                                 213: (173, 255, 47, 255, "Vegetation species change (increased nutrient supply in soil): 70062)"),
                                 214: (128, 0, 32, 255, "Vegetation species change (invasive/exotic species): 70070)"),
                                 215: (255, 192, 203, 255, "Vegetation species change (overgrazing (natural)): 70086)"),
                                 216: (250, 128, 114, 255, "Vegetation species change (overgrazing (stock)): 70087)"),
                                 217: (255, 255, 240, 255, "Vegetation species change (pathogens): 70088)"),
                                 218: (255, 248, 220, 255, "Vegetation species change (pesticide application): 70089)"),
                                 219: (203, 65, 84, 255, "Vegetation species change (pollution): 70092)"),
                                 220: (218, 112, 214, 255, "Vegetation species change (prolonged inundation): 70094)"),
                                 221: (60, 179, 113, 255, "Vegetation species change (succession): 70123)"),
                                 222: (255, 228, 181, 255, "Vegetation species change (undergrazing (natural)): 70129)"),
                                 223: (255, 222, 173, 255, "Vegetation species change (undergrazing (stock)): 70130)"),
                                 224: (175, 238, 238, 255, "Water depth decrease (abstraction): 71001)"),
                                 225: (47, 79, 79, 255, "Water depth decrease (dam failure): 71020)"),
                                 226: (72, 61, 139, 255, "Water depth decrease (dam removal): 71021)"),
                                 227: (65, 74, 76, 255, "Water depth decrease (deposition): 71028)"),
                                 228: (72, 209, 204, 255, "Water depth decrease (evaporation): 71037)"),
                                 229: (148, 0, 211, 255, "Water depth increase (construction): 72016)"),
                                 230: (240, 255, 255, 255, "Water depth increase (dredging): 72029)"),
                                 231: (65, 102, 245, 255, "Water depth increase (flooding): 72044)"),
                                 232: (143, 188, 143, 255, "Water depth increase (sea level fluctuation): 72110)"),
                                 233: (173, 216, 230, 255, "Water depth increase (snowmelt): 72117)"),
                                 234: (0, 255, 255, 255, "Water gain (extent) (aquaculture expansion): 73008)"),
                                 235: (0, 0, 139, 255, "Water gain (extent) (excess precipitation): 73038)"),
                                 236: (65, 105, 225, 255, "Water gain (extent) (flooding): 73044)"),
                                 237: (100, 149, 237, 255, "Water gain (extent) (storm surge): 73119)"),
                                 238: (102, 205, 170, 255, "Water gain (extent) (wetland restoration and/or construction): 73144)"),
                                 239: (255, 182, 193, 255, "Water loss (extent) (aquaculture loss): 74009)"),
                                 240: (211, 211, 211, 255, "Water loss (extent) (drying): 74031)"),
                                 241: (123, 104, 238, 255, "Water loss (extent) (land reclamation): 74072)"),
                                 242: (253, 245, 230, 255, "Water loss (extent) (reduced snowfall): 74101)"),
                                 243: (128, 0, 0, 255, "Water loss (extent) (wetland drainage): 74143)"),
                                 244: (255, 0, 255, 255, "Water quality change (fracking): 75048)"),
                                 245: (135, 66, 31, 255, "Water quality change (nutrification): 75086)"),
                                 246: (209, 226, 49, 255, "Water quality change (pollution): 75094)")},
}

def make_colorbar(fig, ax, measurement, horizontal=False, animation=False):
    """
    Adds a new colorbar with appropriate land cover colours and labels.

    For DEA Land Cover Level 4 data, this function must be used with a double plot. 
    The 'ax' should be on the left side of the figure, and the colour bar will added 
    on the right hand side.
    
    Parameters
    ----------
    fig : matplotlib figure
        Figure to add colourbar to
    ax : matplotlib ax
        Matplotlib figure ax to add colorbar to.
    measurement : str
        Land cover measurement to use for colour map and labels. 
    
    """
    # Create new axis object for colorbar
    # parameters for add_axes are [left, bottom, width, height], in
    # fractions of total plot
    
    if measurement == 'impacts_colour_scheme' and animation == True:
        
        # special spacing settings for level 4
        cax = fig.add_axes([0.62, 0.10, 0.02, 0.80])
        orient = 'vertical'
        
            # get level 4 colour bar colour map ect
        cb_cmap, cb_norm, cb_labels, cb_ticks = lc_colourmap('impacts_colour_scheme_labels',
                                                         colour_bar=True)
    elif measurement == 'impacts_colour_scheme' and animation == False:
        
        # get level 4 colour bar colour map ect
        cb_cmap, cb_norm, cb_labels, cb_ticks = lc_colourmap('impacts_colour_scheme_labels',
                                                         colour_bar=True)
        #move plot over to make room for colourbar
        fig.subplots_adjust(right=0.825)

        # Settings for axis positions
        cax = fig.add_axes([0.84, 0.15, 0.02, 0.70])
        orient = 'vertical'
        
    else:
        #for all other measurements 

        #move plot over to make room for colourbar
        fig.subplots_adjust(right=0.825)

        # Settings for different axis positions
        if horizontal:
            cax = fig.add_axes([0.02, 0.05, 0.90, 0.03])
            orient = 'horizontal'
        else:
            cax = fig.add_axes([0.84, 0.15, 0.02, 0.70])
            orient = 'vertical'
            
        # get measurement colour bar colour map ect
        cb_cmap, cb_norm, cb_labels, cb_ticks = lc_colourmap(measurement,
                                                         colour_bar=True)

    img = ax.imshow([cb_ticks], cmap=cb_cmap, norm=cb_norm)
    cb = fig.colorbar(img, cax=cax, orientation=orient)

    cb.ax.tick_params(labelsize=12)
    cb.set_ticks(cb_ticks + np.diff(cb_ticks, append=cb_ticks[-1]+1) / 2)
    cb.set_ticklabels(cb_labels)



def lc_colourmap(colour_scheme, colour_bar=False):
    """
    Returns colour map and normalisation for the provided DEA Land Cover
    measurement, for use in plotting with Matplotlib library
    
    Parameters
    ----------
    colour_scheme : string
        Name of land cover colour scheme to use
        Valid options: 'level3', 'level4', 'lifeform_veg_cat_l4a', 
        'canopyco_veg_cat_l4d', 'watersea_veg_cat_l4a_au',
        'waterstt_wat_cat_l4a', 'inttidal_wat_cat_l4a', 
        'waterper_wat_cat_l4d_au', 'baregrad_phy_cat_l4d_au'.
    colour_bar : bool, optional
        Controls if colour bar labels are returned as a list for 
        plotting a colour bar. Default: False.
        
    Returns
    ---------
    cmap : matplotlib colormap
        Matplotlib colormap containing the colour scheme for the
        specified DEA Land Cover measurement.
    norm : matplotlib colormap index
        Matplotlib colormap index based on the discrete intervals of the
        classes in the specified DEA Land Cover measurement. Ensures the
        colormap maps the colours to the class numbers correctly.
    cblables : array
        A two dimentional array containing the numerical class values
        (first dim) and string labels (second dim) of the classes found
        in the chosen DEA Land Cover measurement.
    """

    colour_scheme = colour_scheme.lower()
    # Ensure a valid colour scheme was requested
#     try:
    assert (colour_scheme in lc_colours.keys(
    )), f'colour scheme must be one of [{lc_colours.keys()}] (got "{colour_scheme}")'

#     ('The dataset provided does not have a valid '
#     'name. Please specify which DEA Landcover measurement is being plotted '
#     'by providing the name using the "measurement" variable. For example (measurement = "full_classification")')

    # Get colour definitions
    lc_colour_scheme = lc_colours[colour_scheme]

    # Create colour map
    colour_arr = []
    for key, value in lc_colour_scheme.items():
        colour_arr.append(np.array(value[:-2]) / 255)

    cmap = mcolours.ListedColormap(colour_arr)
    bounds = list(lc_colour_scheme)

    # if colour_bar == True:
    #     if colour_scheme == 'level4':
    #         # Set colour labels to shortened level 4 list
    #         lc_colour_scheme = lc_colours['level4_colourbar_labels']
    #     cb_ticks = list(lc_colour_scheme)
    #     cb_labels = []
    #     for x in cb_ticks:
    #         cb_labels.append(lc_colour_scheme[x][4])


    if colour_bar == True:
        if colour_scheme == 'impacts_colour_scheme':
            # Set colour labels to shortened level 4 list
            lc_colour_scheme = lc_colours['impacts_colour_scheme_labels']
        cb_ticks = list(lc_colour_scheme)
        cb_labels = []
        for x in cb_ticks:
            cb_labels.append(lc_colour_scheme[x][4])

    bounds.append(bounds[-1]+1)
    norm = mcolours.BoundaryNorm(np.array(bounds), cmap.N)

    if colour_bar == False:
        return (cmap, norm)
    else:
        return (cmap, norm, cb_labels, cb_ticks)


def plot_land_cover(data, year=None, measurement=None, out_width=15, cols=4, ax=None):
    
    measurement = get_layer_name(measurement, data)

    cmap, norm = lc_colourmap(measurement)

    height, width = data.geobox.shape
    scale = out_width / width

    if year:
        year_string = f"{year}-01-01"
        data = data.sel(time=year_string, method="nearest")

        if ax is None:
            fig, ax = plt.subplots()
            fig.set_size_inches(width * scale, height * scale)
            make_colorbar(fig, ax, measurement)
        else:
            fig = ax.figure

        im = ax.imshow(data, cmap=cmap, norm=norm, interpolation="nearest")

    return im


def lc_animation(
        da,
        file_name="default_animation",
        measurement=None,
        stacked_plot=False,
        colour_bar=False,
        animation_interval=500,
        width_pixels=10,
        dpi=150,
        font_size=15,
        label_ax=True):
    """
    Creates an animation of DEA Landcover though time beside 
    corresponding stacked plots of the landcover classes. Saves the
    animation to a file and displays the animation in notebook.
    
    Parameters
    ----------
    da : xarray.DataArray
        An xarray.DataArray containing a multi-date stack of 
        observations of a single landcover level.
    file_name: string, optional.
        string used to create filename for saved animation file.
        Default: "default_animation" code adds .gif suffix.
    measurement : string, optional
        Name of the DEA land cover classification to be plotted. Passed to 
        lc_colourmap to specify which colour scheme will ve used. If non 
        provided, reads data array name from `da` to determine.
    stacked_plot: boolean, optional
        Determines if a stacked plot showing the percentage of area
        taken up by each class in each time slice is added to the
        animation. Default: False.
    colour_bar : boolean, Optional
        Determines if a colour bar is generated for the stand alone 
        animation. This is NOT recommended for use with level 4 data. 
        Does not work with stacked plot. Default: False.
    animation_interval : int , optional
        How quickly the frames of the animations should be re-drawn. 
        Default: 500.
    width_pixels : int, optional
        How wide in pixles the animation plot should be. Default: 10.
    dpi : int, optional
        Stands for 'Dots Per Inch'. Passed to the fuction that saves the
        animation and determines the resolution. A higher number will
        produce a higher resolution image but a larger file size and
        slower processing. Default: 150.
    font_size : int, optional. 
        Controls the size of the text which indicates the year
        displayed. Default: 15.
    label_ax : boolean, optional
        Determines if animation plot should have tick marks and numbers
        on axes. Also removes white space around plot. default: True
        
    Returns
    -------
    A GIF (.gif) animation file.
    """

    def calc_class_ratio(da):
        """
        Creates a table listing year by year what percentage of the
        total area is taken up by each class.
        Parameters
        ----------
        da : xarray.DataArray with time dimension
        Returns
        -------
        Pandas Dataframe : containing class percentages per year
        """

        # list all class codes in dataset
        list_classes = (np.unique(da, return_counts=False)).tolist()

        # create empty dataframe & dictionary
        ratio_table = pd.DataFrame(data=None, columns=list_classes)
        date_line = {}

        # count all pixels, should be consistent
        total_pix = int(np.sum(da.isel(time=1)))

        # iterate through each year in dataset
        for i in range(0, len(da.time)):
            date = str(da.time[i].data)[0:10]

            # for each year iterate though each present class number
            # and count pixels
            for n in list_classes:
                number_of_pixles = int(np.sum(da.isel(time=i) == n))
                percentage = number_of_pixles / total_pix * 100
                date_line[n] = percentage

            # add each year's counts to dataframe
            ratio_table.loc[date] = date_line

        return ratio_table

    def rgb_to_hex(r, g, b):
        hex = "#%x%x%x" % (r, g, b)
        if len(hex) < 7:
            hex = "#0" + hex[1:]
        return hex

    measurement = get_layer_name(measurement, da)

    # Add gif to end of filename
    file_name = file_name + ".gif"

        # Create colour map and normalisation for specified lc measurement
    try:
        layer_cmap, layer_norm, cb_labels, cb_ticks = lc_colourmap(
            measurement, colour_bar=True)
    except AssertionError:

        raise KeyError(f'Could not automatically determine colour scheme from '
                   f'DataArray name {measurement}. Please specify which '
                   'DEA Landcover measurement is being plotted by providing '
                   'the name using the "measurement" variable For example '
                   '(measurement = "full_classification")')
    
    # Prepare variables needed
    # Get info on dataset dimensions
    height, width = da.geobox.shape
    scale = width_pixels / width
    left, bottom, right, top = da.geobox.extent.boundingbox
    extent = [left, right, bottom, top]

    outline = [patheffects.withStroke(linewidth=2.5, foreground="black")]
    annotation_defaults = {
        "xy": (1, 1),
        "xycoords": "axes fraction",
        "xytext": (-5, -5),
        "textcoords": "offset points",
        "horizontalalignment": "right",
        "verticalalignment": "top",
        "fontsize": font_size,
        "color": "white",
        "path_effects": outline,
    }

    # Get information needed to display the year in the top corner
    times_list = da.time.dt.strftime("%Y").values
    text_list = [False] * len(times_list)
    annotation_list = ["\n".join([str(i) for i in (a, b) if i])
                       for a, b in zip(times_list, text_list)]

    if stacked_plot == True:
        


        # Create table for stacked plot
        stacked_plot_table = calc_class_ratio(da)

        # Build colour list of hex vals for stacked plot
        hex_colour_list = []
        colour_def = lc_colours[measurement]

        # Custom error message to help if user puts incorrect measurement name
        for val in list(stacked_plot_table):
            try:
                r, g, b = colour_def[val][0:3]
            except KeyError:
                raise KeyError(
                    "class number not found in colour definition. "
                    "Ensure measurement name provided matches the dataset being used")
            hex_val = rgb_to_hex(r, g, b)
            hex_colour_list.append(hex_val)

        # Define & set up figure
        fig, (ax1, ax2) = plt.subplots(1, 2, dpi=dpi, constrained_layout=True)
        fig.set_size_inches(width * scale * 2, height * scale, forward=True)
        fig.set_constrained_layout_pads(
            w_pad=0.2, h_pad=0.2, hspace=0, wspace=0)

        # This function is called at regular intervals with changing i
        # values for each frame
        def _update_frames(i, ax1, ax2, extent, annotation_text,
                           annotation_defaults, cmap, norm):
            # Clear previous frame to optimise render speed and plot imagery
            ax1.clear()
            ax2.clear()

            ax1.imshow(da[i, ...], cmap=cmap, norm=norm,
                       extent=extent, interpolation="nearest")
            if(not label_ax):
                ax1.set_axis_off()

            clipped_table = stacked_plot_table.iloc[: int(i + 1)]
            data = clipped_table.to_dict(orient="list")
            date = clipped_table.index

            ax2.stackplot(date, data.values(), colors=hex_colour_list)
            ax2.tick_params(axis="x", labelrotation=-45)
            ax2.margins(x=0, y=0)

            # Add annotation text
            ax1.annotate(annotation_text[i], **annotation_defaults)
            ax2.annotate(annotation_text[i], **annotation_defaults)

        # anim_fargs contains all the values we send to our
        # _update_frames function.
        # Note the layer_cmap and layer_norm which were calculated
        # earlier being passed through
        anim_fargs = (
            ax1,
            ax2,  # axis to plot into
            [left, right, bottom, top],  # imshow extent
            annotation_list,
            annotation_defaults,
            layer_cmap,
            layer_norm,
        )

    else:  # stacked_plot = False

        # if plotting level 4 with colourbar

        if measurement == 'level4' and colour_bar == True:

            # specific setting to fit level 4 colour bar beside the plot
            # we will plot the animation in the left hand plot
            # and put the colour bar on the right hand side

            # Define & set up figure, two subplots so colour bar fits :)
            fig, (ax1, ax2) = plt.subplots(1, 2, dpi=dpi,
                                           constrained_layout=True, gridspec_kw={'width_ratios': [3, 1]})
            fig.set_size_inches(width * scale * 2,
                                height * scale, forward=True)
            fig.set_constrained_layout_pads(
                w_pad=0.2, h_pad=0.2, hspace=0, wspace=0)

            # make colour bar
            # provide left hand canvas to colour bar fuction which is where the image will go
            # colourbar will plot on right side beside it

            make_colorbar(fig, ax1, measurement, animation=True)

            # turn off lines for second plot so it's not ontop of colourbar
            ax2.set_axis_off()

        # plotting any other measurement with or with-out colour bar or level 4 without
        else:

            # Define & set up figure
            fig, ax1 = plt.subplots(1, 1, dpi=dpi)
            fig.set_size_inches(width * scale, height * scale, forward=True)
            if(not label_ax):
                fig.subplots_adjust(left=0, bottom=0, right=1,
                                    top=1, wspace=None, hspace=None)
            # Add colourbar here
            if colour_bar:
                make_colorbar(fig, ax1, measurement)


        # This function is called at regular intervals with changing i
        # values for each frame
        def _update_frames(i, ax1, extent, annotation_text,
                           annotation_defaults, cmap, norm):
            # Clear previous frame to optimise render speed and plot imagery
            ax1.clear()
            ax1.imshow(da[i, ...], cmap=cmap, norm=norm,
                       extent=extent, interpolation="nearest")
            if(not label_ax):
                ax1.set_axis_off()

            # Add annotation text
            ax1.annotate(annotation_text[i], **annotation_defaults)

        # anim_fargs contains all the values we send to our
        # _update_frames function.
        # Note the layer_cmap and layer_norm which were calculated
        # earlier being passed through
        anim_fargs = (
            ax1,
            [left, right, bottom, top],  # imshow extent
            annotation_list,
            annotation_defaults,
            layer_cmap,
            layer_norm,
        )

    # Animate
    anim = FuncAnimation(
        fig=fig,
        func=_update_frames,
        fargs=anim_fargs,
        frames=len(da.time),
        interval=animation_interval,
        repeat=False,
    )

    anim.save(file_name, writer="pillow", dpi=dpi)
    plt.close()
    return Image(filename=file_name)
