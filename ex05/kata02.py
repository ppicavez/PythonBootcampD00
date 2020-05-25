# (hour, minutes, year, month, day)
t = (3, 30, 2019, 9, 25)

tens_diggit_month = ""
tens_diggit_day = ""
tens_diggit_year = ""
tens_diggit_hour = ""
tens_diggit_minute = ""

if t[0] < 10:
    tens_diggit_hour = "0"
if t[1] < 10:
    tens_diggit_minute = "0"
if t[3] < 10:
    tens_diggit_month = "0"
if t[4] < 10:
    tens_diggit_day = "0"

print("{}{}/{}{}/{} {}{}:{}{}".format(
    tens_diggit_month, t[3],
    tens_diggit_day, t[4],
    t[2],
    tens_diggit_hour, t[0],
    tens_diggit_minute, t[1]))
