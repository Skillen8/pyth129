
import requests
import json
import pandas as pd
import APIKEY
import math
import statistics
import matplotlib.pyplot as plt


url = 'https://api.nasa.gov/planetary/apod'

api_key = APIKEY.__API_KEY


def graph():
    # picDayStart = input("Enter a date in YYYY-MM-DD: ")
    # picDayEnd = input("enter date")
    params = {
        'api_key': api_key,
        'hd': 'True',
        'start_date': '2020-03-15',
        'end_date': '2021-03-20'
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

    for length in arr:
        date_count += 1
        if length <= lowestLen:
            lowestLen = length
            date = arr_date[date_count-1]

    print("Lowest length is: ", lowestLen, "characters, and the date is:", date)


def high_len(arr, arr_date):
    highestLen = arr[0]
    date_count = 0

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