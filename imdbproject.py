from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

score = []
titles = []
votes_list = []
year_list = []


movies = soup.find_all('td', class_='titleColumn')
rankings = soup.find_all('td', class_='ratingColumn imdbRating')
poster_col = soup.find_all('td', class_="posterColumn")

for vote in poster_col:
    votes = vote.find('span', attrs={'name': 'nv'})
    votes_list.append(votes['data-value'])

for movie in movies:
    name = movie.a.text
    titles.append(name)

for year in movies:
    year_num = year.span.text
    year_list.append(year_num)

for rank in rankings:
    score_num = rank.text.replace('\n', '')
    score.append(score_num)

df = pd.DataFrame({"Movie": titles,
                   "Year": year_list,
                   "IMDb Rating": score,
                   "Votes": votes_list
                   })

df.index = df.index + 1

print(df)

year_decade = 1920
count = 0
decade_low = 1920
decade_high = 1929
year_list.sort()
new_list = []
sorted_year = []
decades = []
each_decade = []

for i in year_list:
    new_list.append(re.findall(r'\d+', i))

for i in new_list:
    for item in i:
        sorted_year.append(item)

for j in range(0, 11):
    for i in sorted_year:
        if decade_low < int(i) <= decade_high:
            count += 1
    decades.append(count)
    count = 0
    each_decade.append(decade_low)
    decade_low += 10
    decade_high += 10

each_decade_s = []
for i in each_decade:

    var = str(i) + "s"
    each_decade_s.append(var)

print()
print("Number of movies from each decade in the top 250")
print('{:10} {:10}'.format("Decades", "Movies Per Decade"))
for i in range(len(decades)):
    print('{:1} {:6}'.format(each_decade_s[i], decades[i]))

yes_or_no = input("Would you like to search for a movie on the top 250: ")
counter = 0
if yes_or_no.lower() == "yes":
    search_movie = input("Enter the movie you would like to search: ")
    for title in titles:
        if search_movie.lower() == title.lower():
            print("This movie is on the chart")
            print("The score of", title, 'is', score[counter], ", It came out in", year_list[counter], 'with', votes_list[counter], 'votes',
                  ', number', counter+1, 'on the charts')
            break
        counter += 1

    if counter >= 250:
        print("Sorry, I can not find that movie")
else:
    print("Done")




