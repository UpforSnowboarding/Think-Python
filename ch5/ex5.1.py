import time

# epoch is 1 January 1970, time.time() returns time since epoch in seconds

print(time.time())

def hour(t):
    # 3600 seconds in an hour
    hours = t / 3600
    print("Hours passed since the epoch %f" % hours)

def minute(t):
    minutes = t / 60
    print("Minutes passed since the epoch %f" % minutes)

def second(t):
    seconds = t
    print("Seconds passed since the epoch %f" % seconds)

def days():
    secs = time.time()
    num_days = secs / (60 * 60 * 24)
    print("Days since the epoch %f" % num_days)


hour(time.time())
minute(time.time())
second(time.time())
days()
