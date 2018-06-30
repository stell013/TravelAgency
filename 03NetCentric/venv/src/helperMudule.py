#elements for dictionary
dic = {}  # dictionary


reverseSeats =  []
reverseCost = []


reverseRoute = []  #list reversed
reverseString = " "



def createDict(fileObject) :
  f  =  open(fileObject, 'r')

  for line in f: #iterating through each line in the file

        content = line.split(" ")
        route = content[0]
        seats = int(content[1])
        reverseSeats.append(seats)
        costy = int(content[2])
        reverseCost.append(costy)
        dic[route] = [seats, costy] #Since I have 2 values for this dictionaries I have to asign them as a list and them access each 

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


#this is the only method called 

def commandHandler(command):

    command_Method = []
    errorMessage= 'WRONG COMMAND. PLEASE VERIFY THE SPELLING OR YOU CAN CONSULT <HELP>'

    if command == 'HELP' or command == 'help':

        command_Method = showAvailableCommands()

    elif command.__contains__('buyrtTicket'):

        command_Method = buyrtTicket(command)

    elif command == 'LIST' :

        command_Method = listAllFlights(command)

    elif command.__contains__( 'BUY_TICKET '):

        command_Method = buyTicket(command)
    
    elif command.__contains__('SEARCHDEPARTURE') :

        command_Method = travelTo(command)

    elif command.__contains__('searchall') :

        command_Method = searchaLL(command)

    elif command.__contains__('SEARCH') :

        command_Method = travelFrom(command)

    elif command.__contains__('RETURN_TICKET'):

        command_Method = returnTicket(command)

    elif command.__contains__('RETURNRT_TICKET'):

        command_Method = returnrtTicket(command)

    else: 
        command_Method.append(errorMessage)



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
        commandsList.append('<QUIT>')

        return commandsList 




#method that returns all flights
def listAllFlights(sentence):

    flightList = []
    reversedFlightList = []
    

    if sentence == 'LIST':

      flights_list = dic.keys()

      for flight in flights_list:
          flightList.append(flight)

      for up in reverseRoute:
          reversedFlightList.append(up)

      for reversedEle in reversedFlightList:
          flightList.append(reversedEle)


    return flightList



#this method will return all places with DEST dest
def travelFrom(searchCommand):
    list_Dest = []
    reverseList_Dest = []

    
    content = searchCommand.split(" ")
    command = content[0]
    dest = content[1]

     

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

     
    return list_Dest




#SEARCHDEPARTURE dep method



def travelTo(searchCommand):
    list_Dep = []
    reverseList_Dep = []

    

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



    return list_Dep


#print("\nThe destinations available will be displyed\n")
#print(travelTo('SEARCHDEPARTURE MIA'))

roundTrip_Dict ={}
def createDictroundedTrip():

    for f, s, c in zip(reverseRoute, reverseSeats, reverseCost):
        roundTrip_Dict[f] = [s,c ]  #Dictionary
        
    print(" Dictionary for roundedTrip has been created")
    return True 


def searchaLL(command):
    location = command.split(" ")[1]

    
    roundedInfo = []
    #Info = []
   
    for flight , flightA in zip(roundTrip_Dict.keys(), dic.keys()):
            locA= flightA.split("-")[0] 
            loc = flight.split("-")[1]    #dic[flightA][0]
         
            if locA == location: 
                rest = str(dic[flightA][0]) #seats
                money = str(dic[flightA][1])
                roundedInfo.append("\nORIGINAL" + '\n' + flightA + '\n' + "Seats left: " + rest + '\n' + "Cost each: " + money )

            if loc == location: 
                rest2 = str(roundTrip_Dict[flight][0])
                money2 = str(roundTrip_Dict[flight][1])
                roundedInfo.append("\nROUNDED" + '\n' + flight + '\n' + "Seats left: " + rest2 + '\n' + "Cost each: " + money2)
           
    return roundedInfo

