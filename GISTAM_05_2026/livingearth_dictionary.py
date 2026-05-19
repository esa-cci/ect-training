# -*- coding: utf-8 -*-
# mycolourschemes.py

# Suggested as an alternative

# uw_biot1 = {
#     100: {"label": "ANIMALIA", "colour": "#EFB7B7"},
#     101: {"label": "Annelids", "colour": "#964000"},
# }
# patches = [
#     Patch(color=v["colour"], label=v["label"])
#     for v in uw_biot1.values()
# ]


# Define the legend colors and labels

level3_colours = {
    0: "#FFFFFF",
    111: "#D1E133",
    112: "#007A02",
    123: "#4EEEE8",
    124: "#02C077",
    215: "#DA5C69",
    216: "#F3AB69",
    220: "#4D9FDC",
}

level3_labels = {
    0: "Not classified",
    111: "Cultivated or managed terrestrial vegetation",
    112: "Semi-natural terrestrial woody vegetation",
    123: "Cultivated or managed aquatic vegetation",
    124: "Semi-natural aquatic vegetation",
    215: "Artificial surface",
    216: "Bare surface",
    220: "Water",
}


level3plus_scheme = {
    "#FFFFFF": [0.0, "Not classified"],
    "#D1E133": [111.0, "Cultivated or managed terrestrial vegetation"],
    "#007A02": [113.0, "Semi-natural terrestrial woody vegetation"],
    "#95c748": [114.0, "Semi-natural terrestrial herbaceous vegetation"],
    "#4EEEE8": [123.0, "Cultivated or managed aquatic vegetation"],
    "#02C077": [124.0, "Semi-natural aquatic vegetation"],
    "#DA5C69": [215.0, "Artificial surface"],
    "#F3AB69": [216.0, "Bare surface"],
    "#4D9FDC": [220.0, "Water"],
}

level3plus_labels = {
    0.0: "Not classified",
    111.0: "Cultivated or managed terrestrial vegetation",
    113.0: "Semi-natural terrestrial woody vegetation",
    114.0: "Semi-natural terrestrial herbaceous vegetation",
    123.0: "Cultivated or managed aquatic vegetation",
    124.0: "Semi-natural aquatic vegetation",
    215.0: "Artificial surface",
    216.0: "Bare surface",
    220.0: "Water",
}

# CHANGE COLOURS 
# Lifeform
lifeform_colours = [
    "#FFFFFF",  # 0 Non-vegetated
    "#21852C",  # 1 Woody
    "#A3CA54",  # 2 Herbaceous
]

lifeform_labels = {
    0: "Non-vegetated",
    1: "Woody",
    2: "Herbaceous",
}

# Vegetation cover
# Full label and color mapping
cover_labels = {
    0: "No Data / Not vegetated",
    9: "Uncertain cover",
    10: "> 65 % cover",
    12: "40 to 65 % cover",
    13: "15 to 40 % cover",
    15: "4 to 15 % cover",
    16: "4 to 15 % cover",
}

cover_colours = {
    0: "#FFFFFF",  # No Data / Not vegetated
    9: "#FF0000",  # Uncertain cover
    10: "#4BC864", # > 65 % cover
    12: "#E1AF19", # 40 to 65 % cover
    13: "#C87D19", # 15 to 40 % cover
    15: "#964B00", # 4 to 15 % cover
    16: "#AF7D32", # 4 to 15 % cover
}

l3change_colors = {
    "#FFFFFF": [0.0, "Not classified"],
    "#D1E133": [111.0, "Cultivated or managed terrestrial vegetation"],
    "#007A02": [113.0, "Semi-natural terrestrial woody vegetation"],
    "#95c748": [114.0, "Semi-natural terrestrial herbaceous vegetation"],
    "#4EEEE8": [123.0, "Cultivated or managed aquatic vegetation"],
    "#02C077": [124.0, "Natural and semi natural aquatic vegetation"],
    "#DA5C69": [215.0, "Artificial surface"],
    "#F3AB69": [216.0, "Bare surface"],
    "#4D9FDC": [220.0, "Water"],
}

l3change_labels = {
    "Not classified",
    "Cultivated or managed terrestrial vegetation",
    "Semi-natural terrestrial woody vegetation",
    "Semi-natural terrestrial herbaceous vegetation",
    "Cultivated or managed aquatic vegetation",
    "Natural and semi natural aquatic vegetation",
    "Artificial surface",
    "Bare surface",
    "Water",
}

