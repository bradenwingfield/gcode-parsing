def extract_data(file_path, slicer):
    with open(file_path, 'r') as open_file:
        file_data = open_file.readlines()

    # Set keyword (same for each slicer)
    bed_temperature_keyword = "M190"
    hotend_temperature_keyword = "M109"

    # Set keyword based on slicer
    if slicer == "Cura":
        time_keyword = ";TIME_ELAPSED:"
        filament_used_keyword = ";Filament used: "
    else: 
        time_keyword = "; estimated printing time (normal mode) = "
        filament_used_keyword = "; filament used [mm] = "

    # Initialize data
    bed_temperature = "No Data"
    hotend_temperature = "No Data"
    time = "No Data"
    filament_used = "No Data"

    # this will go through every line of the file: O(n)
    for row in file_data:
        if row.find(bed_temperature_keyword) != -1 and bed_temperature == "No Data":
             bed_temperature = row.split('S')[1].split()[0]
        if row.find(hotend_temperature_keyword) != -1 and hotend_temperature == "No Data":
             hotend_temperature = row.split('S')[1].split()[0]

        if slicer == "Cura":
            if row.find(time_keyword) != -1:
                time= row.strip(time_keyword).strip()
            if row.find(filament_used_keyword) != -1:
                filament_used= row.strip(filament_used_keyword).strip()
        else: 
            if row.find(time_keyword) != -1:
                time = row.strip(time_keyword).strip()
            if row.find(filament_used_keyword) != -1:
                filament_used = row.strip(filament_used_keyword).strip()
        
    print(f"Bed Temperature: {bed_temperature}°C")
    print(f"Hotend Temperature: {hotend_temperature}°C")
    print(f"Estimated Print Time: {time}")
    print(f"Filament Used: {filament_used} mm")
    

#Files provided in the directory
file_path = input("Gcode File Path: ")

while True:
    slicer = input("Slicer Software (Cura or Prusa): ")
    
    if slicer == "Cura" or slicer == "Prusa":
        extract_data(file_path, slicer)
        break
    else:
        print("Error: Please enter a valid slicer software.")