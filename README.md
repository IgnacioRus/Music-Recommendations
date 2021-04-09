<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Music Recommendations
*Ignacio Rus Prados*

*DAFT-MAR21, Remote, 09/04/2021*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description

I have been hired as Data Analysts by Gnod, a company that owns a website that provides music recommendations, among other things. They hired me to improve their algorithms and set the ground for a collaboration with bigger companies such as Spotify. My first task is to develop a new feature: song recommendations based on your favorite songs.

My approach was the following: if the song provided by the user is within the Top 100 popular songs (https://www.billboard.com/charts/hot-100) then we'll just pick another song from that list (Path A). If the song is not among the most popular songs of the moment, then we'll analyze the audio features of the song and compare with our database. Based on this we'll find which songs are most "similar" to the one provided and pick one of those at random (Path B).

## Dataset

I scraped "The Hot 100 Chart" by Billboard (https://www.billboard.com/charts/hot-100) for Path A and used an Spotify API (Spotipy) to create a database of songs that I divided into 30 different clusters based on their audio features for Path B. My database includes more than 27.000 songs.


## Organization

I used the Trello template to organize my work and keep track of all remaining tasks.

My repository consists of:

- Folder: Music-Recommendations
    - README.md
    - .gitignore 
    - Folder: data
        - top100songs.csv (a list of the Hot 100 Billboard chart. Can be updated calling update_top100() from get_top_100.py)
        - song_database.csv (starting database gathered from Spotify playlists. NOT DIVIDED INTO CLUSTERS)
        - clustered_database.csv (song_database.csv but with an added column that identifies the cluster each song belongs to)
        - scaler.pickle (trained model for clustering)
        
    - Folder: code
        - get_top_100.ipynb (code for scraping and storing data from the Hot 100 Billboard chart. Includes a function that updates the database to have the latest version of the chart)
        - get_top_100.py (same as get_top_100.ipynb but ready to be called) 
        - Creating_database.ipynb (code that uses Spotipy API to gather and store songs from several Spotify playlists)
        - Creating_Clusters.ipynb (code that takes song_database.csv and divides the songs into clusters by analyzing their audio features)
        - Music_recommendations.ipynb (code that defines the Recommendation() function. It asks for a song name and provides a song recommendation following Path A or B, depending on the input)
        - Music.py (same as Music_recommendations.ipynb but ready to be run. Just call it on Terminal)
        
## Links

[Repository](https://github.com/IgnacioRus/Music-Recommendations)  
[Trello](https://trello.com/b/WUy2UQtZ/music-recommendations-project)  
