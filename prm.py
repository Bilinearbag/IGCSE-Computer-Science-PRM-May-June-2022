#INITIALIZATION:

tickettype=["1. one adult", "2. one child(an adult may bring up to two children)", "3. one senior", "4. family ticket (up to two adults or seniors, and three children)", "5. groups of six people or more, price per person"]
cost1day=[20.00, 12.00, 16.00, 60.00, 15.00]
cost2days=[30.00, 18.00, 24.00, 90.00, 22.50]
attractions=["1. lion feeding", "2. penguin feeding", "3. evening barbecue (two-day tickets only)"]
costattractions=[2.50, 2.00, 5.00]
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
bookingnumber = 0
cost = 0


while True:
  # TASK 1 - Displaying the ticket options and the extra attractions available

  print("\n\n============ Ticket types ============\n\n")
  print (" - - - - Cost for one day - - - - \n")
  for x in range(0,5): 
    print(tickettype[x],": $", cost1day[x])
  print ("\n - Extra Attractions for one day - \n")
  for x in range(0,2):
    print(attractions[x],":$ ", costattractions[x])
  print ("\n\n - - - - Cost for two days - - - - \n")
  for x in range(0,5): 
    print(tickettype[x],": $", cost2days[x])
  print ("\n - Extra Attractions for day two - \n")
  for x in range(0,3):
    print(attractions[x],":$ ", costattractions[x])
  print ("\n\n - - - - Days available for booking - - - - \n")
  for x in range(0,7):
    print(days[x])
  day=str(input("\nEnter the day Sunday-Saturday: "))
  while day not in days:
        print("incorrect day")
        day=str(input("Please enter the day Sunday-Saturday: "))
  
  #TASK 2:

  #Input for Number of People
  adult = int(input("\nEnter number of adult:"))
  child = int(input("\nEnter number of children:"))
  senior = int(input("\nEnter the number of Seniors:"))
  person = senior+adult+child

  while (adult+senior)*2<child:
    print("\n There are not enough Adults or seniors to accompny the children; Please Start another booking")
    adult = int(input("\nEnter number of adult:"))
    child = int(input("\nEnter number of children:"))
    senior = int(input("\nEnter the number of Seniors:"))

  #Number of Days
  day_input = int(input("\nDays of stay:\n 1: One day\n 2: Two Day\n Enter:"))


  #THIS IS A FULLY AUTOMATED BOOKING PROCESS:

  print("This is a Fully Automated Booking Process. Please Select the type of Booking options available for you")
  #First Alternative - Individual Tickets:
  if day_input == 1:
    indvicost = (adult*20) + (child*12) + (senior*16)
    print("Your First Alternative is buying Individual Tickets for all the Persons")
    print("The Cost is", indvicost)
    opt1 = int(input("Would you like to process this booking option? (1 - Yes, 0 - No) \nEnter: "))
    if opt1==1:
      cost=indvicost
      continue;

  elif day_input == 2:
    indvicost = (adult*30) + (child*18) + (senior*24)
    print("Your First Alternative is buying Individual Tickets for all the Persons")
    print("The Cost is", indvicost)
    opt1 = int(input("Would you like to process this booking option? (1 - Yes, 0 - No) \nEnter: "))
    if opt1==1:
      cost=indvicost
      continue;


  if (adult + senior > 2) and child >= 3:
    adultdown = int(adult/2)*2
    childdown = int(child / 3)*3
    seniordown = int(senior/2)*2
    people = adultdown + childdown
    num=1
    if (adultdown==2) and childdown==3:
                              offer = input("\n The best tickt you can book is the Family ticket as it is Cheaper Would you like to take this offer (Y/N)\n Enter:")
                              if offer=="Y":
                                     if day_input==1:                                                 
                                            if adultdown+childdown==5:
                                                   basket.append(['Family Ticket',  'One Day', day1fam])
                                                   print("\nFamily Ticket added Successfully!!")
                                                   adult=adult-2
                                                   child=child-3
                                                   continue;
                                            else:
                                                   print("Not sufficient number of people")
                                                   continue;

                                     elif day_input==2:           
                                            if adultdown+childdown==5:
                                                   basket.append(['Family Ticket',  'Two Day', day2fam])
                                                   print("\nFamily Ticket added Successfully!!")
                                                   adult=adult-2
                                                   child=child-3
                                                   continue;
         
                                            else:
                                                   print("Not sufficient number of people")
                                                   continue;

                       elif adult>=child:
                              fam= math.floor(child/3)
                              print("\nThe cheapest and economical ticket you could purchase are" , fam , "Family Ticket. Would you like to take this offer (Y/N)")
                              offer = input("\n Enter:")
                              if offer=="Y":
                                     if day_input==1:
                                            for c in range(fam):
                                                   basket.append(['Family Ticket',  'One Day', day1fam])
                                            print("\nFamily Ticket added Successfully!!")
                                            adultsub = fam * 2
                                            childsub = fam * 3
                                            adult = adult-adultsub
                                            child = child-childsub
                                            continue;
                                     if day_input == 2:
                                            for c in range(fam):
                                                   basket.append(['Family Ticket',  'Two Day', day2fam])
                                            print("\nFamily Ticket added Successfully!!")
                                            adultsub = fam * 2
                                            childsub = fam * 3
                                            adult = adult-adultsub
                                            child = child-childsub
                                            continue;
                       
                       elif child>=adult:
                              fam= math.floor(child/3)
                              print("\nThe cheapest and economical ticket you could purchase are" , fam , "Family Ticket. Would you like to take this offer (Y/N)")
                              offer = input("\n Enter:")
                              if offer=="Y":
                                     if day_input==1:
                                            for g in range(fam):
                                                   basket.append(['Family Ticket',  'One Day', day1fam])
                                            print("\nFamily Ticket added Successfully!!")
                                            adultsub = fam * 2
                                            childsub = fam * 3
                                            adult = adult-adultsub
                                            child = child-childsub
                                            continue;
                                     if day_input == 2:
                                            for g in range(fam):
                                                   basket.append(['Family Ticket',  'Two Day', day2fam])
                                            print("\nFamily Ticket added Successfully!!")
                                            adultsub = fam * 2
                                            childsub = fam * 3
                                            adult = adult-adultsub
                                            child = child-childsub
                                            continue;














