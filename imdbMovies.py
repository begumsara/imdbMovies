import pandas as pd #help us tp create the data frame
import requests
from bs4 import BeautifulSoup
import numpy as np

#To retrieve movie data from the IMDb website, a URL is set and a GET request is sent to that URL.
url="https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
response = requests.get(url) #help us to get response form web pagepip install requests

#.status_code  ##200 means successfull request and we can proceed further with parsing
soup= BeautifulSoup(response.content,"html.parser")#to get content of web site
print(soup)#prints all html data in web site

#create empty list for datas
movie_name = []
year = []
time = []
rating = []
metascore = []
votes = []
gross = []

#there is a lot of data on the page, we don't need all of it to reduce data
movie_data = soup.findAll('div', attrs={'class':'lister-item mode-advanced'})#we found where the data belongs on the page using "inspect"
                                                                            ##we copy paste your name into attrs
print(movie_data) #to print isim belirterek simplicty yapıp aldığımız veriler için  

for store in movie_data:
    name = store.h3.a.text #film isminin nerede olduğunu bulduk --text kullandık çünkü sadece film ismini çekmek için
    movie_name.append(name) #to store movie name in movie_name

    mYear= store.h3.find('span',class_='lister-item-year text-muted unbold').text.replace('(','').replace(')','')
    year.append(mYear)

    runtime = store.p.find('span',class_='runtime').text.replace(' min',"")
    time.append(runtime)

    rate = store.find('div', class_='inline-block ratings-imdb-rating').text.replace('\n\n',"").replace('\n','')
    rating.append(rate)

    #some movies has no metascore its causes error use if method to this error 
    meta  = store.find('span', class_ = 'metascore').text.replace(' ', '') if store.find('span', class_ = 'metascore') else '^^^^^^'
    metascore.append(meta)

     #since, gross and votes have same attributes, that's why we had created a common variable and then used indexing
    value = store.find_all('span', attrs = {'name': 'nv'})
    vote = value[0].text
    print(vote)
    votes.append(vote) 

    #same values has not gross values do if else statement for these
    grosses = value[1].text if len(value)>1 else '*********' #len>1 gross valuemüz var demek (kelimemiz mouse ise len=5 olur)
    gross.append(grosses)
    print(grosses)



   #creating a dataframe using pandas library
movie_DF = pd.DataFrame({'Name of movie': movie_name, 'Year of relase': year, 'Watchtime': time, 'Movie Rating': rating, 'Metascore': metascore, 'Votes': votes, 'Gross collection': gross})
    #Saving data in Excel file:
movie_DF.to_excel("Top_100_IMDB_Movies.xlsx")
    print(movie_DF)

    #to get first 30 movies in list
print(movie_DF.head(30))

    print(mScore)
    print(rate)
    print(runtime)
    print(mYear)
    print(name) #prints all movie name data one by one
    print(movie_name) #prints all variables in movie_name
   
   #not necesarry for this example
print(np.count_nonzero(movie_name))#prints the number of data in movie_name

