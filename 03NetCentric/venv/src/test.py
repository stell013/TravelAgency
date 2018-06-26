from helperMudule import *

createDict('routes.txt')
#print(getSeat())
reverseTrip()
me = createDictroundedTrip()

if me == True :
	for flight in roundTrip_Dict.keys():
		
		print("\nNew flight info" + '\n' + "Seats: " + roundTrip_Dict[flight][0] + '\n' + "Cost: " + roundTrip_Dict[flight][1])
		
else:
	print("Eroor has occured ")