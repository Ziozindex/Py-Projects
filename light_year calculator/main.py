c = 299792458  # speed of light (m/s)

years = float(input("How many light years?: "))

seconds = years * 31557600  # this convert to years to seconds
distance = c * seconds

distance_km = distance / 1000

print("Distance: ", distance_km, "kilometers")
