dic = {}  # dictionary
reverseRoute = []  #list reversed
reverseString = " "

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


#createDict('routes.txt')

#This method will reverse the each route in the file
def reverseTrip(sentence):
   if sentence == 'LIST':
    for flight in dic.keys():

        origin = flight.split("-")[0]
        dest = flight.split("-")[1]

        reverseString =  dest + "-" + origin
        reverseRoute.append(reverseString)

    #for index in reverseRoute:
        # print(index)
    return reverseRoute   #Return list of reverse trips


#reverseTrip('LIST')


#method that returns all flights
def listAllFlights():
    flights_list = dic.keys()
    print("List of Flights:")
    print("---------------------")
    for flight in flights_list:
        print(flight)

    print("\nNow the reversed list\n")
    for up in reverseRoute:
        print(up)






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
                   # print(flight)  # In case we need the entire route

         print("\nNow in the reversed list\n")

         for up in reverseRoute:

             reversedOrigin = up.split("-")[0]

             if up.split("-")[1] == dest:
                 print(reversedOrigin)
                 #print(up)



     else:
         print ("INVALID COMMAND. PLEASE TRY AGAIN, DID YOU MEAN 'SEARCH dest' ? ")



#print("\nThe departures available will be displyed\n")
#dests = travelFrom('SEARCH MIA')


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
                 #print(dest)
                 print(flight) #In case we need the entire route

        print("\nNow in the reversed list\n")

        for up in reverseRoute:

            reversedOrigin = up.split("-")[0]
            reversedDest = up.split("-")[1]

            if reversedOrigin == dep:
                # print(reversedDest)
                 print(up)



    else:
        print ("INVALID COMMAND. PLEASE TRY AGAIN, DID YOU MEAN 'SEARCHDEPARTURE dep' ? ")


#print("\nThe destinations available will be displyed\n")
#dests = travelTo('SEARCHDEPARTURE MIA')


def SearchALL():
    print("This is the SEARCHALL MIA ")


