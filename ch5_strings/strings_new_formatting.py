thing = "woodchuck"
place = "lake"
print("The {} is in the {}".format(thing, place))
print("The {1} is in the {0}".format(thing, place))

print("The {thing} is in the {place}".format(thing="duck", place="bathtub"))

d = {"thing": "duck", "place": "bathtub"}
print("The {0[thing]} is in the {0[place]}.".format(d))

thing = "wraith"
place = "window"

print("The {:10s} is at the {:10s}".format(thing, place))
print("The {:<10s} is at the {:>10s}".format(thing, place))
print("The {:^10s} is at the {:^10s}".format(thing, place))

print("The {:!^10s} is at the {:!^10s}".format(thing, place))

# new formatting order:
# : - beginning
# symbol that fills empty space, default is ' ' (space)
# < - adjust by left, > - by right, ^ - center
# number of min width for string formatting
# . and number - amount of max symbols taken from original string
# s/d/... - type of argument


