
# Importing required modules
import time
import pandas as pd
import matplotlib.pyplot as pl
from tqdm import trange
from colorama import Fore
import sys
from playsound import playsound


# Defining required functions
def countdown():
    for i in trange(int(2),bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN,Fore.RESET),ascii=False, ncols=75):  
        time.sleep(1) 
    print("3 seconds rest")
    time.sleep(3)

def timer(t):
    print('')
    print('Workout starts in...')
    print('')
    while t:
        mins,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\n")
        time.sleep(1)
        t-=1
    print("\nLets go!!!")
t=5

def cooldown():
    print('')
    print("\nThat was a great workout... your workout is done")
    print("NOW LET'S COOLDOWN")
    print("\n\nFirst Excercise- Stretch arms and legs")
    countdown()
    print("\n\nSecond Excercise- Sit down and breathe deeply")
    countdown()
    print("\n\nThird Excercise- Knee to chest pose")
    countdown() 
    
def warm_up():
    print('')
    print("\nLET'S WARM UP QUICKLY ")
    print("\n\nFirst Excercise- Stretch arms and legs")
    countdown()
    print("\n\nSecond Excercise- 10 jumping jacks")
    countdown()
    print("\n\nThird Excercise- 5 burpees")
    countdown()   
  
        
def workout():
    print('')
    print('Choose a muscle category for workout')
    print('\n [1] Arms \n [2] Legs \n [3] Chest and Back \n [4] Core ')
    workout=int(input("Enter your choice:" ))
    while True:
        if workout in [1,2,3,4]:
            break
        else:
            playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')
            workout=int(input("Enter valid input:" ))
    if workout==1:
        warm_up()
        timer(t)
        print("\n\nFirst Excercise- Bicep Curls")
        countdown()
        print("\n\nSecond Excercise- Hammer Curls")
        countdown()
        print("\n\nThird Excercise- Lateral Curls")
        countdown()
        print("\n\nFourth Excercise- Bent Over Tricep Extention")
        countdown()
        print("\n\nFifth Excercise- Pull Up")
        countdown()
        cooldown()
    elif workout==2:
        warm_up()
        timer(t)
        print("\n\nFirst Excercise- Weighted Squats")
        countdown()
        print("\n\nSecond Excercise- Lunges")
        countdown()
        print("\n\nThird Excercise- Mountain Climbers")
        countdown()
        print("\n\nFourth Excercise- High Knees")
        countdown()
        print("\n\nFifth Excercise- Leg Raises")
        countdown()
        cooldown()
    elif workout==3:
        warm_up()
        timer(t)
        print("\n\nFirst Excercise- Lat Pulldown")
        countdown()
        print("\n\nSecond Excercise- Diamond Push Ups")
        countdown()
        print("\n\nThird Excercise- Rowing")
        countdown()
        print("\n\nFourth Excercise- Declined Push Ups")
        countdown()
        print("\n\nFifth Excercise- Dumbbell Press")
        countdown()
        cooldown()
    elif workout==4:
        warm_up()
        timer(t)
        print("\n\nFirst Excercise- Crunches")
        countdown()
        print("\n\nSecond Excercise- Reverse Crunches")
        countdown()
        print("\n\nThird Excercise- Toe Touch")
        countdown()
        print("\n\nFourth Excercise- Russian Twist")
        countdown()
        print("\n\nFifth Excercise- Plank")
        countdown()
        cooldown()

# Program starts
print('-'*75)
print('')
print('PROJECT WORK')     
print('Welcome to the Health Tracker program!!!')
print('')
print('-'*75)
print("")
playsound(r'E:\Users\rajas\Documents\Rajas College\Startup.mp3')
print('')
print('\n [1] Calculate BMR and calorie intake \n [2] Compare your records \n [3] Get a predefined workout')
print('')
print('Choose the number corresponding to the description.')

start=int(input("Enter your choice:" ))

while True:
    if start in [1,2,3]:
        break
    else:
        playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')
        start=int(input("Enter a valid choice:" ))
        