phase1_colours = {
     "#A6ADA1": [13, "A1.1.1: Semi-natural broadleaved woodland"],
     "#C1C8BC": [14, "A1.1.2: Planted broadleaved woodland"],
     "#74c488": [15, "No class"],
     "#0e6a25": [16, "No class"],
     "#B5C8AE": [17, "A1.1.1: Semi-natural coniferous woodland"],
     "#FAFAF3": [18, "A1.2.2: Planted coniferous woodland"],
     "#f3f5f3": [19, "No class"],  
     "#e9e9e8": [20, "No class"],
     "#B0CAAA": [21, "A1.3.1: Semi-natural mixed woodland"],
     "#BAC7A9": [22, "A1.3.2: Planted mixed woodland"],
     "#dfdfdf": [23, "No class"],
     "#81887B": [24, "A2.1: Dense scrub"],
     "#edece9": [25, "No class"],
     "#dddddd": [26, "No class"],
     "#d8cfb3": [27, "No class"],
     "#d9cb9f": [28, "No class"],
     "#e7e6e1": [29, "No class"],  
     "#f8f7f7": [30, "No class"], 
     "#B7B4AA": [31, "A4.1: Felled broadleaved woodland"],
     "#C9C5A9": [32, "A4.2: Felled coniferous woodland"],
     "#BAB7AD": [33, "A4.3: Felled mixed woodland"],
     "#ff0000": [34, "No class"],     
     "#843c39": [35, "No class"],
     "#F5EADE": [36, "B1.1: Unimproved acid grassland"],
     "#F1DAC3": [37, "B1.2: Semi-improved acid grassland"],
     "#e9e6d2": [38, "No class"],
     "#e9e6d2": [39, "No class"],
     "#A95C39": [40, "B2.2: Semi-improved neutral grassland"],
     "#e0e1df": [41, "No class"], 
     "#F5BD78": [42, "B3.2:Semi-improved calcareous grassland*"],
     "#969696": [43, "B3.1: Unimproved calcareous grassland*"],
     "#FFFFFF": [44, "B4: Improved grassland"],
     "#A9493E": [45, "B5: Marshy grassland"],
     "#fdae6b": [46, "B5.1: Marshy grassland - Juncus dominated"],
     "#518388": [47, "B5.2: Marshy grassland - Molinia dominated"],
     "#f4f8f9": [48, "No class"], 
     "#f1f4f5": [49, "No class"], 
     "#ecf4f8": [50, "No class"], 
     "#DEB38F": [51, "C.1.1: Scattered bracken NOT C2-upland species rich ledges"],
     "#f9f6ff": [52, "No class"], 
     "#bcbddc": [53, "No class"],
     "#f9fbf2": [54, "No class"], 
     "#FCF3EC": [55, "C3.1: Tall ruderal herb"],
     "#D3BA9E": [56, "C3.2: Non-ruderal herb and fern*"],
     "#e4f9fa": [57, "No class"], 
     "#fbfbfb": [58, "No class"], 
     "#F6D789": [59, "D1.1: Dry acid heath"],
     "#DFBB67": [60, "D1.2: Dry basic heath*"],
     "#D39753": [61, "D2: Wet heath*"],
     "#c7c7c7": [62, "No class"],
     "#fff7f8": [63, "No class"], 
     "#EFC479": [64, "D5: Dry heath"],
     "#AF4133": [65, "D6: Wet heath/acid grassland mosaic"],
     "#e7969c": [66, "D7: Basic dry heath/calcareous grassland mosaic*"],
     "#f7f2f3": [67, "No class"], 
     "#fdf6f8": [68, "No class"], 
     "#fdf6f7": [69, "No class"], 
     "#8E4C67": [70, "E1.6.1: Blanket bog"], 
     "#A67A90": [71, "E1.6.2: Modified blanket bog"],
     "#834D63": [72, "E1.7: Raised bog"],
     "#D2B9C2": [73, "E1.8: Modified raised bog"],
     "#D7E461": [74, "E2: Flush and spring"],
     "#B76372": [75, "E2.1: Acid/neutral flush"],
     "#C17C89": [76, "E2.2: Basic flush"],
     "#8B252C": [77, "E2.3: Bryophyte dominated spring*"],
     "#AD5B67": [78, "E3: Valley, basin and floodplain mire"],
     "#ce6dbd": [79, "E3.1: Modified valley, basin and floodplain mire"],
     "#b2abd2": [80, "E3.1.1: Modified valley mire"],
     "#DAA8B0": [81, "E3.2: Basin mire"],
     "#a55194": [82, "E3.2.1: Modified basin mire"],
     "#CF7B89": [83, "E3.3: Flood-plain mire"],
     "#9c9ede": [84, "E3.3.1-modified flood plain mire"],
     "#CAB3B9": [85, "E4: Bare peat*"],
     "#7595B3": [86, "F1: Swamp"],    
     "#7D2027": [87, "F2.2: Marginal and inundation vegetation"],
     "#fdffff": [88, "No class"], 
     "#fafcfc": [89, "No class"], 
     "#08519c": [90, "No class"],
     "#627394": [91, "G1: Standing water"], 
     "#4b0082": [92, "No class"],
     "#f5f7f7": [93, "No class"], 
     "#f3f5f5": [94, "No class"], 
     "#f0f2f2": [95, "No class"], 
     "#eef0f0": [96, "No class"], 
     "#eceded": [97, "No class"], 
     "#637399": [98, "G2: Running water"], 
     "#225ea8": [99, "No class"],
     "#e5e6e6": [100, "No class"], 
     "#e2e3e3": [101, "No class"], 
     "#dedfdf": [102, "No class"], 
     "#dcdddd": [103, "No class"], 
     "#dadbdb": [104, "No class"], 
     "#d7d8d8": [105, "No class"], 
     "#ffe9e9": [106, "No class"], 
     "#fbe5e5": [107, "No class"], 
     "#ffffff": [108, "H1.1: intertidal mud/sand"], 
     "#2171b5": [109, "No class"],
     "#fafafa": [110, "No class"], 
     "#f7f7f7": [111, "No class"], 
     "#f5f5f5": [112, "H1.2: Intertidal cobbles/shingle"], 
     "#d2d2d2": [113, "No class"],
     "#f3f3f3": [114, "No class"], 
     "#f6f6f6": [115, "No class"], 
     "#f8f8f8": [116, "No class"], 
     "#CB8F7D": [117, "H2.6-salt marsh"],
     "#f9f9f9": [118, "No class"], 
     "#f1f1f1": [119, "No class"], 
     "#f2f2f2": [120, "No class"],
     "#f4f4f4": [121, "No class"], 
     "#ececec": [122, "H1.3: Intertidal rocks/boulders"], 
     "#d5d5d4": [123, "H3.1: Mud/sand above mhw"],
     "#fcf7e2": [124, "H3.2: Shingle/gravel above mhw"],
     "#66c2a4": [125, "No class"],
     "#e1e1e1": [126, "H4: Rocks/boulders above mhw"], 
     "#d1d2d3": [127, "No class"],
     "#e2e2e2": [128, "No class"], 
     "#BA917F": [129, "H6.4: Dune slack"], 
     "#CC643A": [130, "H6.5: Dune grassland"],
     "#D9913E": [131, "H6.6: Dune heath"],
     "#8D7056": [132, "H6.7: Dune scrub"],
     "#E8B383": [133, "H6.8: Open dune"],
     "#31a354": [134, "No class"],
     "#CD7A6E": [135, "H8.1: Hard cliff*"], 
     "#CC786F": [136, "H8.2: Soft cliff*"],
     "#a1d99b": [137, "No class"],
     "#A94734": [138, "H8.4: Coastal grassland"], 
     "#D7C175": [139, "H8.5: Coastal heathland"],
     "#b35806": [140, "H8.6: Coastal heath/coastal grassland mosaic*"],
     "#7f2704": [141, "I1: Natural rock exposure*"],
     "#e6e6e6": [142, "No class"], 
     "#d6616b": [143, "I1.1: Inland cliff*"],
     "#e7969c": [144, "I1.1.1:Acid/neutral cliff*"],
     "#d9d8d7": [145, "1.1.2: Basic cliff*"],
     "#9edae5": [146, "I1.2: Acid/neutral scree*"],
     "#e5e2ce": [147, "I1.2.1-Basic scree*"],
     "#f2eed9": [148, "No class"],
     "#74c476": [149, "I1.3-Limestone pavement*"],
     "#ff9896": [150, "I1.4-Other rock exposure*"],
     "#c5b0d5": [151, "I1.4.1: Acid/neutral rock*"],
     "#c49c94": [152, "I1.4.2: Basic rock and limestone pavement*"],
     "#252525": [153, "I1.5L Cave*"],
     "#98df8a": [154, "No class"],
     "#9a9488": [155, "I2.1: Quarry, spoil, mine, refuse-tip"], 
     "#b8e186": [156, "No class"],
     "#1f77b4": [157, "I2.3: Mine*"],
     "#ff7f0e": [158, "I2.4: Refuse-tip"],
     "#FFFFD6": [159, "J1.1: Arable"],
     "#FEE763": [160, "J1.2: Amenity grassland"],
     "#9467bd": [161, "J1.3: Ephemeral/short perennial"],
     "#8c564b": [162, "J1.4: Introduced scrub*"],
     "#ddf0f1": [163, "J1.5: Buildings"],
     "#7f7f7f": [164, "J2.1: Hedge*"],
     "#e8e8e8": [165, "No class"], 
     "#e9e9e9": [166, "No class"], 
     "#d1d1d1": [167, "No class"], 
     "#d1d2d2": [168, "No class"], 
     "#d3d3d3": [169, "No class"], 
     "#d4d4d4": [170, "No class"], 
     "#d5d5d5": [171, "No class"], 
     "#d6d6d6": [172, "No class"], 
     "#d7d7d7": [173, "No class"], 
     "#d8d8d8": [174, "No class"], 
     "#d9d9d9": [175, "No class"], 
     "#d0d0d0": [176, "No class"], 
     "#e0e0e0": [177, "No class"], 
     "#cccccc": [178, "No class"], 
     "#c1c1c1": [179, "No class"], 
     "#c2c2c2": [180, "No class"], 
     "#918283": [181, "J3.4: Caravan site"],    
     "#bcbd22": [182, "J3.5: Sea wall"],
     "#000000": [183, "J3.6: Buildings"],
     "#393b79": [184, "J3.7-track"],
     "#637939": [185, "J4: Bare ground"],
     "#8c510a": [186, "No class"],
     "#3b0f0f": [187, "NA-not accessed"],
     "#7b4173": [188, "Empty_set-unresolved_habitat"],    
}

