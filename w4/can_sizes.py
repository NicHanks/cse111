import math

    

def main():
    with open('cans.csv', "r") as file_data:
        for line in file_data:
            line_data = line.split(',')
            name = line_data[0]
            radius = float(line_data[1])
            height = float(line_data[2])
            volume = compute_volume(radius, height)
            surface_area = compute_surface_area(radius, height)
            #print(radius, height)
            #print(volume, surface_area)
            #print(f"{name}, {volume:.2f}, {surface_area:.2f}")
            print(f"{name}, {compute_storage_efficiency(surface_area, volume):.2f},")


def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(surface_area, volume):
    storage_efficiency = volume/surface_area
    return storage_efficiency


main()