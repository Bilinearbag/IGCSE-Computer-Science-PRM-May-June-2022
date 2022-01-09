from tabulate import tabulate

i=0
bookingnumber = 1111
#following are tickets for one day:
day1adult = 20.00
day1child = 12.00
day1senior = 16.00
day1fam = 60.00
day1grp = 15.00
#following are tickets for two days:
day2adult = 30.00
day2child = 18.00
day2senior = 24.00
day2fam = 90.00
day2grp = 22.50
#following are extra attractions:
lionfeed = 2.50
pengfeed = 2.00
evebbq = 5.00 

while True:
       #table for ticket type:
       table1 = [['Option','Ticket Type', 'Cost for one day', 'Cost for two days'], ['1','One Adult', '$20.00', '$30.00'], ['2','One Child (An Adult may bring up to two children', '$12.00', '$18.00'], ['3','One Senior', '$16.00', '$24.00'], ['4','Family Ticket ( Upto two adults or seniors and three children)', '$60.00','$90.00'], ['5', 'Groups of six people or more, price per person', '$15.00', '$22.50']]
       print(tabulate(table1, headers ='firstrow', tablefmt='fancy_grid'))

       #table for extra attractions:
       table2 = [['Option', 'Extra attraction', 'Cost per person'], ['1', 'Lion feeding', '$2.50'], ['2','Penguin Feeding', '$2.00'], ['3', 'Evening barbecue (two-day tickets only)', '$5.00']]
       print(tabulate(table2, headers ='firstrow', tablefmt='fancy_grid'))




       #code for processing a booking
       basket = [['Ticket Type', 'Duration', 'Price']]
       attractbasket = [['Extra attraction', 'No. of Persons', 'Total Price']]


       #Input for Number of People
       adult = int(input("\nEnter number of adult:"))
       child = int(input("\nEnter number of children:"))
       senior = int(input("\nEnter the number of Seniors:"))

       

       while adult+child+senior>i:


              person = senior+adult+child
              if (adult+senior)*2<child:
                     print("\n There are not enough Adults or seniors to accompny the children; Please Start another booking")
                     break;

              print("\nAdults left without a ticket:", adult)
              print("Child left without a ticket:", child)
              print("Senior left without a ticket:", senior)
       
              #Number of Days
              day_input = int(input("\nDays of stay:\n 1: One day\n 2: Two Day\n Enter:"))

              #Offering a better alternative:
              
              #Alt.1 : Family Ticket
              if ((adult==2) or (senior==2) or (adult+senior==2)) and (child==3):
                     offer = input("\n The best tickt you can book is the Family ticket as it is Cheaper Would you like to take this offer (Y/N)\n Enter:")
                     if offer=="Y":
                            if day_input==1:
                                   if senior==0:
                                          senior=-1
                                   elif adult==0: 
                                          adult=-1
                     
                                   if adult+senior+child==5:
                                          basket.append(['Family Ticket',  'One Day', day1fam])
                                          print("\nFamily Ticket added Successfully!!")
                                          adult=adult-1
                                          senior=senior-1
                                          child=child-3
                                          continue;
                                          
    
                                   elif adult+child==5:
                                          basket.append(['Family Ticket',  'One Day', day1fam])
                                          print("\nFamily Ticket added Successfully!!")
                                          adult=adult-2
                                          child=child-3
                                          continue;

                                   elif senior+child==5:
                                          basket.append(['Family Ticket',  'One Day', day1fam])
                                          print("\nFamily Ticket added Successfully!!")
                                          senior=senior-2
                                          child=child-3
                                          continue;
                                   else:
                                          print("Not sufficient number of people")
                                          continue;

                            elif day_input==2:
                                   if senior==0:
                                          senior=-1
                                   elif adult==0: 
                                          adult=-1
                     
                                   if adult+senior+child==5:
                                          basket.append(['Family Ticket',  'Two Day', day2fam])
                                          print("\nFamily Ticket added Successfully!!")
                                          adult=adult-1
                                          senior=senior-1
                                          child=child-3
                                          continue;
                            
    
                                   elif adult+child==5:
                                          basket.append(['Family Ticket',  'Two Day', day2fam])
                                          print("\nFamily Ticket added Successfully!!")
                                          adult=adult-2
                                          child=child-3
                                          continue;
                            

                                   elif senior+child==5:
                                          basket.append(['Family Ticket',  'Two Day', day2fam])
                                          print("\nFamily Ticket added Successfully!!")
                                          senior=senior-2
                                          child=child-3
                                          continue;
                                   else:
                                          print("Not sufficient number of people")
                                          continue;

                     



              #Alt.2 Group Ticket:
              elif adult+senior>=6 and child<3 or child%3!=0:
                     offer = input("\nThe best tickt you can book is the Group ticket as it is Cheaper Would you like to take this offer (Y/N)\n Enter:")
                     if offer=="Y":
                            if day_input == 1:
                                   basket.append(['Group Ticket',  'One Day', day1grp*person])
                                   print("\nGroup Ticket added Successfully!!")
                                   adult=adult-adult
                                   child=child-child
                                   senior=senior-senior
                                   continue;
                            elif day_input==2:
                                   basket.append(['Group Ticket',  'Two Day', day2grp*person])
                                   print("\nGroup Ticket added Successfully!!")
                                   adult=adult-adult
                                   child=child-child
                                   senior=senior-senior
                                   continue;
       
              
              print(person); print(adult); print(senior); print(child)
              num=1
              if person >= 6 and (adult + senior > 2) and child > 3 and person%5==0 and child%3==0:
                     if day_input == 1:
                            while day1grp*person > num * 60 and num < 100:
                                   num += 1
                     if day_input == 2:
                            while day2grp*person > num * 90 and num < 100:
                                   num += 1
              if num < 100 and num != 0 and num != 1:
                     print("\nThe cheapest and economical ticket you could purchase are" , num-1, "Family Ticket. Would you like to take this offer (Y/N)")
                     offer = input("\n Enter:")
                     if offer=="Y":
                            if day_input==1:
                                   for k in range(num-1):
                                          basket.append(['Family Ticket',  'One Day', day1fam])
                                   print("\nFamily Ticket added Successfully!!")
                                   adult=0
                                   senior=0
                                   child=0
                                   continue;

                            elif day_input==2:
                     
                                   if adult+senior+child==5:
                                          basket.append(['Family Ticket',  'Two Day', day2fam])
                                          print("\nFamily Ticket added Successfully!!")
                                          adult=0
                                          senior=0
                                          child=0
                                          continue;
                                          
                            
              #Day 1 Ticket Booking
              if day_input == 1:
                     day1tickets = int(input("\nType in the option from the tickt type table for the ticket you wish to purchase (1, 2, 3, 4, 5)\n Enter:"))
              
                     #Adult Ticket Day 1
                     if day1tickets == 1:
                            if adult>=1:
                                   basket.append(['Adult Ticket', 'One Day',  day1adult])
                                   print("\nAdult Ticket added Successfully!!")
                                   adult=adult-1
                                      
                            else:
                                   print("An Adult is required to purchase an Adult ticket")
                                   continue;

 
                     #Child Ticket Day 1
                     elif day1tickets == 2:
                            if child>0 and adult>0 or senior>0:
                                   basket.append(['Child Ticket',  'One Day', day1child])
                                   print("\nChild Ticket added Successfully!!")
                                   child=child-1
                            
                            
                            else:
                                   print("An Child is required to be accompined by an Adult to purchase a Child Ticket")
                                   continue;

                            
                     #Senior Ticket Day 1 
                     elif day1tickets == 3:
                            if senior>=1:
                                   basket.append(['Senior Ticket',  'One Day', day1senior])
                                   print("\n Senior Ticket added Successfully!!")
                                   senior=senior-1
                            
                            else:
                                   print("A Senior is required to purchase a Senior Ticket")
                                   continue;


                     #Family Ticket Day 1
                     elif day1tickets == 4:
                            print("\nFor the Family Ticket, Enter the number of adults, seniors you would wish to bring. \nNOTE:Upto Two adults or seniors or one adult and one senior, \nand  three children required to purchase a Family Ticket ")
                            adult1=int(input("\n Enter number of adults:"))
                            senior1=int(input("\n Enter number of seniors:"))
                            
                     
                            if senior1==0:
                                   senior1=-1
                            
                            elif adult1==0: 
                                   adult1=-1
                     
                            if adult1+senior1+child==5:
                                   basket.append(['Family Ticket',  'One Day', day1fam])
                                   print("\nFamily Ticket added Successfully!!")
                                   adult=adult-1
                                   senior=senior-1
                                   child=child-3
                            
    
                            elif adult1+child==5:
                                   basket.append(['Family Ticket',  'One Day', day1fam])
                                   print("\nFamily Ticket added Successfully!!")
                                   adult=adult-2
                                   child=child-3
                            

                            elif senior1+child==5:
                                   basket.append(['Family Ticket',  'One Day', day1fam])
                                   print("\nFamily Ticket added Successfully!!")
                                   senior=senior-2
                                   child=child-3
                            
                           
                            else:
                                   print("\nUpto Two adults or seniors, and three children required to purchase a Family Ticket")
                                   continue;


                     #Group Ticket Day 1
                     elif day1tickets == 5:
                            j=0
                            grpperson = int(input("\nEnter the number of persons buying a group ticket. \nNOTE:Groups of six or more allowed only\n Enter:"))
                            if grpperson<=adult+child+senior:
                                   if grpperson>=6:
                                          while grpperson>j: 
                                                 adultg = int(input("Enter number of adults going for a group ticket, Enter:"))
                                                 childg=int(input("Enter number of children going for a group ticket, Enter:"))
                                                 seniorg=int(input("Enter number of seniors going for a group ticket, Enter:"))
                                                 if adultg<=adult and childg<=child and seniorg<=senior:
                                                        if adultg+seniorg+childg == grpperson:  
                                                               adult=adult-adultg
                                                               child=child-childg
                                                               senior=senior-seniorg 
                                                               basket.append(['Group Ticket',  'One Day', day1grp*grpperson])
                                                               print("\nGroup Ticket added Successfully!!")
                                                               grpperson=grpperson-(adultg+seniorg+childg)
                                                        else:
                                                               print("\nYou have entered a total of", adultg+childg+seniorg, "number of people which is less/more than your total number of people in the group ticket ", "(", grpperson ,")")
                                                 else:
                                                        print("Number of Adults/Senior/Child do not match. Try again.")
                                                        continue;               
                                   else: 
                                          print("\nThis ticket is valid for groups of six or more persons only. Please purchase a different ticket")
                                          continue;
                            else:
                                   print("Number of People in group ticket exceeds number of total people. Pls try again.")
                                   continue;


              elif day_input>2 or day_input<1:
                     print("\nInvalid Option, Please select correct option (1-5) from the Ticket Selection Table above")
       


              #Day 2 Ticket Booking      
              elif day_input == 2:
                     day2tickets = int(input("\nType in the option from the tickt type table for the ticket you wish to purchase(1, 2, 3, 4, 5):\n Enter:"))
              
                     #Adult Ticket Day 2
                     if day2tickets == 1:
                            if adult>=1:
                                   basket.append(['Adult Ticket', 'Two Day',  day2adult])
                                   print("\nAdult Ticket added Successfully!!")
                                   adult=adult-1
                            else:
                                   print("An Adult is required to purchase an Adult ticket")
                                   continue;


                     #Child Ticket Day 2             
                     elif day2tickets == 2:
                            if adult>0 and child>0 or senior>0:
                                   basket.append(['Child Ticket',  'Two Day', day2child])
                                   print("\nChild Ticket added Successfully!!")
                                   child=child-1
                            else:
                                   print("An Child is required to be accompined by an Adult to purchase a Child Ticket")                         
                                   continue;


                     #Senior Ticket Day 2
                     elif day2tickets == 3:
                            if senior>=1:
                                   basket.append(['Senior Ticket',  'Two Day', day2senior])
                                   print("\nSenior Ticket added Successfully!!")
                                   senior=senior-1
                            else:
                                   print("A Senior is required to purchase a Senior Ticket")
                                   continue;


                     #Family Ticket Day 2
                     elif day2tickets == 4:
                            print("\nFor the Family Ticket, Enter the number of adults, seniors you would wish to bring. \nNOTE:Upto Two adults or seniors or one adult and one senior, \nand  three children required to purchase a Family Ticket ")
                            adult1=int(input("\n Enter number of adults:"))
                            senior1=int(input("\n Enter number of seniors:"))
                            if adult1 !=adult:
                                   print("Number of adults are not equal")
                            if senior1 != senior:
                                   print("Number of senior are not equal")
                            if senior1==0:
                                   senior1=-1
                            elif adult1==0: 
                                   adult1=-1
                     
                            if adult1+senior1+child==5:
                                   basket.append(['Family Ticket',  'Two Day', day2fam])
                                   print("\nFamily Ticket added Successfully!!")
                                   adult=adult-1
                                   senior=senior-1
                                   child=child-3
                            
    
                            elif adult1+child==5:
                                   basket.append(['Family Ticket',  'Two Day', day2fam])
                                   print("\nFamily Ticket added Successfully!!")
                                   adult=adult-2
                                   child=child-3
                            

                            elif senior1+child==5:
                                   basket.append(['Family Ticket',  'Two Day', day2fam])
                                   print("\nFamily Ticket added Successfully!!")
                                   senior=senior-2
                                   child=child-3
                            
                           
                            else:
                                   print("Upto Two adults or seniors, and three children required to purchase a Family Ticket")
                                   continue;

              
                     #Group Ticket Day 2
                     elif day2tickets == 5:
                            m=0
                            grpperson = int(input("\nEnter the number of persons buying a group ticket. \nNOTE:Groups of six or more allowed only\n Enter:"))
                            if grpperson<=adult+child+senior:
                                   if grpperson>=6:
                                          while grpperson>m: 
                                                 adultg = int(input("Enter number of adults going for a group ticket, Enter:"))
                                                 childg=int(input("Enter number of children going for a group ticket, Enter:"))
                                                 seniorg=int(input("Enter number of seniors going for a group ticket, Enter:"))
                                                 if adultg<=adult and childg<=child and seniorg<=senior:
                                                        if adultg+seniorg+childg == grpperson:  
                                                               adult=adult-adultg
                                                               child=child-childg
                                                               senior=senior-seniorg 
                                                               basket.append(['Group Ticket',  'One Day', day1grp*grpperson])
                                                               print("\nGroup Ticket added Successfully!!")
                                                               grpperson=grpperson-(adultg+seniorg+childg)
                                                        else:
                                                               print("\nYou have entered a total of", adultg+childg+seniorg, "number of people which is less/more than your total number of people in the group ticket ", "(", grpperson ,")")
                                                 else:
                                                        print("Number of Adults/Senior/Child do not match. Try again.")
                                                        continue;
                                   else: 
                                          print("\nThis ticket is valid for groups of six or more persons only. Please purchase a different ticket")
                                          continue;
                            else:
                                   print("Number of People in group ticket exceeds number of total people. Pls try again.")
                                   continue;
              
              else:
                     print("\nInvalid Option, Please select correct option (1-5) from the Ticket Selection Table above")
                     continue;

              #Extra Attractions Booking Process:
       
              ques = input("\nWould u like to purchase any extra attractions?(Y/N)\n enter:")
              if ques == "Y":
                     an = int(input("\n How many Persons are going to purchase the Extra attractions:\n Enter:"))
                     ann = int(input("\n How many attractions would you like to purchase:\n Enter:"))
       
                     for p in range(ann):
                            attract = int(input("\nType in the option from the extra attractions table for the attraction you wish to purchase (1, 2, 3)\n Enter:"))
              
                            if attract == 1:
                                   attractbasket.append(['Lion Feeding', an, lionfeed*an])
                                   print("\n Lion Feeding attraction added Successfully!!")
              
                            elif attract == 2:
                                   attractbasket.append(['Penguin Feeding', an, pengfeed*an])
                                   print("\n Penguin Feeding added Successfully!!")
              
                            elif attract == 3:
                                   if day_input == 2:
                                          attractbasket.append(['Evening barbecue', an, evebbq*an])
                                   else:
                                          print("\nThis attraction is only available for two day tickets only")

                            else:
                                   print("\nInvalid Option, Please select correct option (1-3) from the Extra attractions Table above")
                                   continue;
              elif ques=="N":
                     continue;
              else:
                     print("Pls Enter Yes or No (Y/N)")
                     continue;

       #booking details output
       print('\nBooking Deatils:')
       bookingnumber=bookingnumber+1
       print("Your Booking Number is:", bookingnumber)
       print(tabulate(basket, headers ='firstrow', tablefmt='fancy_grid'))
       print(tabulate(attractbasket, headers='firstrow', tablefmt='fancy_grid'))

       #total for tickets
       totalbasket=[]
       for a in basket:
              if (isinstance(a, list)): 
                     for b in a:
                            totalbasket.append(b)
                            total = sum(filter(lambda i: isinstance(i, float), totalbasket))
              else:
                     break;

       #total for extra attractions
       totalattractbasket=[]
       for x in attractbasket:
              if (isinstance(x, list)): 
                     for y in x:
                            totalattractbasket.append(y)
                            totalatt = sum(filter(lambda i: isinstance(i, float), totalattractbasket))
              else:
                     break;

       #total cost :
       print("\nThe total cost of your booking = $", total+totalatt)
       
       repeat1 = input("\nWould you like to process another booking? (Y/N)")
       if repeat1=="Y":
              continue;
       else:
              print("\nYour transaction has been completed, Thank You. Have a Wonderful Vist!.")
              break;
