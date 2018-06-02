import datetime
import math

current_weight = 1000
goal_weight = 200
avg_lbs_week = 2

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(7)
    current_weight -= avg_lbs_week

print(end_date)
print(f'Reached goal in {(end_date-start_date).days // 7} weeks')


# weeks_to_go = (current_weight - goal_weight) / avg_lbs_week
#
# today = datetime.date.today()
#
# print("Weeks: ", weeks_to_go)
# print('Goal Reach Date: ', today + datetime.timedelta(weeks_to_go * 7))

