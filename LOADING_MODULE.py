#!/usr/bin/env python
# coding: utf-8


def loadUserPreferenceData():
    users = {}
    try:
        w=open('Book-Ratings.csv','r', encoding = 'ISO-8859-1')
        lines=w.readlines()[1:]
        
        for line in lines:
            data = line.split(';')[0:3]
            UserID = int(data[0].strip().replace('"',''))
            ISBN = data[1].strip().replace('"','')
            BookRating = int(data[2].strip().replace('"',''))
            
            if UserID in users:           
                users[UserID][ISBN]=BookRating
            else:
                users[UserID]={ISBN: BookRating}                      
    except IOError as e:
        print(f'file error {e}')
    return users
user_preferences = loadUserPreferenceData()
user_preferences