phase1_labels = {
    13: "A1.1.1: Semi-natural broadleaved woodland",
    14: "A1.1.2: Planted broadleaved woodland",
    15: "No class",
    16: "No class",
    17: "A1.1.1: Semi-natural coniferous woodland",
    18: "A1.2.2: Planted coniferous woodland",
    19: "No class",
    20: "No class",
    21: "A1.3.1: Semi-natural mixed woodland",
    22: "A1.3.2: Planted mixed woodland",
    23: "No class",
    24: "A2.1: Dense scrub",
    25: "No class",
    26: "No class",
    27: "No class",
    28: "No class",
    29: "No class",
    30: "No class",
    31: "A4.1: Felled broadleaved woodland",
    32: "A4.2: Felled coniferous woodland",
    33: "A4.3: Felled mixed woodland",
    34: "No class",
    35: "No class",
    36: "B1.1: Unimproved acid grassland",
    37: "B1.2: Semi-improved acid grassland",
    38: "No class",
    39: "No class",
    40: "B2.2: Semi-improved neutral grassland",
    41: "No class",
    42: "B3.2: Semi-improved calcareous grassland*",
    43: "B3.1: Unimproved calcareous grassland*",
    44: "B4: Improved grassland",
    45: "B5: Marshy grassland",
    46: "B5.1: Marshy grassland - Juncus dominated",
    47: "B5.2: Marshy grassland - Molinia dominated",
    48: "No class",
    49: "No class",
    50: "No class",
    51: "C.1.1: Scattered bracken NOT C2-upland species rich ledges",
    52: "No class",
    53: "No class",
    54: "No class",
    55: "C3.1: Tall ruderal herb",
    56: "C3.2: Non-ruderal herb and fern*",
    57: "No class",
    58: "No class",
    59: "D1.1: Dry acid heath",
    60: "D1.2: Dry basic heath*",
    61: "D2: Wet heath*",
    62: "No class",
    63: "No class",
    64: "D5: Dry heath",
    65: "D6: Wet heath/acid grassland mosaic",
    66: "D7: Basic dry heath/calcareous grassland mosaic*",
    67: "No class",
    68: "No class",
    69: "No class",
    70: "E1.6.1: Blanket bog",
    71: "E1.6.2: Modified blanket bog",
    72: "E1.7: Raised bog",
    73: "E1.8: Modified raised bog",
    74: "E2: Flush and spring",
    75: "E2.1: Acid/neutral flush",
    76: "E2.2: Basic flush",
    77: "E2.3: Bryophyte dominated spring*",
    78: "E3: Valley, basin and floodplain mire",
    79: "E3.1: Modified valley, basin and floodplain mire",
    80: "E3.1.1: Modified valley mire",
    81: "E3.2: Basin mire",
    82: "E3.2.1: Modified basin mire",
    83: "E3.3: Flood-plain mire",
    84: "E3.3.1: Modified flood plain mire",
    85: "E4: Bare peat*",
    86: "F1: Swamp",
    87: "F2.2: Marginal and inundation vegetation",
    88: "No class",
    89: "No class",
    90: "No class",
    91: "G1: Standing water",
    92: "No class",
    93: "No class",
    94: "No class",
    95: "No class",
    96: "No class",
    97: "No class",
    98: "G2: Running water",
    99: "No class",
    100: "No class",
    101: "No class",
    102: "No class",
    103: "No class",
    104: "No class",
    105: "No class",
    106: "No class",
    107: "No class",
    108: "H1.1: intertidal mud/sand",
    109: "No class",
    110: "No class",
    111: "No class",
    112: "H1.2: Intertidal cobbles/shingle",
    113: "No class",
    114: "No class",
    115: "No class",
    116: "No class",
    117: "H2.6: salt marsh",
    118: "No class",
    119: "No class",
    120: "No class",
    121: "No class",
    122: "H1.3: Intertidal rocks/boulders",
    123: "H3.1: Mud/sand above MHW",
    124: "H3.2: Shingle/gravel above MHW",
    125: "No class",
    126: "H4: Rocks/boulders above MHW",
    127: "No class",
    128: "No class",
    129: "H6.4: Dune slack",
    130: "H6.5: Dune grassland",
    131: "H6.6: Dune heath",
    132: "H6.7: Dune scrub",
    133: "H6.8: Open dune",
    134: "No class",
    135: "H8.1: Hard cliff*",
    136: "H8.2: Soft cliff*",
    137: "No class",
    138: "H8.4: Coastal grassland",
    139: "H8.5: Coastal heathland",
    140: "H8.6: Coastal heath/coastal grassland mosaic*",
    141: "I1: Natural rock exposure*",
    142: "No class",
    143: "I1.1: Inland cliff*",
    144: "I1.1.1: Acid/neutral cliff*",
    145: "I1.1.2: Basic cliff*",
    146: "I1.2: Acid/neutral scree*",
    147: "I1.2.1: Basic scree*",
    148: "No class",
    149: "I1.3: Limestone pavement*",
    150: "I1.4: Other rock exposure*",
    151: "I1.4.1: Acid/neutral rock*",
    152: "I1.4.2: Basic rock and limestone pavement*",
    153: "I1.5: Cave*",
    154: "No class",
    155: "I2.1: Quarry, spoil, mine, refuse-tip",
    156: "No class",
    157: "I2.3: Mine*",
    158: "I2.4: Refuse-tip",
    159: "J1.1: Arable",
    160: "J1.2: Amenity grassland",
    161: "J1.3: Ephemeral/short perennial",
    162: "J1.4: Introduced scrub*",
    163: "J1.5: Buildings",
    164: "J2.1: Hedge*",
    165: "No class",
    166: "No class",
    167: "No class",
    168: "No class",
    169: "No class",
    170: "No class",
    171: "No class",
    172: "No class",
    173: "No class",
    174: "No class",
    175: "No class",
    176: "No class",
    177: "No class",
    178: "No class",
    179: "No class",
    180: "No class",
    181: "J3.4: Caravan site",
    182: "J3.5: Sea wall",
    183: "J3.6: Buildings",
    184: "J3.7: Track",
    185: "J4: Bare ground",
    186: "No class",
    187: "NA: Not accessed",
    188: "Empty set: Unresolved habitat"
}

nvc_colours = [
    "#ffffff",  # 0 No data
    "#2b6b2b",  # 1 Woodland
    "#7fc97f",  # 2 Grassland
    "#41ae76",  # 3 Marshy grassland
    "#a6611a",  # 4 Bracken
    "#d9ef8b",  # 5 Heath
    "#7b3294",  # 6 Mire
    "#80cdc1",  # 7 Swamp
    "#225ea8",  # 8 Freshwater
    "#41b6c4",  # 9 Coastal
    "#636363",  # 10 Rock
    "#bdbdbd"   # 11 Artificial
]

nvc_labels = {
    0: "No data",
    1: "Woodland",
    2: "Grassland",
    3: "Marshy grassland",
    4: "Bracken / tall herb",
    5: "Heath",
    6: "Mire / peatland",
    7: "Swamp",
    8: "Freshwater",
    9: "Coastal",
    10: "Rock / bare ground",
    11: "Artificial / agricultural"
}

broad_habitat_colours = {
    "#FFFFFF": [0.0, "Not classified"],
    "#00C502": [1.0, "Broadleaved woodland"],
    "#006902": [2.0, "Needle-leaved woodland"],
    "#CEF191": [3.0, "Semi-natural grassland"],
    "#C91FCC": [4.0, "Heathland and Scrub"],
    "#F2A008": [5.0, "Bracken"],
    "#F8F8C9": [6.0, "Bog"],
    "#177E88": [7.0, "Fen/Marsh/Swamp"],
    "#FFFF00": [8.0, "Cultivated or managed vegetation"],
    "#00DDA4": [9.0, "Coastal habitat"],
    "#0E00ED": [10.0, "Open Water"],
    "#908E8D": [11.0, "Natural Bare Surfaces"],
    "#000000": [12.0, "Artificial Bare Surfaces"],
    "#DAC654": [13.0, "Young trees/Felled/Coppice"],
    "#5d994e": [14.0, "Woodland and scrub"],
}

