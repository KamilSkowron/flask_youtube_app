from flask import jsonify
from googleapiclient.discovery import build
from datetime import datetime

import os

def get_most_popular_videos(region_code="", category_ID=0):
    api_key = os.environ.get('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    videos = []
    creators = []

    most_views_request = youtube.videos().list(
        part='statistics, snippet',
        maxResults=50,
        chart='mostPopular',
        videoCategoryId = category_ID,
        regionCode = region_code
    )
    most_views_response = most_views_request.execute()
    
    for video in most_views_response['items']:
        vid_views = video['statistics']['viewCount']
        vid_id = video['id']
        yt_link = f'https://youtu.be/{vid_id}'

        current_datetime = datetime.utcnow()
        pub_date = video['snippet']['publishedAt']
        pub_date = datetime.strptime(pub_date, '%Y-%m-%dT%H:%M:%SZ')
        
        days_diff = abs((current_datetime - pub_date).days)

        #print(video['snippet']['channelId'])

        creator_profile = youtube.channels().list(
            part='snippet',
            id=video['snippet']['channelId']
        )

        creator_profile_response = creator_profile.execute()

        videos.append(
            {
                'title' : video['snippet']['title'],
                'creator' : video['snippet']['channelTitle'],
                'views' : int(vid_views),
                'url' : yt_link,
                'thumbnails' : video['snippet']['thumbnails']['high']['url'],
                'publishedDate' : days_diff,
                'description' : video['snippet']['description'][:100],
                'profile_pic' : creator_profile_response['items'][0]['snippet']['thumbnails']['default']['url']
            }
        )

        videos.sort(key= lambda vid: vid['views'], reverse=True) # url, views

        #creators.append(video['']

    return videos
    #return most_views_response['items']