# Given a pH value, return whether that value is "alkaline", "acidic", or "neutral". Return "invalid" if the value given is less than 0 or greater 
# than 14.
# Notes:
# Values such as 6.9999 and 7.00001 should return "acidic" and "alkaline" respectively.
# Example:
# pH_name(5) ➞ "acidic"
# pH_name(8.7) ➞ "alkaline"
# pH_name(7) ➞ "neutral"

def pH_name(pH):
    if pH < 7 and pH >= 0:
        return 'acidic'
    if pH >= 7 and pH < 8:
        return 'neutral'
    if pH >= 8 and pH <= 14:
        return 'alkaline'
    else:
        return 'invalid'
print(pH_name(5))
print(pH_name(8.7))
print(pH_name(7))
print(pH_name(14.1))