broad_habitat_labels = {
    0.0: "Not classified",
    1.0: "Broadleaved woodland",
    2.0: "Needle-leaved woodland",
    3.0: "Semi-natural grassland",
    4.0: "Heathland and Scrub",
    5.0: "Bracken",
    6.0: "Bog",
    7.0: "Fen/Marsh/Swamp",
    8.0: "Cultivated or managed vegetation",
    9.0: "Coastal habitat",
    10.0: "Open Water",
    11.0: "Natural Bare Surfaces",
    12.0: "Artificial Bare Surfaces",
    13.0: "Young trees/Felled/Coppice",
    14.0: "Woodland and scrub",
}
detailed_habitat_colours = {
    "#FFFFFF": [0.0, "Not classified"],
    "#45fb82": [3.0, "Semi-natural grassland (other)"],
    "#577117": [4.0, "Juncus rushes"],
    "#cef191": [5.0, "Molinia grassland"],
    "#efe67e": [9.0, "Young plantations/Felled/Coppice"],
    "#399c4f": [10.0, "Woodland and scrub (other)"],
    "#0ac72d": [12.0, "Broadleaved woodland"],
    "#286b35": [16.0, "Needleleaved woodland"],
    "#6d5742": [23.0, "Ulex dominated scrub"],
    "#d7d236": [35.0, "Acid grassland"],
    "#c5d833": [38.0, "Neutral grassland"],
    "#c3c000": [41.0, "Calcareous grassland"],
    "#fced13": [44.0, "Improved grassland"],
    "#518388": [45.0, "Marshy grassland"],
    "#f37e1c": [50.0, "Bracken"],
    "#9c0f85": [58.0, "Dry dwarf shrub heath"],
    "#e2a7ed": [61.0, "Wet dwarf shrub heath"],
    "#df0f4a": [70.0, "Blanket bog"],
    "#f74428": [71.0, "Raised bog"],
    "#f7eebb": [72.0, "Modified bog"],
    "#6bdac2": [78.0, "Fen"],
    "#000000": [85.0, "Peat (bare)"],
    "#4eb0e0": [86.0, "Swamp"],
    "#013ff6": [90.0, "Open Water"],
    "#a5ffdc": [106.0, "Intertidal vegetation"],
    "#3b4b61": [107.0, "Intertidal bare surfaces"],
    "#4de5fc": [119.0, "Saltmarsh"],
    "#ecb641": [128.0, "Open dune"],
    "#30aa87": [130.0, "Dune grassland"],
    "#6e1ae3": [131.0, "Dune heath"],
    "#7c3843": [132.0, "Dune scrub"],
    "#7286bb": [134.0, "Maritime cliff and slope (unvegetated)"],
    "#5a5860": [135.0, "Maritime cliff and slope (vegetated)"],
    "#020b09": [142.0, "Natural rock exposure and waste"],
    "#c6c3d3": [143.0, "Inland cliff"],
    "#beebeb": [155.0, "Quarry"],
    "#fb9a71": [159.0, "Arable crops"],
    "#ddf0f1": [200.0, "Artificial bare surfaces"],
    "#a0ada9": [201.0, "Natural bare surfaces"],
    "#8cbd77": [202.0, "Semi-natural herbaceous vegetation (other)"],
}

detailed_habitat_labels = [
    "Not classified",
    "Semi-natural grassland (other)",
    "Juncus rushes",
    "Molinia grassland",
    "Young plantations/Felled/Coppice",
    "Woodland and scrub (other)",
    "Broadleaved woodland",
    "Needleleaved woodland",
    "Ulex dominated scrub",
    "Acid grassland",
    "Neutral grassland",
    "Calcareous grassland",
    "Improved grassland",
    "Marshy grassland",
    "Bracken",
    "Dry dwarf shrub heath",
    "Wet dwarf shrub heath",
    "Blanket bog",
    "Raised bog",
    "Modified bog",
    "Fen",
    "Peat (bare)",
    "Swamp",
    "Open Water",
    "Intertidal vegetation",
    "Intertidal bare surfaces",
    "Saltmarsh",
    "Open dune",
    "Dune grassland",
    "Dune heath",
    "Dune scrub",
    "Maritime cliff and slope (unvegetated)",
    "Maritime cliff and slope (vegetated)",
    "Natural rock exposure and waste",
    "Inland cliff",
    "Quarry",
    "Arable crops",
    "Artificial bare surfaces",
    "Natural bare surfaces",
    "Semi-natural herbaceous vegetation (other)",
]

# UNDERWATER LAYERS
# Number of biota (biocom)

uw_biota_colours = [
    "#F2F2F2",  # 0 No biota
    "#B7F6D9",  # 1 One biota
    "#40E5B7",  # 2 More than three biota
    "#00FA97",  # 3 Two (dominant) biota
    "#65BD74",  # 4 Three (dominant) biota
]

uw_biota_labels = {
    0: "No biota",
    1: "One biota",
    2: "More than three biota",
    3: "Two (dominant) biota",
    4: "Three (dominant) biota",
}


uw_biot1_colours = {
    100: "#EFB7B7",  # ANIMALIA
    101: "#964000",  # Annelids
    102: "#73C16E",  # Ascidians
    103: "#DEC49F",  # Brachiopods
    104: "#FFB2C0",  # Bryozoans
    105: "#A647D3",  # Cnidarians
    106: "#F46B56",  # Crustaceans
    107: "#D8B386",  # Echinoderms
    108: "#E2A19A",  # Molluscs
    109: "#FFD600",  # Poriferans
    110: "#E2D75A",  # Zooplankton
    200: "#6F942A",  # PLANTAE
    201: "#FF5948",  # Red seaweed
    202: "#03C72A",  # Green seaweed
    203: "#BFD794",  # Herbaceous
    204: "#D4E5B9",  # Graminoids
    205: "#01EB6F",  # Forbs
    206: "#E270D9",  # Seagrass
    300: "#C6BD92",  # Fungi
    301: "#FF9B6C",  # Lichen
    400: "#C0A1EF",  # CHROMISTA
    401: "#CFC0DC",  # Brown algae
    402: "#E8E0ED",  # Fucoids
    403: "#377E1A",  # Kelp
    404: "#D6F375",  # Haptophytes
    500: "#07EC31",  # PROTOZOA
    501: "#35DB8A",  # Algae (single-celled)
    502: "#FF9F97",  # Red algae
    503: "#62C775",  # Green algae
    600: "#01EBAB",  # PROKARYOTA
    601: "#F3A5FF",  # Bacteria
    602: "#FFE066",  # Cyanobacteria
    603: "#C2FFE4",  # Archaea
    604: "#00CCCB",  # Unknown
}

uw_biot1_labels = {
    100: "ANIMALIA",
    101: "Annelids",
    102: "Ascidians",
    103: "Brachiopods",
    104: "Bryozoans",
    105: "Cnidarians",
    106: "Crustaceans",
    107: "Echinoderms",
    108: "Molluscs",
    109: "Poriferans",
    110: "Zooplankton",
    200: "PLANTAE",
    201: "Red seaweed",
    202: "Green seaweed",
    203: "Herbaceous",
    204: "Graminoids",
    205: "Forbs",
    206: "Seagrass",
    300: "Fungi",
    301: "Lichen",
    400: "CHROMISTA",
    401: "Brown algae",
    402: "Fucoids",
    403: "Kelp",
    404: "Haptophytes",
    500: "PROTOZOA",
    501: "Algae (single-celled)",
    502: "Red algae",
    503: "Green algae",
    600: "PROKARYOTA",
    601: "Bacteria",
    602: "Cyanobacteria",
    603: "Archaea",
    604: "Unknown",
}

