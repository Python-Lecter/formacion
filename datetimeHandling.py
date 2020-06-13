import datetime

start_time = datetime.datetime.now()
end_time = datetime.datetime.now() + datetime.timedelta(days=2.5)
total_time = end_time - start_time
print("Total Time= " + str(total_time))

days, seconds = total_time.days, total_time.seconds
print("Days= " + str(days) + " Seconds= " + str(seconds))

hours = days * 24 + seconds // 3600
print("Hours= " + str(hours))

minutes = (seconds % 3600) // 60
seconds = seconds % 60


