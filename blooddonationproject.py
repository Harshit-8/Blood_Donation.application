print("\n\n\n")
print("---------------------------------------++ WELCOME TO XYZ BLOOD DONATION Application by Harshit and Neeraj ++-----------------------------------------")
print("\n                                                  Login Portal\n\n")
print("Please follow the given instructions in order to log in")
print("\nFOR ADMIN LOGIN: PRESS 1")
print("FOR USER LOGIN : PRESS 2")
q=int(input())

class donor:
  x=0 #for counting no. of donors
  def __init__(self,name,age,sex,blood_group,platelets_count,wbc_count,rbc_count):
    self.name=name
    self.age=age
    self.sex=sex
    self.blood_group=blood_group
    self.platelets_count=platelets_count
    self.wbc_count=wbc_count
    self.rbc_count=rbc_count
    donor.x+=1

donor_1=donor('JONNY',20,'MALE','A+',200454,34768,55698)
donor_2=donor('GARV',44,'MALE','AB-',205466,36758,58790)
donor_3=donor('ANSHIKA',34,'FEMALE','O+',345670,45678,35987)
donor_4=donor('ASHMITA',29,'FEMALE','B-',354548,67647,45691)
donor_5=donor('ALAN',31,'MALE','A+',221232,57543,57764)
donor_6=donor('SIMRAN',33,'FEMALE','A-',275489,48654,65478)
donor_7=donor('RAHUL',48,'MALE','A+',238108,45668,65785)
donor_8=donor('KAMAL',24,'MALE','A+',257454,47694,51773)
donor_9=donor('LAXMAN',25,'MALE','AB+',255854,47604,51893)
donor_10=donor('PRAKASH',52,'MALE','A+',268472,48444,58793)


def blood_banks():
  print("\n\nFollowing blood banks are avalable near you: ")
  print("\n\n1. Dr. Lal Blood Bank")
  print("\n2. Central Blood Bank")
  print("\n3. Rotary Blood Bank")
  print("\n4. National Blood Bank")
  print("\n5. Mother Teresa Blood Bank")


def rare_blood_groups():
  print("\nDonors with rare blood groups and their details are listed below: ")
  print("\nNAME       AGE         SEX           BLOOD_GROUP\n")
  print("MADHAVAN    20         MALE           AB-\n")
  print("RASHI       34         FEMALE         O+\n")
  print("SNEHA       36         FEMALE         B-\n")
  print("ARJUN       22         MALE           AB+\n")

if q==1:
  print("\n\n-------------------- Welcome Admin ---------------------\n")
  w=input("Please enter your username: ")
  w.lower()
  d=1
  if w=='harshit':
    b=input("\nUsername found!\n\n Please enter your password: ")
    b.lower()
    if b=='123':
      print("\nSigned In successfully!")
      print("\n\n-------------Hello Admin Welcome back-----------------")
      while d==1:
         print("\n\nTell me what you want to know")
         print("\n1. Details of the Donors")       #Only admins can know the details of the donors
         print("\n2. Details of the Blood Banks")
         print("\n3. Details of the donors with rare blood groups")
         a=int(input("\n\nEnter a choice from the above: "))
         if a==1:
           l1=[donor_1,donor_2,donor_3,donor_4,donor_5,donor_6,donor_7,donor_8,donor_9,donor_10]
           for d in l1:
             print("\n")
             print(d.__dict__)

         elif a==2:
           blood_banks()
         elif a==3:
           rare_blood_groups()
         elif a==4:
           d=0
           print("Thank You ,Hope to see you soon!!")
         else:
           print("\nInvalid Choice!")
    else:
      print("\nPassword doesn't match!")

  else:
    print("\nAdmin not found. Please enter the correct Username")

elif q==2:
  print("\n\n-------------------- Welcome User ---------------------\n")
  w=input("Please enter your username: ")
  w.lower()
  if w=='neeraj' or 'siddhant' or 'vansh' or 'madhavi' or 'anmol':
    b=input("\nUsername found!\n\n Please enter your password: ")
    b.lower()
    c=1
    if b=='password':

      print("\nSigned In successfully!")
      while c==1:
          print("\n\n-------------Hello User Welcome back-----------------")
          print("\n\nTell me what you want to know")
          print("\n1. Number of the Donors available")  #Users can only know the number of donors available and not their details
          print("\n2. Details of the Blood Banks")
          print("\n3. Details of the donors with rare blood groups")
          print("\n4. To EXIT")
          a=int(input("\n\nEnter a choice from the above: "))
          if a==1:
            print("\nTotal number of Donors avalable is: ",donor.x) #donor.x for counting the number of donors
          elif a==2:
            blood_banks()
          elif a==3:
            rare_blood_groups()
          elif a==4:
            c=0;
            print("Thank You ,Hope to see you soon!!")
          else:
            print("Invalid choice ! Please Enter a valid one")
    else:
      print("\nPassword doesn't match!")

  else:
    print("\nUser not found. Please enter the correct Username")

else:
  print("\nWrong Choice! Please enter from the above choice only")