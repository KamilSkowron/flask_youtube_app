from flask import jsonify
from googleapiclient.discovery import build
from datetime import datetime
from youtube.functions import convert_views_to_readable
import os

def get_most_popular_videos(region_code="", category_ID=0):
    api_key = os.environ.get('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    videos = []
    creators_list = []

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
                'creatorID' : video['snippet']['channelId']
            }
        )
    for i in videos:
        creators_list.append(i['creatorID'])
    idd = ",".join(creators_list)

    creator_profile = youtube.channels().list(
    part='snippet',
    id = idd
    )

    creator_profile_response = creator_profile.execute()

    profile_pics = [x['snippet']['thumbnails']['default']['url'] for x in creator_profile_response['items']]
    print(len(profile_pics))
    for i, video in enumerate(videos[:24]):
        video['profile_pics'] = profile_pics[i]
        print(video)
        print("")

    videos.sort(key= lambda vid: vid['views'], reverse=True) # url, views
    return videos
