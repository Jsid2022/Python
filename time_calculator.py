def add_time(start, duration, day=""):
    """Calculate the Time."""
    # List of Days.
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # Variable To count days.
    day_count = 0
    # Variables to make Day(Title case)
    day = day.title()
    # get hours and mins of start time
    start_time = start.split(":")
    current_hour = int(start_time[0])
    # Sperate AM or PM from Minutes.
    min_list = start_time[1].split()
    current_min = int(min_list[0])
    is_pm = min_list[1]

    # Seperate Hours and Minutes of Duration time.
    # That is to be added.
    duration_time = duration.split(":")
    add_hour = int(duration_time[0])
    add_min = int(duration_time[1])
    
    check_am_or_pm = 0
    # Calculate time by duration hour into start hour.
    # and duration minutes to start minutes.
    calculate_hour = current_hour + add_hour
    calculate_min = current_min + add_min
    # Assign them to variables hours and minutes
    hours = calculate_hour
    minutes = calculate_min
    # These variables are for just formatting.
    next_day_str = ' (next day)'
    show_time = ""
    next_day = False
    
    # If duration hours are more or equal to 24 and
    # minutes more or equal to 60
    # Then get day count by dividing by 24 and increase
    # counter to 1
    if add_hour > 24 and calculate_min >= 60:
        day_count = add_hour // 24
        day_count += 1
    # Else if only duration hours are more or equal to 24
    # Then get the day count.
    elif add_hour >= 24:
        day_count = add_hour // 24

    # If calculate minutes are more or equal to 60
    # then increase the counter of calculate hour to 1
    # and get the remaining minutes by dividing it by 60
    # and assign variable to check_am_or_pm to decide
    # wether it is PM or AM.
    # Update the hours variable
    if calculate_min >= 60:
        calculate_hour += 1
        minutes = calculate_min % 60
        check_am_or_pm = calculate_hour % 24
        hours = calculate_hour
    # else if calculate minutes are less than 60
    # then just assign variable to check_am_or_pm to decide
    # wether it is PM or AM.
    else:
        check_am_or_pm = calculate_hour % 24
    
    # If check_am_or_pm is more or eqaul to 12
    # then set variable is_pm to AM if PM else: PM
    if check_am_or_pm >= 12:
        # If variable is PM and check_am_or_pm more than
        # 12 then also increase then set the next_day to True. 
        if is_pm == 'PM':
            day_count += 1# I don't know why I did This, But I'm too afraid to remove this lol.
            next_day = True
            is_pm = 'AM'
        else:
            is_pm = 'PM'
    # Set the hours in 12-hour format.
    hours = hours % 12
    # variable for formatting.
    days_later_str = f" ({str(day_count)} days later)" 
    
    # Get The variable in the form of Monday, Tuesday.......
    day_no = 0
    for days in days_list:
        if days == day.title():
            # Get the index of start day from days _list
            day_no = days_list.index(day)
    # add the days(that is to be added) to start day
    week_day = day_count + day_no
    week_day = week_day % 7
    # and set the day to variable day_no.
    day_no = days_list[week_day]

    # If hours is equal to 0 then it is 12 AM or PM.
    if hours == 0:
        hours = 12
    # if hours(that is to be added) then set the next_day to true.
    if add_hour == 24:
        next_day = True
    # Format the show Time according to these Conditions.
    if len(day) > 1:
        if day_count > 1:
            if minutes < 10:
                show_time = str(hours) + ':' + '0' + str(minutes) + ' ' + is_pm + ',' + ' ' + day_no + days_later_str
            else:
                show_time = str(hours) + ':' + str(minutes) + ' ' + is_pm + ',' + ' ' + day_no + days_later_str
        elif next_day:
            if minutes < 10:
                show_time = str(hours) + ':' + '0' + str(minutes) + ' ' + is_pm + ',' + ' ' + day_no + next_day_str
            else:
                show_time = str(hours) + ':' + str(minutes) + ' ' + is_pm + ',' + ' ' + day_no + next_day_str
        else:
            if minutes < 10:
                show_time = str(hours) + ':' + '0' + str(minutes) + ' ' + is_pm + ',' + ' ' + day_no
            else:
                show_time = str(hours) + ':' + str(minutes) + ' ' + is_pm + ',' + ' ' + day_no
    else:
        if day_count > 1:
            if minutes < 10:
                show_time = str(hours) + ':' + '0' + str(minutes) + ' ' + is_pm + days_later_str
            else:
                show_time = str(hours) + ':' + str(minutes) + ' ' + is_pm + days_later_str
        elif next_day or day_count == 1:
            if minutes < 10:
                show_time = str(hours) + ':' + '0' + str(minutes) + ' ' + is_pm + next_day_str
            else:
                show_time = str(hours) + ':' + str(minutes) + ' ' + is_pm + next_day_str
        else:
            if minutes < 10:
                show_time = str(hours) + ':' + '0' + str(minutes) + ' ' + is_pm
            else:
                show_time = str(hours) + ':' + str(minutes) + ' ' + is_pm
    return show_time
    
# print(add_time("3:00 PM", "3:10"))  # OK.
# print(add_time("11:30 AM", "2:32", "Monday"))  # OK.
# print(add_time("11:43 AM", "00:20"))  # OK.
# print(add_time("10:10 PM", "3:30"))  # OK.
# print(add_time("11:43 PM", "24:20", "tueSday"))  # OK.
# print(add_time("6:30 PM", "205:12"))  # OK.
# print(add_time("3:30 PM", "2:12")) # OK.
# print(add_time("11:55 AM", "3:12"))  # OK.
# print(add_time("9:15 PM", "5:30"))  # OK.
# print(add_time("11:40 AM", "0:25"))  # OK.
# print(add_time("2:59 AM", "24:00"))  # OK.
# print(add_time("11:59 PM", "24:05"))  # OK.
# print(add_time("8:16 PM", "466:02"))  # OK.
# print(add_time("5:01 AM", "0:00"))  # OK.
# print(add_time("3:30 PM", "2:12", "Monday"))  # OK.
# print(add_time("2:59 AM", "24:00", "saturDay"))  # OK.
# print(add_time("11:59 PM", "24:05", "Wednesday"))  # OK.
# print(add_time("8:16 PM", "466:02", "tuesday"))  # OK.
