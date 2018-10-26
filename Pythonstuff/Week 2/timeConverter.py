#Get the number of seconds
total_secs = int(input("How many seconds, in total?  " ))
#calculate those seconds into days
days = total_secs // 86400
secs_days = total_secs % 86400
#calculate the remainder into hours
hours = secs_days // 3600
secs_hours = secs_days % 3600
#calculate the remainder into minutes
minutes =  secs_hours // 60
secs_minutes = secs_hours % 60
#calculate the remainder into seconds
seconds = secs_minutes 
#print out days if the number is above 0
if days == 0:
    print("  ")
else:
    print("Days=", days)
#print the number of hours & minutes
    print("Hours=", hours)
    print("Minutes=", minutes)
#print out seconds if the number is above 0
if seconds == 0:
    print("  ")
else:
    print("Seconds=", seconds)
print('Thank you')