# Create account part        
if start==1:
    print('')
    name=str(input("Enter your name: "))
    weight=float(input('Enter your weight(in kg):'))
    height=float(input('Enter your height(in cm):'))
    age=int(input('Enter your age (in years): '))
        
    while age<18:
        playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')
        print('You are underage!!!')
        age=int(input('Enter your age (in years 18 or above): '))
    
    gender=str(input('Enter your gender(m/f/t):' ))
    while gender not in ('m','f','M','F','t','T'):
        print('Enter M or F')
        gender=str(input('Enter your gender(m/f/t):' ))
    if gender=='m' or gender=='M':
        BMR = round((13.39*weight)+( 4.799*height) -( 5.677*age) + (88.362),2)
    elif gender=="f" or gender=='F':
        BMR = round((9.247*weight) + (3.098*height) - (4.330*age) + (447.593),2)
    elif gender=="t" or gender=='T':
        BMR = round((11.79*weight) + (4.087*height) - (4.969*age) + (223.864),2)
        
    print("")
    print("")
    print(name,',your BMR(Basal Metabolic Rate) is: ',BMR)
    print('')
    
    print('Level of activity: ')
    print('[1] for little/no excercise ')
    print('[2] for moderate excercise(3-4 days/week) ')
    print('[3] for very active excercise (6-7 days/week) ')
    x=int(input('Enter your choice: '))
    while x not in (1,2,3):
        playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')
        print('Invalid entry!!')
        x=int(input('Enter your choice: '))
    if x==1:
        cal=round(BMR*1.2,2)
    elif x==2:
        cal=round(BMR*1.55,2)
    elif x==3:
        cal=round(BMR*1.725,2)

    print('')

    print('Calorie intake per day: ')
    print('')
    print('To maintain weight: ', cal)
    print('')
    print('For mild weight loss[0.25kg/week]: ', cal-250)
    print('')
    print('For weight loss[0.5kg/week]: ', round(cal-500,2))
    print('')
    print('For extreme weight loss[1kg/week]: ', round(cal-1000,2))
    print('')
    print('For mild weight gain[0.25kg/week]: ', cal+250)
    print('')
    print('For weight gain[0.5kg/week]: ', cal+500)
    print('')
    print('For fast weight gain[1kg/week]: ', cal+1000)
    print('')
    print('')        
    
    print('\n [1] To start your workout \n [2] To end the session')
    start_1=int(input('Enter your choice: '))
    while True:
       
        if start_1 in [1,2]:       
            if start_1==1:
                workout()
                while True:
                    repeatworkout=int(input("[1] Workout \n[2] Confirm exit \nEnter:  "))
                    if repeatworkout in [1,2]:
                        if repeatworkout==1:                           
                            workout()
                        elif repeatworkout==2:
                            playsound(r'E:\Users\rajas\Documents\Rajas College\Shutdown Short.mp3')
                            print("Thanks for your time,", name,"!")
                            print('Have a great day!')                           
                            sys.exit()
                        else:
                            playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')
                            repeatworkout=int(input("Enter a valid choice:  "))
            elif start_1==2:
                print(name,', are you sure you want to exit?')
                repeatworkout=int(input("[1] Workout \n[2] Confirm exit \nEnter:  "))
                while True:                   
                    if repeatworkout in [1,2]:
                        if repeatworkout==1:
                            workout()
                            repeatworkout=int(input("[1] Workout \n[2] Confirm exit \nEnter:  "))
                            while True:                   
                                if repeatworkout in [1,2]:
                                     if repeatworkout==1:
                                        workout()
                                        repeatworkout=int(input("[1] Workout \n[2] Confirm exit \nEnter:  "))
                                     elif repeatworkout==2:                                        
                                        print("Thanks for your time,", name,"!")
                                        playsound(r'E:\Users\rajas\Documents\Rajas College\Shutdown Short.mp3')
                                        print('Have a great day!')
                                        sys.exit()
                                else:
                                     playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')                                   
                                     repeatworkout=int(input("Enter a valid choice:  "))
                
                        elif repeatworkout==2:
                            print( "Thanks for your time,", name,"!")
                            playsound(r'E:\Users\rajas\Documents\Rajas College\Shutdown Short.mp3')
                            print('Have a great day!')
                            sys.exit()
                    else:
                        playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')
                        repeatworkout=int(input("Enter a valid choice:  "))
                
        else:
            playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')
            start_1=int(input('Enter a valid choice: '))
         
