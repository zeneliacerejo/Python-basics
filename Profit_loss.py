actual_cost = float(input("Please enter the actual product price."))

sales_amount = float (input("Please enter the sales amount."))
if (sales_amount > actual_cost):
        amount = sales_amount - actual_cost
        print ("TotalProfit ={0}".format(amount))
else:
        print("No Profit!!!")
                
    