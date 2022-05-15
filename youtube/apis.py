from googleapiclient.discovery import build
from datetime import datetime
import os

def get_most_popular_videos():
    api_key = os.environ.get('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    videos = []
    most_views_request = youtube.videos().list(
        part='statistics, snippet',
        maxResults=50,
        chart='mostPopular',
        #videoCategoryId = 20,
        regionCode = "PL"
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
                'publishedDate' : days_diff
            }
        )


        videos.sort(key= lambda vid: vid['views'], reverse=True) # url, views
    return videos
    #return most_views_response['items']