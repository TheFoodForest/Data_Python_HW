import pandas as pd
import numpy as np 

bank_data = pd.read_csv("C:\\Users\\graha\\Desktop\\python_homework\\PyBank\\pybank_data.csv")

months = bank_data.loc[:,'Date'].values
total_months = len(months)

money = bank_data.loc[:,'Profit/Losses'].values
total_dolars = np.sum(money)

monthly_change = [bank_data.loc[0,'Profit/Losses']]

for i in range(1,total_months):
    try:
        change = money[i] - money[i-1]
        monthly_change.append(change)
    except IndexError:
        change = money[i]
        monthly_change.append(change)


average_change = round(np.average(monthly_change),2)

greatest_increase_index = np.argmax(monthly_change)
greatest_decrease_index = np.argmin(monthly_change)

print('Financial Report')
print("-"*35)
print('Total Months : {}'.format(total_months))
print('Total : ${}'.format(total_dolars))
print('Average Change: ${}'.format(average_change))
print('Greatest Increase in Profits: {} (${})'.format(months[greatest_increase_index], monthly_change[greatest_increase_index]))
print('Greatest Decrease in profits: {} (${})'.format(months[greatest_decrease_index], monthly_change[greatest_decrease_index]))

with open(r"C:\Users\graha\Desktop\python_homework\PyBank\pybank_text.txt", 'w') as file:
    lines  = ['Financial Report\n', '---------------------------------------\n',
             'Total Months: '+str(total_months), 'Total: $'+str(total_dolars)+'\n',
             'Average Change: $'+str(average_change)+'\n', 
             'Greatest Increase in Profits: '+str(months[greatest_increase_index])+' ($'+str(monthly_change[greatest_increase_index])+')\n',
             'Gratest Decrease in Profits: '+str(months[greatest_decrease_index])+' ($'+str(monthly_change[greatest_decrease_index])+')\n']

    file.writelines(lines) 