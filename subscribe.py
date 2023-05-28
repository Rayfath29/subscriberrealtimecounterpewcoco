import requests

def get_subscriber_count(channel_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    subscriber_count = int(data["items"][0]["statistics"]["subscriberCount"])
    return subscriber_count

def check_subscriber_counts(api_key):
    channels = {
        "T-Series": "UCq-Fj5jknLsUf-MWSy4_brA",
        "Mr. Beast": "UCX6OQ3DkcsbYNE6H8uQQuVA",
        "PewDiePie": "UC-lHJZR3Gqxm24_Vd_AJ5Yw",
        "Cocomelon": "UCbCmjCuTUZos6Inko4u57UQ"
    }
    for channel_name, channel_id in channels.items():
        subscriber_count = get_subscriber_count(channel_id, api_key)
        print(f"{channel_name}: {subscriber_count} subscribers")

# Replace 'YOUR_API_KEY' with your actual YouTube Data API key
api_key = 'AIzaSyDAc37sgeWWx8h4Z2I5NAks-TSbDLBs9Vg'
check_subscriber_counts(api_key)
