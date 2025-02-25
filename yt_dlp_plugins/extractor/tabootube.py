from yt_dlp.extractor.common import InfoExtractor

class TabooTubeIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?tabootube\.(to|xxx)/?(embed/)?(?P<id>[^?&/$]+)/?$'
    _TESTS = []

    def _real_extract(self, url):
        video_id = self._match_id(url)

        webpage = self._download_webpage(url, video_id)

        title = self._og_search_title(webpage)
        description = self._og_search_description(webpage)
        thumbnail = self._og_search_thumbnail(webpage)

        # grab the first download link
        video_url = self._search_regex(r'<span class="download-link" data-href="(?P<videoURL>[^"]+)"', webpage, 'videoURL')

        # get the real id from the embed link
        embed_video_url = self._twitter_search_player(webpage)
        video_id = self._match_id(embed_video_url)

        return {
            #'_type': 'url',
            'url': video_url,
            'id': video_id,
            'title': title,
            'description': description,
        }