# TIDAL STATE
uw_tidal_colours = [
    "#B1B7D1",  # 10 Intertidal (littoral)
    "#4168AA",  # 11 Subtidal (sublittoral)
    "#3C90E0",  # 12 Infralittoral
    "#0064FF",  # 13 Circalittoral
]

uw_tidal_labels = {
    10: "Intertidal (littoral)",
    11: "Subtidal (sublittoral)",
    12: "Infralittoral",
    13: "Circalittoral",
}

# Bathymetry
uw_bathymetry_colours = [
    "#2ECFFF",  # 3 0.01-2,
    "#009CFF",  # 4 2-5 m,
    "#0182FF",  # 5 5-10 m
    "#0068D3",  # 6 10-20 m
    "#004EA0",  # 7 20-100 m
    "#00336A",  # 8 > 100 m
]

uw_bathymetry_labels = {
    3: "0.01-2 m",
    4: "2-5 m",
    5: "5-10 m",
    6: "10-20 m",
    7: "20-100 m",
    8: "> 100 m",
}

# Consolidation

uw_consolidation_colours = [
    "#BA5101", # Consolidated
    "#FFDA28", # Unconsolidated
]

uw_consolidation_labels = {
    1: "Consolidated",
    2: "Unconsolidated",
}

# Substrate type
uw_substrate_colours = {
    3: "#EFB7B7",  # Rock
    4: "#964000",  # Bedrock
    5: "#73C16E",  # Soft
    6: "#DEC49F",  # Hard
}

uw_substrate_labels = {
    3: "Rock",
    4: "Bedrock",
    5: "Soft",
    6: "Hard",
}

# Substrate size
uw_substratesize_colours = {
    7: "#FFB2C0",  # Mud
    8: "#A647D3",  # Silt
    9: "#F46B56",  # Sand
    10: "#D8B386",  # Gravels
    11: "#E2A19A",  # Granules
    12: "#FFD600",  # Shingle
    13: "#E2D75A",  # Pebbles
    14: "#6F942A",  # Cobbles
    15: "#FF5948",  # Boulders
    16: "#03C72A",  # Stones
    17: "#BFD794",  # Rubble
}

uw_substratesize_labels = {
    7: "Mud",
    8: "Silt",
    9: "Sand",
    10: "Gravels",
    11: "Granules",
    12: "Shingle",
    13: "Pebbles",
    14: "Cobbles",
    15: "Boulders",
    16: "Stones",
    17: "Rubble",
}

# Spatial aspect
uw_aspect_colours = {
    1: "#DEC4C5",  # Colonial
    2: "#DC9A86",  # Biogenic reef
    3: "#E01D2E",  # Crustose
    4: "#7D696E",  # Cushion
    4: "#01B241",  # Foliose  
    5: "#13D600",  # Film
    6: "#009C6D",  # Mat
    7: "#6ABD51",  # Turf
    8: "#8E7AD5",  # Forest
}

uw_aspect_labels = {
    1: "Colonial",
    2: "Biogenic reef",
    3: "Crustose",
    4: "Cushion",
    5: "Foliose",
    6: "Film",
    7: "Mat",
    8: "Turf",
    9: "Forest",
}

# Energy
uw_energy_colours = {
    1: "#ACB4B3",  # Low energy
    2: "#00B5AA",  # Moderate energy
    3: "#3C7FE0",  # High energy
}

uw_energy_labels = {
    1: "Colonial",
    2: "Bigenic reef",
    3: "Crustose",
}

# CONTEXTUAL LAYERS

# GEOLOGY
geology_colours = {
    "#ffffff",  # 0 No data
    "#F5EADE",  # 1 Acid geology
    "#A95C39",  # 1 Neutral geology
    "#74c476",  # 3 Calcareous geology
    "#2b6b2b",  # 1 Acid/neutral geology
}
geology_labels = {
    0: "No data",
    1: "Acid",
    2: "Neural",
    3: "Calcareous",
    4: "Acid/neutral",
}

# SUBSTRATE
substrate_colours = {
    "#ffffff",  # 0 No data
    "#F5EADE",  # Hard substrate
    "#A95C39",  # Soft substrate
}
substrate_labels = {
    0: "No data",
    1: "Hard substrate",
    2: "Soft substrate",
}

# SLOPE
slope_colours = {
    "#FFFFFF": [0, "Not classified"],
    "#E2FFE1": [1, "Level terrain"],
    "#C7B6AD": [2, "Potential scree areas"],
}

slope_labels = {
    0: "Not classified",
    1: "Level terrain",
    2: "Potential scree areas",
}

# Soil moisture
soil_moisture_colours = [
    "#ffffff",  # 0 No data
    "#A4D3F9",  # 1 Wet
    "#A95C39",  # 2 Dry
]

soil_moisture_labels = {
    0: "No data",
    1: "Wet",
    2: "Dry",
}

# ESA CCI land cover
#Define the LCCS colours according to their ID and names

# # esa_cci_lc_ids = [
#     10, 11, 12, 20, 30, 40,          # Cultivated areas
#     50, 60, 61, 62,                  # Broadleaved trees
#     70, 71, 72,                      # Needleleaved evergreen trees
#     80, 81, 82,                      # Needleleaved deciduous trees
#     90, 100, 110,                    # Mixed vegetation
#     120, 121, 122,                   # Shrubland
#     130, 140,                        # Herbaceous and lichens/mosses
#     150, 151, 152, 153,              # Sparse vegetation
#     160, 170, 180,                   # Aquatic vegetation
#     190,                             # Artificial surfaces
#     200, 201, 202,                   # Bare areas
#     210, 220                         # Water bodies, snow and ice
# ]


# CHANGE COLOURS 
# Level3 Gains and losses
level3_gainloss_colours = [
    "#FFFFFF",  # 0 No Change
    "#0E7912",  # 111112 Cultivated Terrestrial Vegetation -> Natural Woody Vegetation
    "#7BF3EC",  # 111123 Cultivated Terrestrial Vegetation -> Natural Herbaceous Vegetation
    "#1EBF79",  # 111124 Cultivated Terrestrial Vegetation -> Natural Aquatic Vegetation
    "#DA5C69",  # 111215 Cultivated Terrestrial Vegetation -> Artificial Surface
    "#F3AB69",  # 111216 Cultivated Terrestrial Vegetation -> Bare Surface
    "#1A54B9",  # 111220 Cultivated Terrestrial Vegetation -> Water
    "#ACBC2D",  # 112111 Semi-natural Terrestrial Woody Vegetation -> Cultivated Terrestrial Vegetation
    "#7BF3EC",  # 112123 Semi-natural Terrestrial Woody Vegetation -> Natural Herbaceous Vegetation
    "#1EBF79",  # 112124 Semi-natural Terrestrial Woody Vegetation -> Natural Aquatic Vegetation
    "#DA5C69",  # 112215 Semi-natural Terrestrial Woody Vegetation -> Artificial Surface
    "#F3AB69",  # 112216 Semi-natural Terrestrial Woody Vegetation -> Bare Surface
    "#1A54B9",  # 112220 Semi-natural Terrestrial Woody Vegetation -> Water
    "#ACBC2D",  # 124111 Semi-natural Aquatic Vegetation -> Cultivated Terrestrial Vegetation
    "#0E7912",  # 124112 Semi-natural Aquatic Vegetation -> Natural Woody Vegetation
    "#7BF3EC",  # 124123 Semi-natural Aquatic Vegetation -> Natural Herbaceous Vegetation
    "#DA5C69",  # 124215 Semi-natural Aquatic Vegetation -> Artificial Surface
    "#F3AB69",  # 124216 Semi-natural Aquatic Vegetation -> Bare Surface
    "#1A54B9",  # 124220 Semi-natural Aquatic Vegetation -> Water
    "#ACBC2D",  # 215111 Artificial Surface -> Cultivated Terrestrial Vegetation
    "#0E7912",  # 215112 Artificial Surface -> Natural Woody Vegetation
    "#7BF3EC",  # 215123 Artificial Surface -> Natural Herbaceous Vegetation
    "#1EBF79",  # 215124 Artificial Surface -> Natural Aquatic Vegetation
    "#F3AB69",  # 215216 Artificial Surface -> Bare Surface
    "#1A54B9",  # 215220 Artificial Surface -> Water
    "#ACBC2D",  # 216111 Bare Surface -> Cultivated Terrestrial Vegetation
    "#0E7912",  # 216112 Bare Surface -> Natural Woody Vegetation
    "#7BF3EC",  # 216123 Bare Surface -> Natural Herbaceous Vegetation
    "#1EBF79",  # 216124 Bare Surface -> Natural Aquatic Vegetation
    "#DA5C69",  # 216215 Bare Surface -> Artificial Surface
    "#1A54B9",  # 216220 Bare Surface -> Water
    "#ACBC2D",  # 220111 Water -> Cultivated Terrestrial Vegetation
    "#0E7912",  # 220112 Water -> Natural Woody Vegetation
    "#7BF3EC",  # 220123 Water -> Natural Herbaceous Vegetation
    "#1EBF79",  # 220124 Water -> Natural Aquatic Vegetation
    "#DA5C69",  # 220215 Water -> Artificial Surface
    "#F3AB69",  # 220216 Water -> Bare Surface
]