#BUY_TICKET [where] [seats]
def buyTicket(command):

    seatList = []
    errorMessage= "INVALID NUMBER OF SEATS PLEASE TRY AGAIN"

    buy_Action = command.split(" ")[0]
    where = command.split(" ")[1]
    myseats = command.split(" ")[2]
    
    seats_Num = int(myseats)

    purchaseMessage = "PURCHASE TO -- %s -- SUCCESSFULLY COMPLETED\nCHECK YOUR EMAIL TO SEE THE RECEIPT. " % where

    for A  in  dic.keys(): #    traverse dictionary for flights in files 
        if where == A :
             #take the number of seats: seatsNo
             #substract the # entered from the seatsNo
             #update dictionary!!!
             actualSeats =  int(dic[A][0])
             if actualSeats != 0 and seats_Num > 0 and actualSeats >= seats_Num:
                actualSeats =  actualSeats - seats_Num 
                dic[A][0] = actualSeats  #update dictionary
                
                seatList.append(purchaseMessage)

             elif actualSeats < seats_Num:
                errorMessage =  "NOT POSSIBLE PURCHASE\n -- %d -- NUMBER OF SEATS AVAILABLE IN ROUTE: -- %s --." % (actualSeats, where)
                seatList.append(errorMessage)
                
             else:
                actualSeats = 0 
                seatList.append(errorMessage)

    
 
    for B in roundTrip_Dict.keys(): #traverse dictionary for reversed flights 
        if where == B:
           
            actualSeatsB =  int(roundTrip_Dict[B][0])
            if actualSeatsB !=0 and seats_Num > 0 and actualSeatsB >= seats_Num:
                actualSeatsB = actualSeatsB - seats_Num 
                roundTrip_Dict[B][0] = actualSeatsB #update dictionary
                
                seatList.append(purchaseMessage) 

            elif actualSeatsB < seats_Num:
                errorMessage =  "NOT POSSIBLE PURCHASE\n -- %d -- NUMBER OF SEATS AVAILABLE IN ROUTE: -- %s --." % (actualSeatsB, where)
                seatList.append(errorMessage)

            else: 
                actualSeatsB = 0 
                seatList.append(errorMessage)


    return seatList

def buyrtTicket(command):
    


    stringBk = " "
    seatList = []
    errorMessage = " "

    buy_Action = command.split(" ")[0]
    where = command.split(" ")[1]
    myseats = command.split(" ")[2]

    seats_Num = int(myseats)

    purchaseMessage = " "
    #purchaseMessage = "PURCHASE TO -- %s -- SUCCESSFULLY COMPLETED\nCHECK YOUR EMAIL TO SEE THE RECEIPT. " % where

    #handling string
    origin = where.split("-")[0]
    destino = where.split("-")[1]
    stringBk = destino + "-" + origin #new result 


    for A  in  dic.keys(): #    traverse dictionary for flights in files 
        if where == A or stringBk == A:
             #take the number of seats: seatsNo
             #substract the # entered from the seatsNo
             #update dictionary!!!
             actualSeats =  int(dic[A][0])
             if actualSeats != 0 and seats_Num > 0 and actualSeats >= seats_Num:
                actualSeats =  actualSeats - seats_Num 
                dic[A][0] = actualSeats  #update dictionary
                
                if A == where:
                    purchaseMessage = "PURCHASE TO -- %s -- SUCCESSFULLY COMPLETED\nCHECK YOUR EMAIL TO SEE THE RECEIPT. " % where
                elif A == stringBk:
                    purchaseMessage = "PURCHASE TO -- %s -- SUCCESSFULLY COMPLETED\nCHECK YOUR EMAIL TO SEE THE RECEIPT. " % stringBk

                
                seatList.append(purchaseMessage)

             elif actualSeats < seats_Num:
                if A == where:
                    errorMessage = "NOT POSSIBLE PURCHASE\n -- %d -- NUMBER OF SEATS AVAILABLE IN ROUTE: -- %s --." % (actualSeats, where)
                elif A == stringBk:
                    errorMessage = "NOT POSSIBLE PURCHASE\n -- %d -- NUMBER OF SEATS AVAILABLE IN ROUTE: -- %s --." % (actualSeats, stringBk)
                seatList.append(errorMessage)  
                
             else:
                actualSeats = 0 
                errorMessage = "INVALID NUMBER OF SEATS. PLEASE TRY AGAIN "
                seatList.append(errorMessage)

    
 
    for B in roundTrip_Dict.keys(): #traverse dictionary for reversed flights 
        if stringBk == B or where == B:
           
            actualSeatsB =  int(roundTrip_Dict[B][0])
            if actualSeatsB !=0 and seats_Num > 0 and actualSeatsB >= seats_Num:
                actualSeatsB = actualSeatsB - seats_Num 
                roundTrip_Dict[B][0] = actualSeatsB #update dictionary

                if B == stringBk:
                    purchaseMessage = "PURCHASE TO -- %s -- SUCCESSFULLY COMPLETED\nCHECK YOUR EMAIL TO SEE THE RECEIPT. " % stringBk
                elif B == where:
                    purchaseMessage = "PURCHASE TO -- %s -- SUCCESSFULLY COMPLETED\nCHECK YOUR EMAIL TO SEE THE RECEIPT. " % where

                
                seatList.append(purchaseMessage) 

            elif actualSeatsB < seats_Num:
                if B == where:
                    errorMessage = "NOT POSSIBLE PURCHASE\n -- %d -- NUMBER OF SEATS AVAILABLE IN ROUTE: -- %s --." % (actualSeatsB, where)
                elif B == stringBk:
                    errorMessage = "NOT POSSIBLE PURCHASE\n -- %d -- NUMBER OF SEATS AVAILABLE IN ROUTE: -- %s --." % (actualSeatsB, stringBk)
                seatList.append(errorMessage) 

            else: 
                actualSeatsB = 0 
                errorMessage = "INVALID NUMBER OF SEATS. PLEASE TRY AGAIN "
                seatList.append(errorMessage)

    

    return seatList
    

