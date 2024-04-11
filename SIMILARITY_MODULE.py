#!/usr/bin/env python
# coding: utf-8
from math import *

def users_similarity(user_preferences, user1, user2, method):
    try:        
        ISBNs_rated_by_both = set(user_preferences[user1].keys()).intersection(set(user_preferences[user2].keys()))
        if len(ISBNs_rated_by_both) == 0:
            similarity= 0            
        else:
            if method=='Jaccard':
                similarity = len(ISBNs_rated_by_both) / len(set(user_preferences[user1].keys()).union(set(user_preferences[user2].keys())))
                
            elif method=='Cosine':                
                numerator = sum([user_preferences[user1][ISBN] * user_preferences[user2][ISBN] for ISBN in ISBNs_rated_by_both])
                denominator = (sum([user_preferences[user1][ISBN]**2 for ISBN in ISBNs_rated_by_both]) * 
                              sum([user_preferences[user2][ISBN]**2 for ISBN in ISBNs_rated_by_both]))**0.5
                similarity = numerator / denominator
            elif method=='Pearson':
                mean1 = sum([user_preferences[user1][ISBN] for ISBN in ISBNs_rated_by_both]) / len(ISBNs_rated_by_both)
                mean2 = sum([user_preferences[user2][ISBN] for ISBN in ISBNs_rated_by_both]) / len(ISBNs_rated_by_both)
                numerator = sum([(user_preferences[user1][ISBN] - mean1) * (user_preferences[user2][ISBN] - mean2) for ISBN in ISBNs_rated_by_both])
                denominator = (sum([(user_preferences[user1][ISBN] - mean1)**2 for ISBN in ISBNs_rated_by_both]) * 
                              sum([(user_preferences[user2][ISBN] - mean2)**2 for ISBN in ISBNs_rated_by_both]))**0.5
                similarity = numerator / denominator
            
            elif method=='Euclidean':
                similarity = 1 / (1 + sum([(user_preferences[user1][ISBN] - user_preferences[user2][ISBN])**2 for ISBN in ISBNs_rated_by_both])**0.5)

            elif method=='Manhattan':
                similarity = sum([abs(user_preferences[user1][ISBN] - user_preferences[user2][ISBN]) for ISBN in ISBNs_rated_by_both])

            else:
                print("Enter correct method, please!!")          
        
        return similarity
                  
    except KeyError as e:
        print(f"KeyError: {e}")

        return None


    
##############################################################################################################################


def books_similarity(user_preferences, ISBN1, ISBN2, method):
    try:         
        users_rated_both = [user for user in user_preferences if ISBN1 in user_preferences[user] and ISBN2 in user_preferences[user]]
        
        if method=='Jaccard':
            users_rated_ISBN1 = [user for user in user_preferences if ISBN1 in user_preferences[user]]
            users_rated_ISBN2 = [user for user in user_preferences if ISBN2 in user_preferences[user]]
            similarity = len(users_rated_both) / len(set(users_rated_ISBN1) | set(users_rated_ISBN2))

        elif method=='Pearson':        
            sum1 = sum([user_preferences[user][ISBN1] for user in users_rated_both])
            sum2 = sum([user_preferences[user][ISBN2] for user in users_rated_both])
            sum1_squared = sum([pow(user_preferences[user][ISBN1], 2) for user in users_rated_both])
            sum2_squared = sum([pow(user_preferences[user][ISBN2], 2) for user in users_rated_both])
            product_sum = sum([user_preferences[user][ISBN1] * user_preferences[user][ISBN2] for user in users_rated_both])
            n = len(users_rated_both)
            numerator = product_sum - (sum1 * sum2 / n)
            denominator = pow((sum1_squared - pow(sum1, 2) / n) * (sum2_squared - pow(sum2, 2) / n), 0.5)
            if denominator == 0:
                similarity = 0
            else:
                similarity = numerator / denominator

        elif method=='Cosine':
            sum1_squared = sum([pow(user_preferences[user][ISBN1], 2) for user in users_rated_both])
            sum2_squared = sum([pow(user_preferences[user][ISBN2], 2) for user in users_rated_both])
            product_sum = sum([user_preferences[user][ISBN1] * user_preferences[user][ISBN2] for user in users_rated_both])
            numerator = product_sum
            denominator = pow(sum1_squared, 0.5) * pow(sum2_squared, 0.5)
            if denominator == 0:
                similarity = 0
            else:
                similarity = numerator / denominator
                                
                
        elif method=='Manhattan':
            similarity = sum([abs(user_preferences[user][ISBN1] - user_preferences[user][ISBN2]) for user in users_rated_both])
                
        elif method=='Euclidean':
            similarity = pow(sum([pow(user_preferences[user][ISBN1] - user_preferences[user][ISBN2], 2) for user in users_rated_both]), 0.5)
            
        else:
            print("Enter correct method, please!")

        return similarity
    
    except KeyError as e:
        print(f"KeyError: {e}")
        return None


##############################################################################################################################
    


def find_similar_users(user_preferences, target_userID, n):
    scores = {}
    target_user_preferences = user_preferences[target_userID]
    for other_user_id, other_user_preferences in user_preferences.items():
        if other_user_id != target_userID:
            score = 0
            for item_id in target_user_preferences:
                if item_id in other_user_preferences:
                    score += 1
            scores[other_user_id] = score

    similar_users = list(sorted(scores, key=scores.get, reverse=True))[:n]
    return similar_users



##############################################################################################################################



def find_similar_books(user_preferences, target_ISBN, n):
    target_users = [userID for userID, books in user_preferences.items() if target_ISBN in books]
    scores = {}
    for userID in target_users:
        for ISBN, rating in user_preferences[userID].items():
            if ISBN == target_ISBN:
                continue
            if ISBN not in scores:
                scores[ISBN] = 0
            scores[ISBN] += rating
    
    return [ISBN for ISBN, score in sorted(scores.items(), key=lambda x: x[1], reverse=True)[:n]]


# In[ ]:




