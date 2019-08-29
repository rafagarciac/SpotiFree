import requests as rq
from bs4 import BeautifulSoup

YOUTUBE_URL =  "https://www.youtube.com"
YOUTUBE_SEARCH_URL = YOUTUBE_URL + "/results?search_query="


class VideoYT(object):
    
    def __init__(self, soup = None, *args, **kwargs):
        
        self._yt_url = YOUTUBE_URL
        self._yt_query_url = YOUTUBE_SEARCH_URL
        self.soup = soup
        self.title = self.get_title()
        self.artist = self.get_artist()
        self.description = self.get_description()
        self.views = self.get_views()
        self.publication_date = self.get_publication_date()
        self.url_video = self.get_url_video()
        self.url_thumbnail = self.get_url_thubmnail()
        
    def __str__(self):
        return "Title: {0}\nArtist: {1}\nDescription: {2}\nUrl humbnail: {3}\nUrl Video: {4}\nViews: {5}\nPublication Date: {6}\n".format(
                self.title, self.artist, self.description, self.url_thumbnail, self.url_video, str(self.views), self.publication_date)

    def get_title(self):
        return self.soup.find(attrs={'class': 'yt-uix-tile-link'})['title']

    def get_artist(self):
        artist_raw = self.soup.find(attrs={'class': 'yt-lockup-byline'}).find('a', recursive=False) 
        return artist_raw.text if artist_raw is not None else None

    def get_description(self):
        desc_raw = self.soup.find(attrs={'class': 'yt-lockup-description'})
        return desc_raw.text if desc_raw is not None else None

    def get_views(self):
        pre_views_raw = self.soup.find(attrs={'class': 'yt-lockup-meta-info'})
        views_raw = list(pre_views_raw.find_all('li', recursive=False)) if pre_views_raw is not None else []
        return views_raw[1].text if pre_views_raw is not None and len(views_raw) >= 2 else 0

    def get_publication_date(self):
        pre_publication_date_raw = self.soup.find(attrs={'class': 'yt-lockup-meta-info'})
        publication_date_raw = list(pre_publication_date_raw.find_all('li', recursive=False)) if pre_publication_date_raw is not None else [] 
        return publication_date_raw[0].text if pre_publication_date_raw is not None and len(publication_date_raw) >= 1 else None

    def get_url_video(self):
        return self._yt_url + self.soup.find(attrs={'class': 'yt-uix-tile-link'})['href']

    def get_url_thubmnail(self):
        return self.soup.find(attrs={'class': 'yt-thumb-simple'}).find('img', recursive=False)['src'] 


class ManagerContentYT(object):
    
    def __init__(self, soup = None, *args, **kwargs):
        
        self.soup = BeautifulSoup(soup, 'html.parser')
        self.soup_videos_list = self.get_videos_YT_list()

    def get_videos_list_raw(self):
        return list(self.soup.find(attrs={'class': 'item-section'}).find_all("li", recursive=False))

    def get_len_videos_list_raw(self):
        return len(self.get_videos_list_raw())

    def get_videos_YT_list(self):
        videos_list = []
        for raw_video in self.get_videos_list_raw():
            # Create a VideoYT and add to videos_list array         
            videoYT = VideoYT(raw_video)
            videos_list.append(videoYT) 
            
        return videos_list
    
    
    def get_len_videos_list(self):
        return len(self.soup_videos_list)

    def get_manager_content_data(self):
        for vid in self.get_videos_YT_list(): 
            print(vid.__str__())
        print(f"Video List Length: {self.get_len_videos_list()}")

""" Html Model for each VideoYT Object - Web Scrapping
    --------------------------------------------------
        <li>
            <div class="yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix" data-context-item-id="nsm4ReJaED0" data-visibility-tracking="CEgQ3DAYACITCO7jtb_jyd4CFVsx4Aod330KRyj0JEC9oOiS3oju5J4B">
                <div class="yt-lockup-dismissable yt-uix-tile">
                    <div class="yt-lockup-thumbnail contains-addto">
                        <a aria-hidden="true" class=" yt-uix-sessionlink spf-link " data-sessionlink="itct=CEgQ3DAYACITCO7jtb_jyd4CFVsx4Aod330KRyj0JFIKbWFsYSBtdWplcg" href="/watch?v=nsm4ReJaED0">
                            <div class="yt-thumb video-thumb">
                                <span class="yt-thumb-simple">
                                    <img alt="" data-ytimg="1" height="138" onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" src="https://i.ytimg.com/vi/nsm4ReJaED0/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&amp;rs=AOn4CLBUhC07Kp-NagWHCupDu75BQgsDTw" width="246"/>
                                    <span aria-hidden="true" class="video-time">3.40</span>
                                </span>
                            </div>
                        </a>
                        <span class="thumb-menu dark-overflow-action-menu video-actions">
                            <button aria-expanded="false" aria-haspopup="true" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" type="button">
                                <span class="yt-uix-button-arrow yt-sprite"></span>
                                <ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid">
                                    <li class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" data-video-ids="nsm4ReJaED0" onclick=";return false;" role="menuitem">
                                        <span class="addto-watch-queue-menu-text">Afspil næste</span>
                                    </li>
                                    <li class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" data-video-ids="nsm4ReJaED0" onclick=";return false;" role="menuitem">
                                        <span class="addto-watch-queue-menu-text">Afspil nu</span>
                                    </li>
                                </ul>
                            </button>
                        </span>
                        <button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="nsm4ReJaED0" onclick=";return false;" role="button" title="Se senere" type="button">
                            <span class="yt-uix-button-arrow yt-sprite"></span>
                        </button>
                        <button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" data-style="tv-queue" data-video-ids="nsm4ReJaED0" onclick=";return false;" title="Kø" type="button"></button>
                    </div>
                    <div class="yt-lockup-content">
                        <h3 class="yt-lockup-title ">
                            <a aria-describedby="description-id-447013" class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link " data-sessionlink="itct=CEgQ3DAYACITCO7jtb_jyd4CFVsx4Aod330KRyj0JFIKbWFsYSBtdWplcg" dir="ltr" href="/watch?v=nsm4ReJaED0" rel="spf-prefetch" title="C. Tangana - Mala Mujer (Video Oficial)">C. Tangana - Mala Mujer (Video Oficial)</a>
                            <span class="accessible-description" id="description-id-447013"> - Varighed: 3.40.</span>
                        </h3>
                        <div class="yt-lockup-byline ">
                            <a class="yt-uix-sessionlink spf-link " data-sessionlink="itct=CEgQ3DAYACITCO7jtb_jyd4CFVsx4Aod330KRyj0JA" href="/channel/UCOZyjrZSrTJJHU05DlF71Jw">C. Tangana</a>
                        </div>
                        <div class="yt-lockup-meta ">
                            <ul class="yt-lockup-meta-info">
                                <li>for 1 år siden</li>
                                <li>29.716.255 visninger</li>
                            </ul>
                        </div>
                        <div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">C. Tangana -<b>Mala Mujer</b> (Video Oficial) Escucha el álbum completo Ídolo:
                            <a class="yt-uix-redirect-link" dir="ltr" href="https://goo.gl/zzYbc5" rel="nofollow" target="_blank" title="https://goo.gl/zzYbc5">https://goo.gl/zzYbc5</a> Suscríbete al canal oficial de ...
                        </div>
                    </div>
                </div>
            </div>
        </li>
    """