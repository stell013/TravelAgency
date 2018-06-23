dic = {}  # dictionary

def createDict(file ) :
  f  =  open(file , 'r')

  for line in f: #iterating through each line in the file

        content = line.split(" ")
        route = content[0]
        seats = content[1]
        cost = content[2]
        dic[route] = [seats, cost]

  #returns a list , then get element 0 of the list
  print("File has been uploaded")
  return True


createDict('routes.txt')



#method that returns all flights
def listAllFlights():
    flights_list = dic.keys()
    print("List of Flights:")
    print("---------------------")
    for flight in flights_list:
        print(flight)

listAllFlights()




#this method will return all places with DEST dest
def travelFrom(searchCommand):
     content = searchCommand.split(" ")
     command = content[0]
     dest = content[1]

     #try to validate it for capitalize letters
     if command == 'SEARCH':


         for flight in dic.keys(): #return all the complete trips

                 origin = flight.split("-")[0] #get the departure place

                 if flight.split("-")[1] == dest: #if dest is on dictionary
                    print(origin)
                  # print(flight) In case we need the entire route

     else:
         print ("INVALID COMMAND. PLEASE TRY AGAIN, DID YOU MEAN 'SEARCH dest' ? ")



#print("\nThe departures available will be displyed\n")
#dests = travelFrom('SEARCH MEX')


#SEARCHDEPARTURE dep method

def travelTo(searchCommand):
    content = searchCommand.split(" ")
    command = content[0]
    dep = content[1]     #departure name

    # try to validate it for capitalize letters
    if command == 'SEARCHDEPARTURE':

        for flight in dic.keys():  # return all the complete trips

            origin = flight.split("-")[0]  # get the departure place
            dest = flight.split("-")[1]

            if origin == dep:  # if dest is on dictionary
                # print(dest)
                 print(flight) #In case we need the entire route

    else:
        print ("INVALID COMMAND. PLEASE TRY AGAIN, DID YOU MEAN 'SEARCHDEPARTURE dep' ? ")


print("\nThe destinations available will be displyed\n")
dests = travelTo('SEARCHDEPARTURE HAV')


