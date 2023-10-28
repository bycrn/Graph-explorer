
subway_data = {
                'stations' : {},
                'join' : {
                        'summit1': [],
                        'summit2': [],
                        'lon': []
                         }
                }

# -------- 1) Description du stockage des données ------------

# format pour les sommets :
# V num_sommet nom_sommet numéro_ligne si_terminus branchement (0 stations en commun, 1 pour la direction 1,  2 pour la direction 2, ainsi 
# de suite ...)
    
# format pour les arêtes :
# E num_sommet1 num_sommet2 temps_en_secondes 


# récupérer les diférentes lignes et branches




with open('metro.txt', 'r', encoding="UTF-8") as metro:
    for line in metro:
        if line[0] == 'V':
            # station id ->   station name,
            #               ligne 
            #               terminus True or False
            #               branchement principale : 0, 1er branche : 1, 2e branche : 2
            
            subway_data['stations'][int(line.split()[1])] = [' '.join(line.lower().split()[2:-3]), 
                                                     line.split()[-3][1:], 
                                                     False if line.split()[-2][1:] == 'False' else True, 
                                                     0 if line.split()[-1]== '0' else 1 if line.split()[-1] == '1' else 2]

        if line[0] == 'E':
            
            subway_data['join']['summit1'].append(int(line.split()[1:][0]))
            subway_data['join']['summit2'].append(int(line.split()[1:][1]))
            subway_data['join']['lon'].append(int(line.split()[1:][2]))
            





# Create a dictionary to store metro lines
terminus = {}

# Iterate through the station information
for station_id, station_info in subway_data['stations'].items():
    line_number = station_info[1]
    is_mainbranch = station_info[3] == 0
    branch = station_info[3]
    
    if line_number not in terminus:
            terminus[line_number] = [[]]
    
    if station_info[2]:
        if is_mainbranch:
            terminus[line_number][0].insert(0, station_id)

        else : 
            if branch == 1:
                terminus[line_number][0].append(station_id)
            if branch == 2:
                terminus[line_number].append([terminus[line_number][0][0],station_id])
    














