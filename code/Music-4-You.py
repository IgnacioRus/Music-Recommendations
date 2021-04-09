import re
import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import *
from get_top_100 import update_top100

def Recommendation():

    #--------------------------------Initializing Variables--------------------------------#
    
    top100_len = 99
    another = True
    update_top100()
    top100 = pd.read_csv('../data/top100songs.csv',skipinitialspace=True)
    
    
    looking_for_the_right_song = True
    filename = '../data/scaler.pickle'
    

    #--------------------------------Asking for input--------------------------------#
    
    songname = input('Please, introduce the name of a song you like: ')
    # artistname = input('Thanks! Now introduce the name of the artist: ')
    
    
    #--------------------------------Loop for 'Hot Songs'--------------------------------#
    
    songnames = [song.lower() for song in list(top100['Song'].unique())]
    
    if songname.lower() in songnames:
        
        top100_songs = list(top100['Song'])
        top100_artists = list(top100['Artist'])
        
        while another:
            
            rand_num = random.randint(0,top100_len)
            
            print('\n')
            print('You can listen to "'+top100_songs[rand_num]+'" by '+top100_artists[rand_num])
            
            top100_songs.remove(top100_songs[rand_num])
            top100_artists.remove(top100_artists[rand_num])
            top100_len -= 1
            
            if top100_len==94:
                
                print('\n')
                print('You already got lots of recommendations. Enough for today!')
                return
            
            print('\n')
            again = input('Do you want another recommendation? (Y/N):')
            
            if 'n' in again.lower():
                
                another = False
        
        
    #--------------------------------Checking if it's a 'Hot Song'--------------------------------#    
    else:
        
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= Client_ID,
                                                           client_secret= Client_Secret_ID))
        
        while looking_for_the_right_song:
            
            result = sp.search(q="track:"+songname,limit=20)
            
            num_of_matches = len(result['tracks']['items'])
            
            print('\n')
            if num_of_matches==20: 
                print('There are more than 20 songs that match that information')
            else:
                print('There are '+str(num_of_matches)+' songs that match that information')

            for song in result['tracks']['items']:
                
                song_artists_check = ','.join([artists['name'] for artists in song['artists']])
                
                print('\n')
                check = input('Do you mean '+song['name']+' by ' + song_artists_check+'? (Y/N):')
                
                if 'y' in check.lower():
                    
                    looking_for_the_right_song = False
                    the_song_uri = song['uri']
                    break        
            if looking_for_the_right_song == True: 
                
                print('\n')
                print('Unfortunately we cannot find the song you meant. Try again with a different song')
                print('\nGo listen to AURORA ;)')
                return
        
        with open(filename, "rb") as f: 
            kmeans =  pickle.load(f)
        
        audio_features = sp.audio_features(the_song_uri)
        table_features = pd.DataFrame(audio_features).drop(columns=['key','mode','type','id','uri','track_href',
                                                                    'analysis_url','duration_ms','time_signature'])
        
        features_scaled = StandardScaler().fit_transform(table_features)
        
        cluster = kmeans.predict(features_scaled)[0]
        
        database = pd.read_csv('../data/clustered_database.csv')
        
        while another:
            
            sample = database.loc[database['cluster']==cluster].sample()
            
            sample_name = list(sample['song'])[0]
            sample_artist = list(sample['artist'])[0]
            
            print('\n')
            print('You can listen to "'+sample_name+'" by '+sample_artist)
            print('\n')
            
            again = input('Do you want another recommendation? (Y/N):')
            
            if 'n' in again.lower():
                
                another = False
                
                print('\nGo listen to AURORA ;)')
                return
            
    print('\nGo listen to AURORA ;)')
Recommendation()

