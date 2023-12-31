
line_colors = {
    '1': '#F6D046',
    '2': '#2962AB',
    '3': '#9F993B',
    '3bis': '#A4D2E0',
    '4': '#B24A8E',
    '5': '#E49352',
    '6': '#90C195',
    '7': '#E8A7BA',
    '7bis': '#90C195',
    '8': '#9F993B',
    '9': '#BAB33A',
    '10': '#DBB448',
    '11': '#866034',
    '12': '#387F53',
    '13': '#A4D2E0',
    '14': '#5E287E'
}

# subway_data = {
#                 'stations' : {
#                         'numstation : [
#                                      station name,
#                                      ligne 
#                                      terminus Oui : 1 / Non : 0
#                                      branchement principale : 0, 1er branche : 1, 2e branche : 2],
#                 'join' : {
#                         's1': [],
#                         's2': [],
#                         'lon': []
#                          }
#                 }


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
            
            subway_data['stations'][int(line.split()[1])] = [' '.join(line.split()[2:-3]), 
                                                     line.split()[-3][1:], 
                                                     False if line.split()[-2][1:] == 'False' else True, 
                                                     0 if line.split()[-1]== '0' else 1 if line.split()[-1] == '1' else 2]

        if line[0] == 'E':
            
            subway_data['join']['summit1'].append(int(line.split()[1:][0]))
            subway_data['join']['summit2'].append(int(line.split()[1:][1]))
            subway_data['join']['lon'].append(int(line.split()[1:][2]))
            


# Create a dictionary to store metro lines

terminus = {}

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
    


# Create a dictionary to store metro's positions                
                
position = {}

with open('pospoints.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().split(';')
        if len(line) == 3:
            x_coord, y_coord, station_name = line
            x_coord = int(x_coord)
            y_coord = int(y_coord)
            position[(x_coord, y_coord)] = int(station_name)  # Replace @ with spaces


# Create an array to store metro's lines   
    # Reconstitution des lignes de métro   

from graph import Graph
graph = Graph()
lines = []

for line in terminus:
    temp_lines = [line]
    for branch in terminus[line]:
        temp = graph.bellman_ford(branch[0], branch[1])
        temp_lines.append(temp[1])
    lines.append(temp_lines)
        