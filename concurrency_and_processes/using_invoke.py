# module 'invoke' lets you define local tasks
# module 'fabric2' lets you define remote tasks

from invoke import task

@task
def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("Local time is", time_str)

