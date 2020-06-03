# Create a function that takes in year and month as input, then return what year it would be after n-months has elapsed.
# Example:
# after_n_months(2020, 24) ➞ 2022
# after_n_months(1832, 2) ➞ 1832
# after_n_months(1444, 60) ➞ 1449
# after_n_months(2020, '') ➞ 'month missing'
# after_n_months('', 2020) ➞ 'year missing'
# Notes:
# Assume that adding 12 months will always increment the year by 1.
# If no value is given for year or months, return "year missing" or "month missing".
# At least one value will be present.

def after_n_months(year, month):
	if not year:
		return 'year missing'
	if not month:
		return 'month missing'
	return year + month // 12
print(after_n_months(2020, 24))
print(after_n_months(1832, 2))
print(after_n_months(1444, 60))
print(after_n_months(2020, ''))
print(after_n_months('', 2020))
