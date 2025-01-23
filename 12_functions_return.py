print("Return Statements")
# by default all functions return an empty object - something like None when there is no return statement

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return tax                                   # 25.0 <class 'float'>
    return amount, tax, total_amount             # (100, 25.0, 125.0) <class 'tuple'>
    return [amount, tax, total_amount]           # [100, 25.0, 125.0] <class 'list'> -- can print out individual elements
    return {amount, tax, total_amount}           # {100, 25.0, 125.0} <class 'set'>
    return f"{amount}, {tax}, {total_amount}"    # 100, 25.0, 125.0 <class 'str'>
    
price = value_added_tax(100)    
print(price, type(price))
