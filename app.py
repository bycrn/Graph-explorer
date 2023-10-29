import tkinter as tk
from data import position, subway_data  # Assuming `position` and `subway_data` are defined in your data module
from graph import Graph  # Assuming the graph class exists

graph = Graph()  # Your graph object

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

    for i in range(len(shortest_path) - 1):
        current_station = shortest_path[i]
        next_station = shortest_path[i + 1]

        # Initialize x1, y1, x2, y2 before the loop
        
        x1, y1 = get_station_coordinates(current_station)
            
        x2, y2 = get_station_coordinates(next_station)
            

        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            # Draw a line between the stations
            line = canvas.create_line(x1, y1, x2, y2, fill="green", width=4)

            # Color the stations
            canvas.itemconfig(stations[current_station], fill="green")
            canvas.itemconfig(stations[next_station], fill="green")

            # Store the line in a list to remove it later if needed
            lines_between_stations.append(line)
            
def color_acpm(depart_station):
    reset_stations_color()

    acpm = graph.prim(depart_station)

    for i in range(len(acpm)):
        current_station = acpm[i][0]
        next_station = acpm[i][1]

        # Initialize x1, y1, x2, y2 before the loop
        for (x, y), station_id in position.items():
            if station_id == current_station:
                x1, y1 = x, y
            elif station_id == next_station:
                x2, y2 = x, y

        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            # Draw a line between the stations
            line = canvas.create_line(x1, y1, x2, y2, fill="blue", width=4)

            # Color the stations
            canvas.itemconfig(stations[current_station], fill="blue")
            canvas.itemconfig(stations[next_station], fill="blue")

            # Store the line in a list to remove it later if needed
            lines_between_stations.append(line)


def reset_stations_color():
    for station_id in stations.keys():
        canvas.itemconfig(stations[station_id], fill="black")
    for line in lines_between_stations:
        canvas.delete(line)
    lines_between_stations.clear()
    
    
    

station_lines = {
    'Station A': 'Line 1',
    'Station B': 'Line 1',
    'Station C': 'Line 1',
    'Station D': 'Line 2',
    'Station E': 'Line 2',
    'Station F': 'Line 2'
    # Add more stations and their respective lines as needed
}

# ... (Existing functions and UI elements)

def display_metro_lines():
    # Draw lines and station circles for each line
    for line_name in set(station_lines.values()):  # Gather unique line names
        line_color = 'red'  # Define line color or use different colors for each line
        stations_in_line = [station for station, line in station_lines.items() if line == line_name]

        for i in range(len(stations_in_line) - 1):
            current_station = found_ID(stations_in_line[i])
            next_station = found_ID(stations_in_line[i + 1])

            x1, y1 = get_station_coordinates(current_station)
            x2, y2 = get_station_coordinates(next_station)

            if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
                line = canvas.create_line(x1, y1, x2, y2, fill=line_color, width=3)

        for station_name in stations_in_line:
            station_id = found_ID(station_name)
            x, y = get_station_coordinates(station_id)
            if x is not None and y is not None:
                station_circle = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=line_color)
                canvas.create_text(x, y, text=station_name, fill='white')
                
                

def on_submit():
    change_color(found_ID(departure_var.get()), found_ID(destination_var.get()))
    
    # Display metro lines
    display_metro_lines()
    
def acpm_submit():
    color_acpm(found_ID(acpm_root.get()))

root = tk.Tk()
root.title("Station Map")

frame = tk.Frame(root)
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
departure_dropdown.pack()

destination_var = tk.StringVar(root)
destination_var.set("Select Destination")
destination_values = [info[0] for info in subway_data['stations'].values()]
destination_dropdown = tk.OptionMenu(frame, destination_var, *destination_values)
destination_dropdown.pack()

submit_button = tk.Button(frame, text="Submit", command=on_submit)
submit_button.pack()

# Create a frame to contain the new dropdown and button
top_frame = tk.Frame(root)
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




