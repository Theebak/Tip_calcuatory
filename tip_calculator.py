




meal = float(raw_input ("Enter the cost of the meal "))
tax = float(raw_input ("Enter the tax percentage "))/100
tip = float(raw_input ("Enter the tip percentage "))/100

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal * tip


total = meal_with_tax + tip_value
	


print ('The base cost of the meal is ${:.2f}'.format(meal))
print ('The dollar value of the tax on the meal is ${:.2f}'.format(tax_value))
print ('The Tip that they will need to pay is ${:.2f}'.format(tip_value))
print ('The grand total for the meal, inclusive of tax and tip is ${:.2f}'.format (total))