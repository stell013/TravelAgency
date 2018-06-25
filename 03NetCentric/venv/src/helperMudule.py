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
def reverseTrip():

    for flight in dic.keys():

        origin = flight.split("-")[0]
        dest = flight.split("-")[1]

        reverseString =  dest + "-" + origin
        reverseRoute.append(reverseString)


    return reverseRoute   #Return list of reverse trips


#reverseTrip()


#this is the only method called f
def commandHandler(command):

    command_Method = []

    if command == 'HELP' or command == 'help':

        command_Method = showAvailableCommands()

    if command == 'LIST':

        command_Method = listAllFlights(command)

    elif command.__contains__('SEARCHDEPARTURE'):

        command_Method = travelTo(command)

    elif command.__contains__('SEARCH'):

        command_Method = travelFrom(command)


    return  command_Method


def showAvailableCommands():
        commandsList = []
    


        commandsList.append('<SEARCH dest>')
        commandsList.append('<SEARCHDEPARTURE dest>')
        commandsList.append('<SEARCHALL DEST>')
        commandsList.append('<LIST>')
        commandsList.append('<BUY_TICKET>') 
        commandsList.append('<BUYRT_TICKET>') 
        commandsList.append('<RETURN_TICKET [where] [seats]>')
        commandsList.append('<RETURNRT_TICKET [where] [seats]>') 

        return commandsList 



#method that returns all flights
def listAllFlights(sentence):
    flightList = []
    reversedFlightList = []

    errorMessage = "Wrong command. Did you mean 'LIST' ? "

    if sentence == 'LIST':

      flights_list = dic.keys()

      for flight in flights_list:
          flightList.append(flight)

      for up in reverseRoute:
          reversedFlightList.append(up)

      for reversedEle in reversedFlightList:
          flightList.append(reversedEle)

    else:
      flightList.append(errorMessage)




    return flightList



#this method will return all places with DEST dest
def travelFrom(searchCommand):
     list_Dest = []
     reverseList_Dest = []

     errorMessage = "INVALID COMMAND. PLEASE TRY AGAIN, DID YOU MEAN 'SEARCH dest' ? "

     content = searchCommand.split(" ")
     command = content[0]
     dest = content[1]

     #try to validate it for capitalize letters
     if command == 'SEARCH':


         for flight in dic.keys(): #return all the complete trips

                 origin = flight.split("-")[0] #get the departure place

                 if flight.split("-")[1] == dest: #if dest is on dictionary
                   # print(origin)
                   list_Dest.append(origin)
                   # print(flight)  # In case we need the entire route


         for up in reverseRoute:

             reversedOrigin = up.split("-")[0]

             if up.split("-")[1] == dest:
                 #print(reversedOrigin)
                 #print(up)
                 reverseList_Dest.append(reversedOrigin)

         for reversedEle in reverseList_Dest:
             list_Dest.append(reversedEle)



     else:
         list_Dest.append(errorMessage)

     return list_Dest




#SEARCHDEPARTURE dep method



def travelTo(searchCommand):
    list_Dep = []
    reverseList_Dep = []

    errorMessage = "INVALID COMMAND. PLEASE TRY AGAIN, DID YOU MEAN 'SEARCHDEPARTURE dep' ? "

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
                 #print(flight) #In case we need the entire route
                 list_Dep.append(flight)



        for up in reverseRoute:

            reversedOrigin = up.split("-")[0]
            reversedDest = up.split("-")[1]

            if reversedOrigin == dep:
                # print(reversedDest)
                # print(up)
                reverseList_Dep.append(up)

        for reversedEle in reverseList_Dep:
            list_Dep.append(reversedEle)



    else:
        list_Dep.append(errorMessage)

    return list_Dep


#print("\nThe destinations available will be displyed\n")
#print(travelTo('SEARCHDEPARTURE MIA'))


def SearchALL():
    print("This is the SEARCHALL MIA ")

         #TO DO LIST

#for buytickets methods have the dictionary to decrease its seats
#update dictionary
#so next user entering the same command will have the real information

#also validate commands for  no capital letters

#HANDLE ERROS better