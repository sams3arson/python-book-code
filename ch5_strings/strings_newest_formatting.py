thing = "wereduck"
place = "werepond"
print(f"The {thing} is in the {place}")

print(f"The {thing:>20} is in the {place:.^20}")
# syntax of formatting is same

print(f"{thing[-4:] =}, {place.title() =}")
# will print name of expression/variable to output

print(f"{thing = :>4.4}")

