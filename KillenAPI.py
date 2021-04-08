import requests
import json
import pandas as pd
import APIKEY
import math
import statistics
import re
import matplotlib.pyplot as plt

url = 'https://api.nasa.gov/planetary/apod'

api_key = APIKEY.__API_KEY


def get_date(pic_date):
    repeat = True
    split_input = re.split(r'\-', pic_date)
    while repeat:
        try:
            if not re.match(r"(\d{4})-(\d{2})-(\d{2})", pic_date):
                pic_date = input("Please re-enter the start date")
            else:
                break
        except ValueError:
            print("Wrong input")

    year = int(split_input[0])
    month = int(split_input[1])
    day = int(split_input[2])
# checks year
    if year > 2021 or year < 1995:
        new_year = input("Please enter a different year")
        split_input.remove(split_input[0])
        split_input.insert(0, new_year)
# checks month
    if month > 12 or month < 1:
        new_month = input("Enter different month")
        split_input.remove(split_input[1])
        split_input.insert(1, new_month)
# checks leap year
    if month == 2:
        if year % 4 == 0:
            if day > 29 or day < 1:
                new_day = input("Enter a different day")
                split_input.remove(split_input[2])
                split_input.insert(2, new_day)
        else:
            if day > 28 or day < 1:
                new_day = input("Enter a different day")
                split_input.remove(split_input[2])
                split_input.insert(2, new_day)

# checks august
    elif month == 8:
        if day > 31 or day < 1:
            new_day = input("Enter a different day")
            split_input.remove(split_input[2])
            split_input.insert(2, new_day)

    else:
        if month % 2 == 0:
            if day > 30 or day < 1:
                new_day = input("Enter a different day")
                split_input.remove(split_input[2])
                split_input.insert(2, new_day)

        else:
            if day > 31 or day < 1:
                new_day = input("Enter a different day")
                split_input.remove(split_input[2])
                split_input.insert(2, new_day)

    pic_date = '-'.join(split_input)

    if re.match(r"(\d{4})-(\d{2})-(\d{2})", pic_date):
        return pic_date


def graph():

    first_date = input("Enter the start date in YYYY-MM-DD: ")
    start_date = get_date(first_date)

    second_date = input("Enter the end date in YYYY-MM-DD: ")
    end_date = get_date(second_date)

    params = {
        'api_key': api_key,
        'hd': 'True',
        'start_date': start_date,
        'end_date': end_date
    }

    response = requests.get(url, params=params)
    json_data = json.loads(response.text)

    exp_len = []
    date_list = []

    for data in json_data:
        exp_len.append(len(data['explanation']))
        date_list.append(data['date'])

    date_dict = {"Length": exp_len}

    # for plot line
    # df = pd.DataFrame(date_dict, index=date_list)
    # lines = df.plot.line()

    # for chart
    df = pd.DataFrame(date_dict, columns=['Length'], index=date_list)
    df.index.name = 'Date'

    return df, exp_len, date_list


def avg_len(arr):
    count = 0
    for i in arr:
        count += i

    avg = count / len(arr)

    print()
    print("The average character length of the explanations is:", avg)


def low_len(arr, arr_date):
    lowestLen = arr[0]
    date_count = 0
    date = 0
    for length in arr:
        date_count += 1
        if length <= lowestLen:
            lowestLen = length
            date = arr_date[date_count - 1]

    print("Lowest length is: ", lowestLen, "characters, and the date is:", date)


def high_len(arr, arr_date):
    highestLen = arr[0]
    date_count = 0
    date = 0
    for i in arr:
        date_count += 1
        if i > highestLen:
            highestLen = i
            date = arr_date[date_count - 1]

    print("Highest length is: ", highestLen, "characters, and the date is:", date)


def top_25(arr):
    arr.sort()
    arr.reverse()
    count = 0
    for _ in arr:
        count += 1
    bottom = count * .25
    rounded = math.ceil(bottom)
    count_up = 0
    count_2 = 0
    for i in arr:
        count_up += i
        count_2 += 1
        if count_2 == rounded:
            break
    avg_25 = count_up / rounded

    print("The top 25% average explanation length is", avg_25, "characters long")


def bottom_25(arr):
    arr.sort()
    count = 0
    for _ in arr:
        count += 1
    bottom = count * .25
    rounded = math.ceil(bottom)
    count_up = 0
    count_2 = 0
    for i in arr:
        count_up += i
        count_2 += 1
        if count_2 == rounded:
            break
    avg_25 = count_up / rounded

    print("The bottom 25% average explanation length is", avg_25, "characters long")


def standard_dev(arr):
    print("The standard deviation is", (statistics.stdev(arr)))


def main():
    print("The lowest date you can enter is 1995-06-16")
    table, arr, date_arr = graph()
    print(table)
    avg_len(arr)
    print()
    low_len(arr, date_arr)
    print()
    high_len(arr, date_arr)
    print()
    bottom_25(arr)
    print()
    top_25(arr)
    print()
    standard_dev(arr)


if __name__ == '__main__':
    main()
