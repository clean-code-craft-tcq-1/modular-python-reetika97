import TelePairNumber as TP

def printManual():
  for i in range (0, len(MAJOR_COLORS)):
    for j in range (0, len(MINOR_COLORS)):
     pair_name= TP.color_pair_to_string(MAJOR_COLORS[i], MINOR_COLORS[j])
     pair_value=TP. get_pair_number_from_color(MAJOR_COLORS[i], MINOR_COLORS[j])
     print(pair_name, " : ", pair_value)
