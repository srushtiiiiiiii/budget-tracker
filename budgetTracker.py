


import os
import csv
import datetime
import matplotlib.pyplot as plt

def add_money():
   deposit =int(input("Enter the amount to deposit: "))
   global income
   income+=deposit
   
  
    
def enter_data():
  if not os.path.exists('data.csv'):
    with open('data.csv','w', newline = "") as file:
      writer=csv.writer(file)
      writer.writerow(['Date','Label','Expense'])
  
  if os.path.exists('data.csv'):
    read_file_list = list(csv.reader(open('data.csv','r')))
    if len(read_file_list) == 0:
      with open('data.csv','a', newline = "") as file:
        writer=csv.writer(file)
        writer.writerow(['Date','Label','Expense'])

  date = int(input("Enter the date: "))
  label =input("Label your Expense: ")
  expense= int(input("Expenditure:"))

  with open("data.csv",'a', newline="") as file:
    writer=csv.writer(file)
    writer.writerow([date,label,expense])



def choices():
  print("0 : Add money to Account.")  
  print("1 : Enter the data.")
  print("2 : Insights of data.")
  print("3 : Graphical view of data.")
  print("4 : Range graphical view.")
  
  try:
    choice = int(input())
  except:
      print("!Enter a valid Value..")
      
  return choice



def data_insights():
  try:
    with open('data.csv','r') as file:
      read = csv.reader(file)
      read_list=list(read)
      print(read_list)
      total_expense=0

      if(income <= 0):
        print("!! You don't have any income yet.Add some money first.");
        return

      for each in read_list[1:]:
        total_expense+=int(each[2])
        
      balance=income-total_expense
      print("Account Balance:",balance)
      print("Total Expenditure this month:",total_expense)
      percent=(total_expense/income * 100)
      print("Expediture is {:.4f}%  of income in {} days of this month.\n".format(percent,len(read_list)-1))
  except Exception as e:
     print("It looks like you don't have enough data yet.",e)   
     


def data_visualization():
  try:
    with open('data.csv','r') as file:
      dates=[]
      expense=[]
      read=csv.reader(file)
      file_list=list(read)
      for each in file_list[1:]:
        dates.append(int(each[0]))
        expense.append(int(each[2]))
   
      today=datetime.date.today()
      
      plt.plot(dates,expense,label='per month')
      plt.title("--Monthly Expenditure--")
      plt.xlabel(f"Date {today.month} {today.year}")
      plt.ylabel("Expense")
      plt.xticks(dates)  
      plt.legend()
      plt.show()
  except Exception as e:
    print("It looks like you don't have enough data yet.",e)



def limited_visualization(start_date,stop_date):
  try:
    with open('data.csv','r') as file:
      dates=[]
      expense=[]
      read=csv.reader(file)
      file_list=list(read)
      #print(len(file_list))
      if stop_date > (len(file_list)-1):
          print("!! Stop date out of range..")
          return
      
      for each in file_list[start_date:stop_date+1]:
        dates.append(int(each[0]))
        expense.append(int(each[2]))
      total_expense=sum(list(map(int,expense)))
      percent=total_expense/income*100
      print(f"Total expenditure in this period is {total_expense} which is {percent:.4f}% of the monthly income.")
      today=datetime.date.today()
      plt.plot(dates,expense,label='per day range')
      plt.title("--Range of days Expenditure--")
      plt.xlabel(f"Date {today.month} {today.year}")
      plt.ylabel("Expense")
      plt.xticks(dates)  
      plt.legend()
      plt.show()
  except Exception:
    print("It looks like you don't have enough data.")



if __name__=="__main__":
  income=0
  
  print("Select the choice::")
  running=True
  while running:
    choice = choices()
    if choice ==0: 
      add_money()
    elif choice == 1:
      enter_data()
    elif choice == 2:
      data_insights()
    elif choice == 3:
      data_visualization()
    elif choice ==4:
      print("Specify:")
      start=int(input("Start Date: "))
      stop =int(input("Stop Date: "))
      limited_visualization(start,stop)  
    else:
      print("!!INVALID choice.") 

    ask=input("Do you want to continue:(y/n) ")
    if  ask == 'n' or ask =='N':
      running = False
      
