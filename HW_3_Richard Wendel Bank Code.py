import csv
import os

csvpath = os.path.join("budget_data.csv")	
pathout = os.path.join("Budget Analysis.txt")
print(str(csvpath))
	
net_change=0
max_gain=["", 0]
max_loss=["", 0]
the_mean = 0
revenue_monthly=0
last_month_revenue=0
the_difference=0
net_change_list=[]

with open(csvpath) as revenue_data:
	reader = csv.reader(revenue_data)
	# next(reader, None)  # skip the headers
	header = next(reader)
	first_row = next(reader)
	# print(first_row)
	previous_profit = int(first_row[1])
	net_change_list.append(previous_profit)
	for row in reader:
		# print(type(row[1]), type(previous_profit))
		net_change = int(row[1])-previous_profit
		previous_profit=int(row[1])
		net_change_list.append(net_change)
	

			
		if net_change > max_gain[1]:
	            max_gain[1]=net_change
	            max_gain[0]=row[0]
		elif net_change < max_loss[1]:
	            max_loss[1]=net_change
	            max_loss[0]=row[0]
	        
	
	the_mean=sum(net_change_list)/len(net_change_list)

print("---------------------------------------")
#total number of months in the dataset
print("total number of months in the dataset")
print(len(net_change_list))
print("---------------------------------------")

#net amount of profit/loss over time
print("net amount of profit/loss over time")
print(sum(net_change_list))
print("---------------------------------------")

#The average of the changes in profit/loss over time period
print("The average of the changes in profit/loss over time period")
print(the_mean)
print("---------------------------------------")

#greatest increase in profits
print("greatest increase in profits")
print(max_gain)
print("---------------------------------------")

#greatest loss in profits
print("greatest loss in profits")
print(max_loss) 
print("---------------------------------------")



