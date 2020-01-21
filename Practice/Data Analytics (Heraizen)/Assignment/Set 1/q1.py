cost_price=int(input("Enter the cost price?"))
selling_price=int(input("Enter the selling price?"))
if cost_price>selling_price:
    print("The User has incurred loss!")
    loss=cost_price-selling_price
    print("Quantum of loss is:",loss)
else:
    print("The User has incurred Profit!")
    profit=selling_price-cost_price
    print("Quantum of profit is:",profit)