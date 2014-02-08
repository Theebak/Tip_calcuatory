




meal = 44.50
tax = 0.0675
tip = 0.15

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal * tip


total = meal_with_tax + tip_value
print("%.2f" % total)

print ('The base cost of the meal is {:.2f}'.format(meal))
print ('The dollar value of the tax on the meal is {:.2f}'.format(tax_value))
print ('The Tip that they will need to pay is {:.2f}'.format(tip_value))
print ('The grand total for the meal, inclusive of tax and tip is {:.2f}'.format (total))