level3_gainloss_labels = {
    0: "No Change",
    111112: "Cultivated or managed terrestrial vegetation to Semi-natural terrestrial woody vegetation",
    111123: "Cultivated or managed terrestrial vegetation to Cultivated or managed aquatic vegetation",
    111124: "Cultivated or managed terrestrial vegetation to Semi-natural aquatic vegetation",
    111215: "Cultivated or managed terrestrial vegetation to Artificial surface",
    111216: "Cultivated or managed terrestrial vegetation to Bare surface",
    111220: "Cultivated or managed terrestrial vegetation to Water",
    112111: "Remained as Semi-natural terrestrial woody vegetation",
    112123: "Semi-natural terrestrial woody vegetation to Cultivated or managed aquatic vegetation",
    112124: "Semi-natural terrestrial woody vegetation to Semi-natural aquatic vegetation",
    112215: "Semi-natural terrestrial woody vegetation to Artificial surface",
    112216: "Semi-natural terrestrial woody vegetation to Bare surface",
    112220: "Semi-natural terrestrial woody vegetation to Water",
    124111: "Semi-natural aquatic vegetation to Cultivated or managed terrestrial vegetation",
    124112: "Semi-natural aquatic vegetation to Semi-natural terrestrial woody vegetation",
    124123: "Semi-natural aquatic vegetation to Cultivated or managed aquatic vegetation",
    124215: "Semi-natural aquatic vegetation to Artificial surface",
    124216: "Semi-natural aquatic vegetation to Bare surface",
    124220: "Semi-natural aquatic vegetation to Water",
    215111: "Artificial surface to Cultivated or managed terrestrial vegetation",
    215112: "Artificial surface to Semi-natural terrestrial woody vegetation",
    215123: "Artificial surface to Cultivated or managed aquatic vegetation",
    215124: "Artificial surface to Semi-natural aquatic vegetation",
    215216: "Artificial surface to Bare surface",
    215220: "Artificial surface to Water",
    216111: "Bare surface to Cultivated or managed terrestrial vegetation",
    216112: "Bare surface to Semi-natural terrestrial woody vegetation",
    216123: "Bare surface to Cultivated or managed aquatic vegetation",
    216124: "Bare surface to Semi-natural aquatic vegetation",
    216215: "Bare surface to Artificial surface",
    216220: "Bare surface to Water",
    220111: "Water to Cultivated or managed terrestrial vegetation",
    220112: "Water to Semi-natural terrestrial woody vegetation",
    220123: "Water to Cultivated or managed aquatic vegetation",
    220124: "Water to Semi-natural aquatic vegetation",
    220215: "Water to Artificial surface",
    220216: "Water to Bare surface"
}

lifeform_change_colours = [
    "#FFFFFF",  # 0 Remained non-vegetated
    "#C80000",  # 1 Non-vegetated to Woody
    "#64006E",  # 2 Non-vegetated to Herbaceous
    "#D2D2D2",  # 10 Woody to non-vegetated
    "#21852C",  # 11 Remained woody
    "#A5C8B4",  # 12 Woody to herbaceous
    "#F0F0F0",  # 20 Herbaceous to non-vegetated
    "#C89B64",  # 21 Herbaceous to woody
    "#A3CA54",  # 22 Remained herbaceous
]

# Labels for lifeform change
lifeform_change_labels = {
    0: "Remained non-vegetated",
    1: "Non-vegetated to Woody",
    2: "Non-vegetated to Herbaceous",
    10: "Woody to non-vegetated",
    11: "Remained woody",
    12: "Woody to herbaceous",
    20: "Herbaceous to non-vegetated",
    21: "Herbaceous to woody",
    22: "Remained herbaceous",
}

cover_change_colours = [
    "#FFFFFF",  # 0 No Data / Not vegetated
    
    # Bare -> covers
    "#FDB2F4", #900: "Bare to non data"
    "#D0F7C9", #910: "Bare to > 65 % cover",
    "#D0F7D6", #912: "Bare to to 40 to 65 % cover",
    "#D0F7E1", #913: "Bare to to 15 to 40 % cover",
    "#D0F7F8", #915: "Bare to 4 to 15 % cover",
    "#F7D3E6", #916: "Bare to 1 to 4 % cover",

    # >65 -> *
    "#D1F8E7",  #1000: "> 65 % to no data" 
    "#F7D3E6",  #1009> 65 % to bare",
    "#7D7D7D",  # 1010 Remained as > 65 % cover
    "#E1AF19",  # 1012 > 65 % to 40 to 65 % cover
    "#C87D19",  # 1013 > 65 % to 15 to 40 % cover
    "#964B00",  # 1015 > 65 % to 4 to 15 % cover
    "#644B19",  # 1016 > 65 % to 1 to 4 % cover

    # 40–65 -> *
    "#D1F8F4",  # 1200: "40 to 65 % to no data" 
    "#F7E0E6",  #1209:  "40 to 65 % cover to bare",
    "#4BC864",  # 1210 40 to 65 % to > 65 % cover
    "#969696",  # 1212 Remained as 40 to 65 % cover
    "#FA964B",  # 1213 40 to 65 % to 15 to 40 % cover
    "#C87D4B",  # 1215 40 to 65 % to 4 to 15 % cover
    "#AF7D32",  # 1216 40 to 65 % to 1 to 4 % cover

    # 15–40 -> *
    "#E3F8F4",  # 1300: "15 to 40 % to no data"  
    "#F7D3E6",  # 1309:  "15 to 40 % cover to bare",
    "#32AF32",  # 1310 15 to 40 % to > 65 % cover
    "#4BB34B",  # 1312 15 to 40 % to 40 to 65 % cover
    "#AFAFAF",  # 1313 Remained as 15 to 40 % cover
    "#E19600",  # 1315 15 to 40 % to 4 to 15 % cover
    "#C8AF64",  # 1316 15 to 40 % to 1 to 4 % cover

    # 4–15 -> *
    "#F0F8F4",  # 1500: "14 to 15 % to no data" 
    "#F7F4E3",  #1509:  "4 to 15 % cover to bare",
    "#006432",  # 1510 4 to 15 % to > 65 % cover
    "#329632",  # 1512 4 to 15 % to 40 to 65 % cover
    "#64AF00",  # 1513 4 to 15 % to 15 to 40 % cover
    "#C8C8C8",  # 1515 Remained as 4 to 15 % cover
    "#FEE164",  # 1516 4 to 15 % to 1 to 4 % cover

    # 1–4 -> *
    "#FDF8F4",  # 1600: "1 to 4 % to > 65 % cover",
    "#F7F4EE",  # 1609: "1 to 4 % cover to bare",
    "#003219",  # 1610 1 to 4 % to > 65 % cover
    "#327D32",  # 1612 1 to 4 % to 40 to 65 % cover
    "#7D9632",  # 1613 1 to 4 % to 15 to 40 % cover
    "#96C832",  # 1615 1 to 4 % to 4 to 15 % cover
    "#DCDCDC",  # 1616 Remained as 1 to 4 % cover
]

