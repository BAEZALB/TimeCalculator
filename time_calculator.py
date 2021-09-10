# ideas: dump both start times and added time into straight minutes

# add times together and get new total time

# get hours by dividing total by 60 and converting to int

# get minutes by using total % 60

# calculate days elapsed by dividing total by 1440 (number of minutes in a day)

# create list with days of the week and mod 7 to map to a day of the week


# 
def add_time(start, duration, day = "none"):

    day = day.lower()

    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    start = start.split()
    period = start[1]
    start[0] = start[0].replace(":", " ")
    start = start[0].split()

    startMins = int(start[0]) * 60 + (int (start[1]))

    if(period == "PM"):
      startMins += 720

    duration = duration.replace(":", " ")
    duration = duration.split()
    totalMins = startMins + int(duration[0]) * 60 + (int (duration[1]))

    daysLater = int(totalMins / 1440)

    newHour = int((totalMins % 1440) / 60)

    newMinute = int(totalMins % 1440 % 60)

    newPeriod = "AM"

    if(newHour > 11):
      newHour = newHour % 12
      newPeriod = "PM"

    if(newHour == 0):
      newHour = 12
    
    if(day != "none"):
      currentDay = 0
      i = 0
      while(i < 7):
        if day == days[i]:
          currentDay = i
          break
        i += 1

      newDay = days[(currentDay + daysLater) % 7]
      newDay = newDay.capitalize()

    newHour = str(newHour)
    newMinute = str(newMinute)

    if len(newMinute) == 1:
      newMinute = "0" + newMinute

    newTime = newHour + ":" + newMinute + " " + newPeriod

    if(day != "none"):
      newTime += ", " + newDay
    
    if daysLater == 1:
      newTime += " (next day)"

    elif daysLater > 1:
      newTime += " (" + str(daysLater) + " days later)"

    return newTime