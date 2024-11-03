from yt_dlp.extractor.common import InfoExtractor

class FullTabooIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?fulltaboo\.tv/(?P<id>[^/?#&]+)'
    _TESTS = []

    def _real_extract(self, url):
        video_id = self._match_id(url)

        webpage = self._download_webpage(url, video_id)

        title = self._og_search_title(webpage)
        description = self._og_search_description(webpage)
        thumbnail = self._og_search_property('image', webpage)

        video_url = self._html_search_regex(r'"embedURL" content="(?P<videoURL>[a-zA-Z0-9:/._\-]*)"', webpage, 'videoURL')

        return {
            '_type': 'url_transparent',
            'url': video_url,
            'id': video_id,
            'title': title,
            'description': description,
            'thumbnail': thumbnail,
        }
