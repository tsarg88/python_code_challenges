# Wild Roger is tasked with shooting down 6 bottles with 6 shots as fast as possible. Here are the different types of shots he could make:

# He could use one pistol to shoot a bottle with a "Bang!" in 0.5 seconds.
# Or he could use both pistols at once with a "BangBang!" to shoot two bottles in 0.5 seconds.
# Given a list of Bangs and BangBangs return the time (in seconds) it took to shoot down all 6 bottles. Make sure to only count Bangs and BangBangs. Anything else doesn't count.
# Examples:
# roger_shots(["Bang!", "Bang!", "Bang!", "Bang!", "Bang!", "Bang!"]) ➞ 3
# roger_shots(["Bang!", "Bang!", "Bang!", "Bang!", "BangBang!"]) ➞ 2.5
# roger_shots(["Bang!", "BangBangBang!", "Boom!", "Bang!", "BangBang!", "BangBang!"]) ➞ 2

def roger_shots(lst):
    total_botles = 0
    time = 0
    for n in lst:
        if n == 'Bang!':
            total_botles += 1
            time += 0.5
        if n == "BangBang!":
            total_botles += 2
            time += 0.5
    return time if total_botles == 6 else 'not 6 bottles!'
print(roger_shots(["Bang!", "Bang!", "Bang!", "Bang!", "Bang!", "Bang!"]))
print(roger_shots(["Bang!", "Bang!", "Bang!", "Bang!", "BangBang!"]))
print(roger_shots(["Bang!", "BangBangBang!", "Boom!", "Bang!", "BangBang!", "BangBang!"]))
