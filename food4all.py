# -*- coding: utf-8 -*-
"""Food4All.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WZ02qrtburz8Foqpv-gS5nrEU1a3X9B6

Functions
"""

import csv
import pandas as pd
import json

def userDetailsHeader():
   with open('User Details.csv','a',newline="") as file:
    myFile = csv.writer(file)
    myFile.writerow(["UserName","UserCity","UserZipcode","UserPreference"])

def storeuserprofile():
  with open('User Details.csv','a',newline="") as file:
    myFile = csv.writer(file)
   # myFile.writerow(["UserName","UserCity","UserZipcode","UserPreference"])

    #noOfRows = int(input("Enter how many preferences provided "))
    #for i in range(noOfRows):
    UserName = input("UserName "+ str(0+1) +": Enter UserName(As created by UI...): ")
    UserCity = input("UserCity "+ str(0+1) +": Enter UserCity: ")
    UserZipcode = input("UserZipcode "+ str(0+1) +": Enter UserZipcode(As created by UI...): ")
    UserPreference = input("UserPreference "+ str(0+1) +": Enter UserPreference(Vegetarian/Non-Vegetarian/Vegan): ")
    myFile.writerow([UserName,UserCity,UserZipcode,UserPreference])

def lookuserprofileAndGetPref(UserName):
  df = pd.read_csv(open(r'User Details.csv', 'rb'))
  #df
  df1 = df.loc[df['UserName'] == UserName]
  #df1
  #df = df.loc[df['flag'] == 'Not feasible'].copy() 
  return df1

def getFoodItemsOnPref(UserPreference):
  f = open('Database.json')
  
  # returns JSON object as 
  # a dictionary
  data = json.load(f)
  
  #for i in data[UserPreference]:
   #   print(i)
    
  # Closing file
  f.close()
 # test = UserPreference.lower()
  #print(test)
  return data.get(UserPreference.lower())

def getAvailabilityOnZipByPref(foodPrefer,zipcode):
  #print(zipcode)
  #print(foodPrefer)
  f = open('VendorDB.json')
  
  # returns JSON object as 
  # a dictionary
  vendordata = json.load(f)
  
  for sub in vendordata:
    if sub['ZipCode'] == zipcode:
        res = sub
        break
  #print(type(res))
  # printing result
  #print("The filtered dictionary value is : " + str(res))

  values = res['SuplusEndOfDayFood']

  # Indices list of matching element from other list
  # Using list comprehension + set() + enumerate()
  temp = set(foodPrefer)
  result = [val for i, val in enumerate(values) if val in temp]
  
  # printing result 
  #print("The matching element Indices list : " + str(result))
  return(str(result))
  #print(list_of_all_values)

"""Execute Section"""

userDetailsHeader()

storeuserprofile()

df = lookuserprofileAndGetPref('test1')
df['UserPreference'][0]

items = getFoodItemsOnPref(df['UserPreference'][0])
type(items)

getAvailabilityOnZipByPref(items,df['UserZipcode'][0])
