import psutil

print(psutil.cpu_times(True))

print(psutil.cpu_percent(True))
print(psutil.cpu_percent(percpu=True))

# very little info is given on psutil, better read docs (or call saul)

