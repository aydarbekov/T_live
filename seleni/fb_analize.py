import csv
import sys

maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
count = 1
all = []
all_likes = []
dates = []

with open('fb_profile.csv', 'r', newline='') as file:
    rows = csv.reader(file, delimiter='|')
    # print(len(rows))
    for row in rows:
        try:
            row[37]
        except:
            continue
        link_name_date = []
        friends = row[37]
        friends = friends.strip('[ ]')
        friends_all = friends.split(',')
        likes = row[35]
        likes = likes.strip('[ ]')
        likes_all = likes.split(',')
        date_i = row[4]
        print(date_i)
        date_i = date_i.split('г.')
        date_i = date_i[0].split(',')
        # print(date_i)
        for friend in friends_all:
            all.append(friend)
            # print(friend)
            # print(count)
            # count += 1
        for like in likes_all:
            all_likes.append(like)
        # print(len(date))
        if len(date_i) > 1:
            date_i = date_i[1].strip(' ')
            day, month, year = date_i.split(' ')
            if len(day) == 1:
                day = '0' + day
            print(month)
            if month == 'января':
                month = '01'
            elif month == 'февраля':
                month = '02'
            elif month == 'марта':
                month = '03'
            elif month == 'апреля':
                month = '04'
            elif month == 'мая':
                month = '05'
            elif month == 'июня':
                month = '06'
            elif month == 'июль':
                month = '07'
            elif month == 'августа':
                month = '08'
            elif month == 'сентября':
                month = '09'
            elif month == 'октября':
                month = '10'
            elif month == 'ноября':
                month = '11'
            elif month == 'декабря':
                month = '12'

            # dates.append(date)
            print(day, month, year)
            date_p = f'{day}-{month}-{year}'
            link_name_date.append(row[0])
            link_name_date.append(row[1])
            link_name_date.append(date_p)
            dates.append(link_name_date)

print(dates)
from datetime import datetime

for i in dates:
    date_1 = datetime.strptime(i[2], "%d-%m-%Y")
    date_2 = datetime.strptime('05-10-2020', "%d-%m-%Y")
    if date_1 >= date_2:
        # print(date_1)
        print(i)



from collections import Counter


# c = Counter(all)

# print(type(c))
# most = c.most_common(40)
# for mos in most:
#     print(mos)
#
# a = Counter(all_likes)
#
# print(type(a))
# most1 = a.most_common(40)
# for mos in most1:
#     print(mos)

print(dates)
c = Counter(dates)
# print(type(a))
most2 = c.most_common(30)
for mos in most2:
    print(mos)



# from datetime import datetime
# d = datetime.strptime('24 june 2020', "%d %B %Y")
# print(d)
