s1 = "%s" % 42
s2 = "%d" % 42
s3 = "%x" % 42
s4 = "%o" % 42

# %s - string
# %d - digit
# %x - digit in hexadecimal
# %o - digit in octadecimal

print(s1, s2, s3, s4)

s5 = "%s" % 7.03
s6 = "%f" % 7.03
s7 = "%e" % 7.03
s8 = "%g" % 7.03

# %s - string
# %f - float
# %e - float in hexadecimal
# %g - float in octadecimal

print(s5, s6, s7, s8)

actor = "Rami Malek"
cat = "Vasya"
weight = 4.3

actor_string = "My favorite actor is %s"
cat_string = "My cat %s weighs %s kg"

print(actor_string % actor)
print(cat_string % (cat, weight))

thing = "woodchuck"
print("%s" % thing)

print("%12s" % thing)
print("%+12s" % thing)
print("%-12s" % thing)

# the number after % is amount of spaces we add
# + or nothing between % and number - adjust by right side
# - between % and number - adjust by left side

print("%.3s" % thing)
print("%12.3s" % thing)
print("%-12.3s" % thing)

# . and number after % of after number of spaces is max amount of symbols that
# is being taken from the string

thing = 98.6
print("%f" % thing)
print("%12f" % thing)
print("%+12f" % thing)
print("%-12f" % thing)
print("%.3f" % thing)
print("%12.3f" % thing)
print("%-12.3f" % thing)

thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%+12d' % thing)
print('%-12d' % thing)
print('%.3d' % thing)
print('%12.3d' % thing)
print('%-12.3d' % thing)


