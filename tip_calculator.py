from optparse import OptionParser

parser = OptionParser()

parser.add_option('-m','--meal', dest='meal_input', type="float")
parser.add_option('-x','--tax', dest='tax_input', type="float"	)
parser.add_option('-t','--tip', dest='tip_input', type="float", default=15.0)

(options,args)=parser.parse_args()

if not options.meal_input:
	parser.error ("You forgot to enter meal cost")
if not options.tax_input:
	parser.error ("You forgot to enter tax rate")

meal = options.meal_input
tax = options.tax_input/100
tip = options.tip_input	/100

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal * tip


total = meal_with_tax + tip_value
	


print ('The base cost of the meal is ${:.2f}'.format(meal))
print ('The dollar value of the tax on the meal is ${:.2f}'.format(tax_value))
print ('The Tip that they will need to pay is ${:.2f}'.format(tip_value))
print ('The grand total for the meal, inclusive of tax and tip is ${:.2f}'.format (total))