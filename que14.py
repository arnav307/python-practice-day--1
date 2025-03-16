#1.	You’re waiting at a station and the announcer has just broadcast that your train is going to be 13445 seconds late. You need to work out in understandable terms what that means. You assume this is going to be quite a long time so you whip out your laptop to write a program to convert the seconds into hours, minutes and seconds, aiming to maximise readability by giving priority to the largest units, i.e. the resulting seconds and minute’s values must not be greater than 60.

#You will need four variables to hold: the total number of seconds; the number of hours; the number of minutes; and the number of remaining seconds. The example output should look something like this:
#13442 Seconds is: 3 Hours, 44 Minutes and 5 Seconds.

the_total_number_of_seconds=13445
second_to_hours=13445//3600
hours_to_min=13445%3600
extra_main=hours_to_min//60
min_to_sec=13445%60
print(min_to_sec)
print(f"Seconds is {second_to_hours} Hours,{extra_main} Minutes and {min_to_sec} remaining second")