cover_change_labels = {
    0:    "No Data / Not vegetated",
    900:  "Bare to non data",
    910:  "Bare to > 65 % cover",
    912:  "Bare to to 40 to 65 % cover",
    913:  "Bare to to 15 to 40 % cover",
    915:  "Bare to 4 to 15 % cover",
    916:  "Bare to 1 to 4 % cover",
    1000: "> 65 % to no data", 
    1009: "> 65 % to bare",
    1010: "Remained as > 65 % cover",
    1012: "> 65 % to 40 to 65 % cover",
    1013: "> 65 % to 15 to 40 % cover",
    1015: "> 65 % to 4 to 15 % cover",
    1016: "> 65 % to 1 to 4 % cover",
    1200: "40 to 65 % to no data", 
    1209: "40 to 65 % cover to bare",
    1210: "40 to 65 % to > 65 % cover",
    1212: "Remained as 40 to 65 % cover",
    1213: "40 to 65 % to 15 to 40 % cover",
    1215: "40 to 65 % to 4 to 15 % cover",
    1216: "40 to 65 % to 1 to 4 % cover",
    1300: "15 to 40 % to no data",
    1309: "15 to 40 % cover to bare",
    1310: "15 to 40 % to > 65 % cover",
    1312: "15 to 40 % to 40 to 65 % cover",
    1313: "Remained as 15 to 40 % cover",
    1315: "15 to 40 % to 4 to 15 % cover",
    1316: "15 to 40 % to 1 to 4 % cover",
    1500: "14 to 15 % to no data",
    1509: "4 to 15 % cover to bare",
    1510: "4 to 15 % to > 65 % cover",
    1512: "4 to 15 % to 40 to 65 % cover",
    1513: "4 to 15 % to 15 to 40 % cover",
    1515: "Remained as 4 to 15 % cover",
    1516: "4 to 15 % to 1 to 4 % cover",
    1600: "1 to 4 % to > 65 % cover",
    1609: "1 to 4 % cover to bare",
    1610: "1 to 4 % to > 65 % cover",
    1612: "1 to 4 % to 40 to 65 % cover",
    1613: "1 to 4 % to 15 to 40 % cover",
    1615: "1 to 4 % to 4 to 15 % cover",
    1616: "Remained as 1 to 4 % cover",
}

waterper_change_colours = [
    "#FFFFFF",  # -9999 nan
    "#FFFFFF",  # -9919 nan
    "#FFFFFF",  # -9909 nan
    "#FFFFFF",  # 0 No Data / No water


    # >9 months row
    "#004B96",  # 11 Remained as > 9 months
    "#64AFAF",  # 13 > 9 months to tidal
    "#9696C8",  # 17 > 9 months to 7-9 months
    "#AF7D96",  # 18 > 9 months to 4-6 months
    "#C87D4B",  # 19 > 9 months to 1-3 months

    # Tidal row
    "#00C8AF",  # 31 Tidal to > 9 months
    "#649696",  # 33 Remained as tidal
    "#00C8AF",  # 37 Tidal to 7-9 months
    "#7DC8AF",  # 38 Tidal to 4-6 months
    "#AFC896",  # 39 Tidal to 1-3 months

    # 7–9 months row
    "#007DC8",  # 71 7-9 months to > 9 months
    "#96C8C8",  # 73 7-9 months to tidal
    "#969696",  # 77 Remained as 7-9 months
    "#E19696",  # 78 7-9 months to 4-6 months
    "#E1AF64",  # 79 7-9 months to 1-3 months

    # 4–6 months row
    "#4BB3E1",  # 81 4-6 months to > 9 months
    "#C8E1E1",  # 83 4-6 months to tidal
    "#00C8E1",  # 87 4-6 months to 7-9 months
    "#AFAFAF",  # 88 Remained as 4-6 months
    "#C8AF64",  # 89 4-6 months to 1-3 months

    # 1–3 months row
    "#64C8FA",  # 91 1-3 months to > 9 months
    "#AFFE E1", # 93 1-3 months to tidal
    "#7DE1FF",  # 97 1-3 months to 7-9 months
    "#C8FAFA",  # 98 1-3 months to 4-6 months
    "#C8C8C8",  # 99 Remained as 1-3 months
]

# Labels for water persistence
waterpersistence_labels = {
    -9999: "nan",
    -9919: "nan",
    -9909: "nan",
    0: "No Data / No water",
    11: "Remained as > 9 months",
    13: "> 9 months to tidal",
    17: "> 9 months to 7-9 months",
    18: "> 9 months to 4-6 months",
    19: "> 9 months to 1-3 months",
    31: "Tidal to > 9 months",
    33: "Remained as tidal",
    37: "Tidal to 7-9 months",
    38: "Tidal to 4-6 months",
    39: "Tidal to 1-3 months",
    71: "7-9 months to > 9 months",
    73: "7-9 months to tidal",
    77: "Remained as 7-9 months",
    78: "7-9 months to 4-6 months",
    79: "7-9 months to 1-3 months",
    81: "4-6 months to > 9 months",
    83: "4-6 months to tidal",
    87: "4-6 months to 7-9 months",
    88: "Remained as 4-6 months",
    89: "4-6 months to 1-3 months",
    91: "1-3 months to > 9 months",
    93: "1-3 months to tidal",
    97: "1-3 months to 7-9 months",
    98: "1-3 months to 4-6 months",
    99: "Remained as 1-3 months",
}