# Compare records part         
elif start==2:
    dic={'Name':['Rajas','Shreyash','Johnny','Naidu','Aadish'],
         'Weight':[62,96,92,94,96],
         'Height':[181,179,184,183,186],
         'Age':[18,19,19,23,30],
         'BMR':[1684.97,2130.637,2074.29,2081.87,2164.23]}
    data=pd.DataFrame(dic)
    print('Before we compare your records we would like to know a couple of details about you.')
    n_n=input('Enter your name: ')
    n_w=int(input('Enter your weight(in kg): '))
    n_h=int(input('Enter your height(in cm): '))
    n_a=int(input('Enter your current age: '))

    g=str(input('Enter your gender(m/f/t):' ))
    
    while g not in ('m','f','M','F','T','t'):
    
        print('Enter M or F')
        g=str(input('Enter your gender(m/f/t):' ))
    if g=='m' or g=='M':
        n_BMR = (13.39*n_w)+( 4.799*n_h) -( 5.677*n_a) + (88.362)
    elif g=="f" or g=='F':
        n_BMR = (9.247*n_w) + (3.098*n_h) - (4.330*n_a) + (447.593)
    elif g=="t" or g=='T':
        n_BMR = round((11.79*n_w) + (4.087*n_h) - (4.969*n_a) + (223.864),2)    

    print('')
    print('Your updated BMR is',n_BMR)    
    print('')

    newrow= {'Name': n_n,'Weight':n_w,'Height':n_h,'Age':n_a,'BMR':n_BMR}
    data1=data.append([newrow],ignore_index =True)
    print('')
    while True:
        repeatworkout=int(input("[1] Workout \n[2] Compare with other records \n[3] Confirm exit \nEnter your choice: "))
        if repeatworkout in [1,2,3]:
            if repeatworkout==1:
                workout()
            elif repeatworkout==2:
                print('')
                print('New records(weight)')
                data1.plot(x ='Name', y='Weight', kind = 'bar')
                print('Please wait, loading graphs...')
                time.sleep(3)
                pl.show()
                print('')
                print('New records(height)')
                data1.plot(x ='Name', y='Height', kind = 'bar')
                print('Please wait, loading graphs...')
                time.sleep(3)
                pl.show()
                print('')
                print('New records(BMR)')
                data1.plot(x ='Name', y='BMR', kind = 'bar')
                print('Please wait, loading graphs...')
                time.sleep(3)
                pl.show()
                print('')
                print('Would you like to see your graphs again?')
                
                
            elif repeatworkout==3:
                print("Thanks for your time!")
                playsound(r'E:\Users\rajas\Documents\Rajas College\Shutdown Short.mp3')
                print('Have a great day!')
                sys.exit()
        else:
            playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')
            print('Invalid input!!!')
            repeatworkout=int(input("Enter a valid choice:"))
            
# Predefined workout part          
elif start==3:
    workout()
    print('\n [1] To repeat workout \n [2] To end the session')
    start_1=int(input('Enter your choice: '))
    while True:
        if start_1 in [1,2]:
            break
        else:
            playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')
            start_1=int(input('Enter valid choice: '))
    if start_1==1:
        workout()
        while True:
            repeatworkout=int(input("[1] Workout \n[2] Confirm exit \nEnter your choice: "))
            if repeatworkout in [1,2]:
                if repeatworkout==1:
                    workout()
                elif repeatworkout==2:
                    print("Thanks for your time!")
                    playsound(r'E:\Users\rajas\Documents\Rajas College\Shutdown Short.mp3')
                    print('Have a great day!')
                    sys.exit()
                else:
                    playsound(r'E:\Users\rajas\Documents\Rajas College\Error Short.mp3')
                    print('Invalid input!!!')
                    repeatworkout=int(input("Enter a valid choice:"))
      
    elif start_1==2:
        print( 'Thank you for your time!')
        playsound(r'E:\Users\rajas\Documents\Rajas College\Shutdown Short.mp3')
        print('Have a great day!')