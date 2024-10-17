from yt_dlp.extractor.common import InfoExtractor

class TabooTubeIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?tabootube\.xxx/(?!embed)(?P<id>[^/?#&]+)'
    _TESTS = []

    def _real_extract(self, url):
        video_id = self._match_id(url)

        webpage = self._download_webpage(url, video_id)

        title = self._og_search_title(webpage)
        description = self._og_search_description(webpage)
        thumbnail = self._og_search_thumbnail(webpage)

        # be lazy and send off the embed url to another extractor
        video_url = self._twitter_search_player(webpage)
        #video_url = self._html_search_meta('twitter:player', webpage)
        #video_url = self._search_regex(r'name=\"twitter:player\" content="(?P<videoURL>[^"]+)"', webpage, 'videoURL')

        return {
            '_type': 'url',
            'url': video_url,
            'id': video_id,
        }