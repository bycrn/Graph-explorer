terminus_data = []

subway_data = {
                'stations' : {},
                'join' : {
                        'summit1': [],
                        'summit2': [],
                        'lon': []
                         }
                }
with open('metro.txt', 'r', encoding="UTF-8") as metro:
    for line in metro:
        if line[0] == 'V':
            num_stations = line.lower().split()[1]
            subway_data['stations'][num_stations] = [' '.join(line.lower().split()[2:-3])]
            #OBTENIR nbr ligne, terminus (s1, s2,..)
            # if line.split()[-2][1:] == 'True':
            #     print(line.split()[-3][1:], line.split()[1])
            
            
        # if line[0] == 'T':
        #         terminus_data.append([line.split()[1],line.split()[2],line.split()[3]])     
                

        # if line[0]== 'V':
        #         num_stations = line.lower().split()[1]
        #         subway_data['stations'][num_stations] = [line.lower()[7:-1]]

        if line[0] == 'E':
            subway_data['join']['summit1'].append(int(line.split()[1:][0]))
            subway_data['join']['summit2'].append(int(line.split()[1:][1]))
            subway_data['join']['lon'].append(line.split()[1:][2])
# print(terminus_data)    
 
for key in subway_data:
    print(subway_data[key])

