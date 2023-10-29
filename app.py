import tkinter as tk
from data import position, subway_data, lines  # Assuming `position` and `subway_data` are defined in your data module
from graph import Graph  # Assuming the graph class exists
from main import find_directions, findname

graph = Graph()  # Your graph object

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

def create_left_panel(root):
    left_panel = tk.Frame(root, bg='white')
    left_panel.pack(side=tk.LEFT, fill=tk.Y)

    for line, color in line_colors.items():
        # Draw line circle with line number
        line_circle = tk.Canvas(left_panel, width=30, height=30, bg=color, highlightthickness=0)
        line_circle.create_oval(5, 5, 25, 25, fill=color)
        line_circle.create_text(15, 15, text=line, fill='black')
        line_circle.pack(pady=5)

        # Example icons (Replace with your own)
        direction_icon = tk.Label(left_panel, text="→", font=("Arial", 10))
        direction_icon.pack()

        # Station names
        station_label = tk.Label(left_panel, text="Station Name", font=("Arial", 8))
        station_label.pack()

def found_ID(name):
    for station_id, info in subway_data['stations'].items():
        if name == info[0]:
            return station_id
        
        
def get_station_coordinates(station):
    for (x, y), station_id in position.items():
        if station_id == station:
            return x, y
    return None, None
       

def change_color(depart_station, dest_station):
    reset_stations_color()
    shortest_path = graph.bellman_ford(depart_station, dest_station)[1]
    transfert = graph.get_transfert(depart_station, dest_station)
    route_directions = findname(find_directions(transfert, lines))
    time_sp = graph.calculateTime(depart_station, dest_station)

    
    for i in range(len(shortest_path) - 1):
        current_station = shortest_path[i]
        next_station = shortest_path[i + 1]
        
        for key, info in subway_data['stations'].items():
            for line in line_colors:
                if key == current_station and info[1] == line:
                    color1 = line_colors[line]
                if key == next_station and info[1] == line:
                    color2 = line_colors[line]

        # Initialize x1, y1, x2, y2 before the loop
        
        x1, y1 = get_station_coordinates(current_station)
        x2, y2 = get_station_coordinates(next_station)
            
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            # Draw a line between the stations
            line = canvas.create_line(x1, y1, x2, y2, fill=color1, width=4)

            # Color the stations
            canvas.itemconfig(stations[current_station], fill=color1)
            canvas.itemconfig(stations[next_station], fill=color2)

            # Store the line in a list to remove it later if needed
            lines_between_stations.append(line)
    
    create_transit_map(transfert, route_directions, time_sp)
    
            
def color_acpm(depart_station):
    reset_stations_color()

    acpm = graph.prim(depart_station)

    for i in range(len(acpm)):
        current_station = acpm[i][0]
        next_station = acpm[i][1]

        # Initialize x1, y1, x2, y2 before the loop
        
        x1, y1 = get_station_coordinates(current_station)
        x2, y2 = get_station_coordinates(next_station)

        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            # Draw a line between the stations
            line = canvas.create_line(x1, y1, x2, y2, fill="blue", width=4)

            # Color the stations
            canvas.itemconfig(stations[current_station], fill="blue")
            canvas.itemconfig(stations[next_station], fill="blue")

            # Store the line in a list to remove it later if needed
            lines_between_stations.append(line)
            
            
def create_transit_map(transfert, route_directions, time):
    
    for key, direction in zip(transfert, route_directions):
        for line,color in line_colors.items():
            if key == line :
                line_circle = tk.Canvas(frame, width=40, height=40, highlightthickness=0)
                line_circle.create_oval(5, 5, 35, 35, fill=color,outline= color )
                line_circle.create_text(20, 20, text=line, fill='black')
                line_circle.pack(pady=5)
        
        
    
        direction_icon = tk.Label(frame, text=f"→ {direction}", font=("Arial", 20))
        direction_icon.pack()
        
        stop = transfert[key][-1]
        stop_icon = tk.Label(frame, text=f"stop at {stop[1]}", font=("Arial", 20))
        stop_icon.pack()
       
       
    time_icon = tk.Label(frame, text=f"~{time} mn", font=("Arial", 70))
    time_icon.pack(ipady=50)
       
        
    
def reset_stations_color():
    for station_id in stations.keys():
        canvas.itemconfig(stations[station_id], fill="black")
    for line in lines_between_stations:
        canvas.delete(line)
    lines_between_stations.clear()
    
    widgets_to_keep = [departure_dropdown, destination_dropdown, submit_button ] # Replace with your actual dropdowns
    for widget in frame.winfo_children():
        if widget not in widgets_to_keep:
            widget.destroy()
    
         

def on_submit():
    change_color(found_ID(departure_var.get()), found_ID(destination_var.get()))
    
    # Display metro lines
    
def acpm_submit():
    color_acpm(found_ID(acpm_root.get()))

root = tk.Tk()
root.title("Station Map")

frame = tk.Frame(root, padx=8)
frame.pack(side=tk.LEFT)


canvas = tk.Canvas(root, width=1200, height=1000)
canvas.pack()

stations = {}
lines_between_stations = []

for (x, y), station_id in position.items():
    station = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
    stations[station_id] = station
    

departure_var = tk.StringVar(root)
departure_var.set("Select Departure")
departure_values = [info[0] for info in subway_data['stations'].values()]
departure_dropdown = tk.OptionMenu(frame, departure_var, *departure_values)
departure_dropdown.pack(anchor='n', pady=5)


destination_var = tk.StringVar(root)
destination_var.set("Select Destination")
destination_values = [info[0] for info in subway_data['stations'].values()]
destination_dropdown = tk.OptionMenu(frame, destination_var, *destination_values)
destination_dropdown.pack(anchor='n', pady=5)

submit_button = tk.Button(frame, text="Submit", command=on_submit)
submit_button.pack(anchor='n', pady=5)

# Create a frame to contain the new dropdown and button
top_frame = tk.Frame(root, padx= 8)
top_frame.place(x=root.winfo_screenwidth() - 950, y=0)  # Adjust the coordinates as needed

# Create the ACPM dropdown inside the new frame
acpm_root = tk.StringVar(root)
acpm_root.set("Select a vertex")
acpm_rootValues = [info[0] for info in subway_data['stations'].values()]
acpm_rootValues_dropdown = tk.OptionMenu(top_frame, acpm_root, *acpm_rootValues)
acpm_rootValues_dropdown.pack()

# Create a button inside the new frame
acpm_button = tk.Button(top_frame, text="Submit", command=acpm_submit)
acpm_button.pack(side=tk.RIGHT)

root.mainloop()




