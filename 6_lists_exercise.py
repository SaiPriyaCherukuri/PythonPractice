## - you sell lemonade over 2 weeks, the lists show the number of lemonades sold per week
## - Profit for each lemonade sold is 1.5$

# Add another day to week 2 by capturing a number as input
# Combine the 2 lists into a list called sales
# Calculate/Print how much you have earned on the best day, worst day, seperately and in total (3 prints)


sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

ele_w2 = input('Enter a number: ')
sales_w2.append(int(ele_w2))

sales.extend(sales_w1)
sales.extend(sales_w2)
 
best_day_earning = max(sales) * 1.5 
worst_day_earning = min(sales) * 1.5

print('Amount earned on the best day: ' + str(best_day_earning) + 'dollars')
print('Amount earned on the worst day: ' + str(worst_day_earning) + 'dollars')

total_earning = sum(sales) * 1.5
print('Total amount earned by selling Lemonades: ' + str(worst_day_earning) + 'dollars')



### solution 

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
sales.extend(sales_w1)
sales.extend(sales_w2)
#sales = sales_w1 + sales_w2
sales.sort()
worst_day_prof = sales[0] * 1.5
best_day_prof = sales[-1] * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')