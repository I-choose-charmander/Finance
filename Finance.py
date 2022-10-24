#!/usr/bin/env python3


"""
Created on Sun Feb 13 11:39:35 2022

@author: syate

This program will run your monthly income and give you an initial breakdown of income based on 50,30,20 Rule
Additional breakdown will show you your income vs outcome of the above breakdown.

All breakdowns are plotted.


"""
import matplotlib.pyplot as plt

def breakdown_income():
   
    #establsh base income
   
    Income = float(input("What is your monthly income? "))
   
    # Breakdowns for income
    Living = .5 * Income 
    Personal = .3 * Income
    Saving = .2 * Income
    
    Sizes = [ 50, 30, 20]
    Breakdown = [ '50 % Living', '30 % Personal', '20 % Savings']
    Breakdown_data = [Living, Personal, Saving]
    
    fig = plt.figure(figsize = ( 10, 7 ))
    plt.pie( Breakdown_data, labels = Breakdown)
    
    plt.show()
    
    
    if ( Living + Personal + Saving ) == Income:
    
        print('Your Living Amount based on your Income: ')
        print(Living)
    
        print('Your Personal Amount based on your Income: ')
        print(Personal)
    
        print('Your Saving Amount based on your Income: ')
        print(Saving)
    else:
        print(' Error ')
        
    Question1 = input('Do you want to run a breakdown for your monthly? ')

    if Question1 == "Yes": 
        
        
        LivingA = float(input('How much is monthly Rent? '))
        LivingB = float(input('How much are monthly Utilities? '))
        LivingC = float(input('How much for monthly Groceries? '))
        LivingD = float(input('How much for monthly Renters Insurance?'))
    
        Living_need = (LivingA + LivingB + LivingC + LivingD)
        Living_Leftover = Living - Living_need
    
        print('Your Living Essentials for the month: ', Living_need)
        print("  ")
        print('Your Living Left over for the month: ', Living_Leftover)
        print("   ")
    
        PersonalA = float(input('How much is your monthly Phone Bill? '))
        PersonalB = float(input('How much are is your monthly auto payment and insurance? '))
        PersonalC = float(input('How much for monthly subscriptions? '))
    
        Personal_need = (PersonalA + PersonalB + PersonalC)
        Personal_Leftover = Personal - Personal_need
    
        print('Your Personal Essentials for the month: ', Personal_need)
        print('   ')
        print('Your Personal Left over for the month: ', Personal_Leftover)
        print('   ')
    
        Personal_Savings = float(input('What is your Personal Save Goal? '))
        Current_Savings = float(input('What is your current Savings? '))
        print('   ')
    
        SavingA = Saving * .5
        
        Total_Leftover = (Living_Leftover + Personal_Leftover)
        print('Your Total Leftover is: ', Total_Leftover)
    
        if Personal_Savings != Current_Savings:
            print('Your Personal Savings for the Month: ', SavingA)
            print('   ')
            print('Your Investment Savings for the Month: ', SavingA)
            print('   ')
            
            Sub_Breakdowns = ['Living Need', 'Living_Leftover', 'Personal Need', 'Personal Leftover', 'Savings', 'Investmetns', 'Total Leftover' ]
            Sub_Breakdowns_data = [Living_need, Living_Leftover, Personal_need, Personal_Leftover, SavingA, SavingA, Total_Leftover ]
            
            fig = plt.figure(figsize = ( 10, 7 ))
            plt.pie(Sub_Breakdowns_data, labels = Sub_Breakdowns)
            
        
        else:
            print('You have met your goal!! Your Total Savings will go into income growth. ')
            print('Your Investment Savings is: ', Saving)
            print('   ')
            
            Sub_Breakdowns = ['Living Need', 'Living_Leftover', 'Personal Need', 'Personal_Leftover', 'Investmetns',  'Total Leftover' ]
            Sub_Breakdowns_data = [Living_need, Living_Leftover, Personal_need, Personal_Leftover, Saving, Total_Leftover ]
        
            fig = plt.figure(figsize = ( 10, 7 ))
            plt.pie(Sub_Breakdowns_data, labels = Sub_Breakdowns)
        
       
        
        
    elif Question1 == "No" :
        print('Thank you for your use! Have a great day!')
    else:
        print("Please answer Yes or No")
        return
    
        
    
    
   
breakdown_income()

