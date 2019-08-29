import requests as rq
from video_scrap import ManagerContentYT, VideoYT, YOUTUBE_URL, YOUTUBE_SEARCH_URL

# Declarations

# Methods & Functions
def getMetadataOnline(search):
    query = rq.utils.requote_uri(search)
    url = YOUTUBE_SEARCH_URL + query
    response = rq.api.get(url)
    managerContentYT = ManagerContentYT(response.content)
    managerContentYT.get_manager_content_data()    
    return managerContentYT
    
def getMetadataOffline():
    with open(r"data\yt.html", "r", encoding="utf8") as f:
        managerContentYT = ManagerContentYT(soup=f.read())
        managerContentYT.get_manager_content_data()
    return managerContentYT
        # print([video.soup for video in managerContentYT.get_videos_YT_list()])
        # print(managerContentYT.get_videos_YT_list()[0].soup)

def writeUrlVideosInFile(managerContentYT):
    with open(r"data\url_list.list", "w+", encoding="utf8") as f:
        for videos in managerContentYT.soup_videos_list:
            f.write(videos.get_url_video() + "\n")
        f.close()

def main():
    managerContentYT = getMetadataOnline("mala mujer")
    # managerContentYT = getMetadataOffline()
    writeUrlVideosInFile(managerContentYT)
    
if __name__ == "__main__":
    main()    