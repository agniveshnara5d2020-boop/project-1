print('-------Welcome to Billing System-------')
customer_name = input('enter name:')
n = int(input('enter number of items:'))
total_amount = 0 
for i in range(n):
    print(f'\nitem {i+1}')
    item_name = input('enter item name:')
    price = float(input('price:'))
    quantity = int(input('enter quantity:'))
    item_total = price*quantity
    total_amount += item_total
    print('{item name}total = {item_total}')

tax = total_amount*0.05
final_bill = total_amount + tax
amount_paid = float(input('\nenter amount paid:'))
due_amount = final_bill - amount_paid
print('\n========FINAL BILL========')
print('Customer name:',customer_name)
print('Total Amount:',total_amount)
print('Tax (5%):',tax)
print('Final Bill Amount:',final_bill)
print('Amount Paid:',amount_paid)

if due_amount > 0:
    print('status:payment pending')
    print('due amount:',due_amount)
elif due_amount == 0:
    print('status:payment complete')
    print('no due amount')
else:
    print('status:extra payment')
    print('change to return:',abs(due_amount))

print('=====================================')
print('thank you visit again')
