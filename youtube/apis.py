from flask import jsonify
from googleapiclient.discovery import build
from datetime import datetime
from youtube.functions import convert_views_to_readable, TimeVideo
import os

def get_most_popular_videos(region_code="", category_ID=0):
    api_key = os.environ.get('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    videos = []
    
    round_num = 0
    nextPageToken = None

    while True:
        most_views_request = youtube.videos().list(
            part='statistics, snippet, contentDetails',
            maxResults=50,
            chart='mostPopular',
            videoCategoryId = category_ID,
            regionCode = region_code,
            pageToken=nextPageToken
        )
        most_views_response = most_views_request.execute()

        creators_list = []

        for i in most_views_response['items']:
            creators_list.append(i['snippet']['channelId'])

        creator_profile = youtube.channels().list(
            part='snippet',
            id=','.join(creators_list),
            maxResults=50,
            pageToken=nextPageToken
        )

        creator_profile_response = creator_profile.execute() # returns list with no duplicates and in random order (correct it in some day)

        for i, video in enumerate(most_views_response['items']):
            vid_views = video['statistics']['viewCount']
            yt_link = f"https://youtu.be/{video['id']}"

            duration_video = video['contentDetails']['duration'][2:]

            V = TimeVideo(duration_video)
            
            

            current_datetime = datetime.utcnow()
            pub_date = datetime.strptime(video['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            
            days_diff = abs((current_datetime - pub_date).days)

            videos.append(
                {
                    'title' : video['snippet']['title'],
                    'creator' : video['snippet']['channelTitle'],
                    'views' : int(vid_views),
                    'url' : yt_link,
                    'thumbnails' : video['snippet']['thumbnails']['high']['url'],
                    'publishedDate' : days_diff,
                    'description' : video['snippet']['description'][:100],
                    'views_read' : convert_views_to_readable(vid_views),
                    'creatorID' : video['snippet']['channelId'],
                    'profile_pic' : creator_profile_response['items'][i]['snippet']['thumbnails']['default']['url'] if i < len(creator_profile_response['items']) else 0,
                    'duration_video' : V.repr()
                }
            )

        round_num += 1
        nextPageToken = most_views_response.get('nextPageToken')

        if (not nextPageToken) or round_num == 20:
            break

    #videos.sort(key= lambda vid: vid['views'], reverse=True) 
    return videos