# -----------------------------
# Impact colours in hex
# -----------------------------
impact_colours = [
    "#FFFFFF",  # 0 No change
    "#CD853F",  # 1 Accretion
    "#00FF00",  # 2 Algal bloom
    "#D2691E",  # 3 Algal dieback
    "#773F1A",  # 4 Bare soil exposure
    "#3D0734",  # 5 Blackwater event
    "#FFE4B5",  # 6 Browning (vegetation)
    "#9370DB",  # 7 Building or infrastructure abandonment
    "#DAA520",  # 8 Compaction
    "#FAFAD2",  # 9 Coral bleaching
    "#C71585",  # 10 Coral damage
    "#F88379",  # 11 Coral recovery
    "#FFB61E",  # 12 Crop change in cultivated lands
    "#B87333",  # 13 Crop damage
    "#A7FC00",  # 14 Crop establishment
    "#FFF000",  # 15 Cropland gain
    "#7B3F00",  # 16 Cropland loss
    "#CD9575",  # 17 Deglaciation
    "#F2F0E6",  # 18 Desalinisation
    "#FFAE42",  # 19 Desertification
    "#9F8170",  # 20 Elevation change
    "#960018",  # 21 Erosion
    "#6F00FF",  # 22 Flooding
    "#8D2B0B",  # 23 Geomorphological change
    "#B0E0E6",  # 24 Glaciation
    "#9ACD32",  # 25 Greening
    "#B8860B",  # 26 Increased sediment load
    "#1E90FF",  # 27 Inundation
    "#CF1020",  # 28 Lava flow
    "#C46210",  # 29 Leaf scorch
    "#B3446C",  # 30 Mine abandonment
    "#C4AEAD",  # 31 Mine expansion
    "#FFDABF",  # 32 Natural surface gain
    "#663399",  # 33 Natural surface loss
    "#FFFAFA",  # 34 Net snow gain (amount)
    "#B6AA99",  # 35 Net snow loss (amount)
    "#F5F5F5",  # 36 Net snow gain (extent)
    "#C0C0C0",  # 37 Net snow loss (extent)
    "#FFFAF0",  # 38 Net snow gain (hydroperiod)
    "#DCDCDC",  # 39 Net snow loss (hydroperiod)
    "#DAA520",  # 40 Phenological change
    "#4B0082",  # 41 Railway or road abandonment
    "#F08080",  # 42 Railway or road construction
    "#FFA500",  # 43 Receding Flood
    "#EE82EE",  # 44 Salinisation
    "#B0C4DE",  # 45 Sea ice decrease
    "#D7F6F5",  # 46 Sea ice increase
    "#008B8B",  # 47 Sea level fall
    "#00BFFF",  # 48 Sea level rise
    "#E9967A",  # 49 Sedimentation
    "#F0FFF0",  # 50 Sink hole
    "#F0F8FF",  # 51 Snow accumulation
    "#A9A9A9",  # 52 Snow melt
    "#C71585",  # 53 Urban area loss
    "#9F00FF",  # 54 Urban damage
    "#CC9898",  # 55 Urban decay
    "#E52B50",  # 56 Urban densification
    "#FE6F5E",  # 57 Urban development
    "#E34234",  # 58 Urban growth
    "#FFB6C1",  # 59 Urban renewal
    "#CC3333",  # 60 Urban sprawl
    "#F06000",  # 61 Vegetation damage
    "#FFD580",  # 62 Vegetation dieback
    "#63A950",  # 63 Vegetation gain (amount)
    "#01755E",  # 64 Vegetation gain (extent)
    "#EEE8AA",  # 65 Vegetation health deterioration
    "#00CC99",  # 66 Vegetation health improvement
    "#FF8C00",  # 67 Vegetation loss (extent)
    "#DC8C00",  # 68 Vegetation reduction (amount)
    "#B28C00",  # 69 Vegetation reduction in understorey (amount)
    "#F5FFFA",  # 70 Vegetation species change
    "#AFEEEE",  # 71 Water depth decrease
    "#9400D3",  # 72 Water depth increase
    "#00FFFF",  # 73 Water gain (extent)
    "#FFB6C1",  # 74 Water loss (extent)
    "#FFFFFF",  # 75 Water quality change
]

# -----------------------------
# Impact labels
# -----------------------------
impact_labels = {
    0: "No change",
    1: "Accretion",
    2: "Algal bloom",
    3: "Algal dieback",
    4: "Bare soil exposure",
    5: "Blackwater event",
    6: "Browning (vegetation)",
    7: "Building or infrastructure abandonment",
    8: "Compaction",
    9: "Coral bleaching",
    10: "Coral damage",
    11: "Coral recovery",
    12: "Crop change in cultivated lands",
    13: "Crop damage",
    14: "Crop establishment",
    15: "Cropland gain",
    16: "Cropland loss",
    17: "Deglaciation",
    18: "Desalinisation",
    19: "Desertification",
    20: "Elevation change",
    21: "Erosion",
    22: "Flooding",
    23: "Geomorphological change",
    24: "Glaciation",
    25: "Greening",
    26: "Increased sediment load",
    27: "Inundation",
    28: "Lava flow",
    29: "Leaf scorch",
    30: "Mine abandonment",
    31: "Mine expansion",
    32: "Natural surface gain",
    33: "Natural surface loss",
    34: "Net snow gain (amount)",
    35: "Net snow loss (amount)",
    36: "Net snow gain (extent)",
    37: "Net snow loss (extent)",
    38: "Net snow gain (hydroperiod)",
    39: "Net snow loss (hydroperiod)",
    40: "Phenological change",
    41: "Railway or road abandonment",
    42: "Railway or road construction",
    43: "Receding Flood",
    44: "Salinisation",
    45: "Sea ice decrease",
    46: "Sea ice increase",
    47: "Sea level fall",
    48: "Sea level rise",
    49: "Sedimentation",
    50: "Sink hole",
    51: "Snow accumulation",
    52: "Snow melt",
    53: "Urban area loss",
    54: "Urban damage",
    55: "Urban decay",
    56: "Urban densification",
    57: "Urban development",
    58: "Urban growth",
    59: "Urban renewal",
    60: "Urban sprawl",
    61: "Vegetation damage",
    62: "Vegetation dieback",
    63: "Vegetation gain (amount)",
    64: "Vegetation gain (extent)",
    65: "Vegetation health deterioration",
    66: "Vegetation health improvement",
    67: "Vegetation loss (extent)",
    68: "Vegetation reduction (amount)",
    69: "Vegetation reduction in understorey (amount)",
    70: "Vegetation species change",
    71: "Water depth decrease",
    72: "Water depth increase",
    73: "Water gain (extent)",
    74: "Water loss (extent)",
    75: "Water quality change",
}


# OTHER LAND COVER, HABITAT OR ECOSYSTEM CLASSIFICATION SCHEMS

esa_cci_lc_colours = [
    "#ffff64", "#ffff64", "#ffff64", "#aaf0f0", "#dcf064", "#c8c864",
    "#006400", "#00a000", "#00a000", "#00a000", "#003c00", "#003c00",
    "#003c00", "#285000", "#285000", "#285000", "#788200", "#8ca000",
    "#be9600", "#966400", "#966400", "#966400", "#ffb432", "#ffdcd2",
    "#ffebaf", "#ffebaf", "#ffebaf", "#ffebaf", "#00785a", "#009678",
    "#00dc82", "#c31400", "#fff5d7", "#fff5d7", "#fff5d7", "#0046c8",
    "#ffffff"
]


esa_cci_lc_labels = {
    10: "Rainfed crops",
    11: "Rainfed herbaceous crops",
    12: "Rainfed shrub/tree crops",
    20: "Irrigated crops",
    30: "Cropland/Natural vegetation mosaic",
    40: "Natural vegetation/Cropland mosaic",
    50: "Broadleaved evergreen/semi-deciduous trees",
    60: "Broadleaved deciduous trees",
    61: "Broadleaved deciduous closed trees",
    62: "Broadleaved deciduous open trees",
    70: "Needleleaved evergreen trees",
    71: "Needleleaved evergreen closed trees",
    72: "Needleleaved evergreen open trees",
    80: "Needleleaved deciduous trees",
    81: "Needleleaved deciduous closed trees",
    82: "Needleleaved deciduous open trees",
    90: "Mixed broadleaved/needleleaved trees",
    100: "Mixed trees/shrubland/herbaceous",
    110: "Herbaceous/trees/shrubland",
    120: "Shrubland",
    121: "Evergreen shrubland",
    122: "Deciduous shrubland",
    130: "Grassland",
    140: "Lichens and mosses",
    150: "Sparse vegetation",
    151: "Sparse trees",
    152: "Sparse shrubs",
    153: "Sparse herbaceous",
    160: "Flooded trees (fresh water)",
    170: "Flooded trees (saline/brackish water)",
    180: "Flooded shrubs/herbaceous",
    190: "Urban areas",
    200: "Bare areas",
    201: "Consolidated bare areas",
    202: "Unconsolidated bare areas",
    210: "Water bodies",
    220: "Snow and ice"
}