def returnTicket(command):

    seatList = []
    errorMessage= "INVALID NUMBER OF SEATS TO RETURN. PLEASE TRY AGAIN"

    buy_Action = command.split(" ")[0]
    where = command.split(" ")[1]
    myseats = command.split(" ")[2]
    
    seats_Num = int(myseats)

    purchaseMessage = "-- %d -- TICKETS SUCCESSFULLY RETURNED " % seats_Num

    

    for A  in  dic.keys(): #    traverse dictionary for flights in files 
        if where == A :
             #take the number of seats: seatsNo
             #substract the # entered from the seatsNo
             #update dictionary!!!
             actualSeats =  int(dic[A][0])

             if seats_Num > 0 :
                actualSeats =  actualSeats + seats_Num 
                dic[A][0] = actualSeats  #update dictionary
                 
                if seats_Num == 1:
                    purchaseMessage = "-- %d -- TICKET SUCCESSFULLY RETURNED " % seats_Num #if 1 overwrite message 

                seatList.append(purchaseMessage)

            
             else:
                actualSeats = 0 
                seatList.append(errorMessage)

    
 
    for B in roundTrip_Dict.keys(): #traverse dictionary for reversed flights 
        if where == B:
           
            actualSeatsB =  int(roundTrip_Dict[B][0])
            if  seats_Num > 0 :
                actualSeatsB = actualSeatsB + seats_Num 
                roundTrip_Dict[B][0] = actualSeatsB #update dictionary
                seatList.append(purchaseMessage) 

           
            else: 
                actualSeatsB = 0 
                seatList.append(errorMessage)


    return seatList




def returnrtTicket(command):
    stringBk = " "
    seatList = []
    errorMessage = " "

    buy_Action = command.split(" ")[0]
    where = command.split(" ")[1]
    myseats = command.split(" ")[2]

    seats_Num = int(myseats)

    purchaseMessage = "-- %d -- TICKETS SUCCESSFULLY RETURNED " % seats_Num
  

    #handling string
    origin = where.split("-")[0]
    destino = where.split("-")[1]
    stringBk = destino + "-" + origin #new result 




    for A  in  dic.keys(): #    traverse dictionary for flights in files 
            if where == A or stringBk == A:

                #take the number of seats: seatsNo
                #substract the # entered from the seatsNo
    
                actualSeats =  int(dic[A][0])

                if  seats_Num > 0 :
                    actualSeats =  actualSeats + seats_Num 
                    dic[A][0] = actualSeats  #update dictionary
                    seatList.append(purchaseMessage)

                
                else:
                    actualSeats = 0 
                    errorMessage = "INVALID NUMBER OF SEATS. PLEASE TRY AGAIN "
                    seatList.append(errorMessage)

    
 
    for B in roundTrip_Dict.keys(): #traverse dictionary for reversed flights 
            if stringBk == B or where == B:
           
                actualSeatsB =  int(roundTrip_Dict[B][0])

                if  seats_Num > 0 :
                    actualSeatsB = actualSeatsB + seats_Num 
                    roundTrip_Dict[B][0] = actualSeatsB #update dictionary
                    seatList.append(purchaseMessage) 


                else: 
                    actualSeatsB = 0 
                    errorMessage = "INVALID NUMBER OF SEATS. PLEASE TRY AGAIN "
                    seatList.append(errorMessage)

    return seatList



















