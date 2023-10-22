lignes = []

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
            

# Create a dictionary to store neighbors for each station
neighbors = {}

# Iterate through the connections and accumulate neighbors
for s1, s2 in zip(subway_data['join']['summit1'], subway_data['join']['summit2']):
    if s1 not in neighbors:
        neighbors[s1] = set()
    if s2 not in neighbors:
        neighbors[s2] = set()
    
    # Add neighbors to each station
    neighbors[s1].add(s2)
    neighbors[s2].add(s1)

# Convert the dictionary to nested lists
neighbors_list = [[station, list(neighbors)] for station, neighbors in neighbors.items()]

# Sort the neighbor lists in ascending order
neighbors_list = sorted(neighbors_list, key=lambda x: x[0])

# for element in neighbors_list:
#     print(element)


# Create a dictionary to store metro lines
metro_lines = {}

# Iterate through the station information
for station_id, station_info in subway_data['stations'].items():
    line_number = station_info[1]
    is_mainbranch = station_info[3] == 0
    branch = station_info[3]
    
    if line_number not in metro_lines:
            metro_lines[line_number] = [[],[],[]]
        
    if is_mainbranch:
        if station_info[2]:
            metro_lines[line_number][0].insert(0, station_id)
        metro_lines[line_number][0].append(station_id)
    else : 
        if branch == 1:
            metro_lines[line_number][1].append(station_id)
        if branch == 2:
            metro_lines[line_number][2].append(station_id)
    

# print(metro_lines)
 












