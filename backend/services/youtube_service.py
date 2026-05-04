"""YouTube Data API v3 integration for fetching real tutorial videos."""

import os
import logging
from urllib.parse import quote_plus

import requests
from dotenv import load_dotenv

load_dotenv(override=True)

logger = logging.getLogger(__name__)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_VIDEOS_URL = "https://www.googleapis.com/youtube/v3/videos"


def search_youtube_videos(query: str, max_results: int = 3) -> list[dict]:
    """Search YouTube for tutorial videos using YouTube Data API v3.

    Returns a list of dicts with keys: title, video_id, thumbnail, channel, views, duration, url
    Falls back to Invidious API if YouTube API key is not configured.
    """
    load_dotenv(override=True)
    api_key = os.getenv("YOUTUBE_API_KEY", "")

    if api_key:
        return _search_youtube_official(query, max_results, api_key)
    else:
        return _search_invidious(query, max_results)


def _search_youtube_official(query: str, max_results: int, api_key: str) -> list[dict]:
    """Search using the official YouTube Data API v3."""
    try:
        # Step 1: Search for videos
        search_params = {
            "part": "snippet",
            "q": f"{query} tutorial",
            "type": "video",
            "maxResults": max_results,
            "order": "relevance",
            "videoDuration": "medium",  # 4-20 minutes
            "key": api_key,
        }
        search_resp = requests.get(YOUTUBE_SEARCH_URL, params=search_params, timeout=10)
        search_resp.raise_for_status()
        search_data = search_resp.json()

        items = search_data.get("items", [])
        if not items:
            return _fallback_search_link(query)

        video_ids = [item["id"]["videoId"] for item in items]

        # Step 2: Get video details (duration, view count)
        details_params = {
            "part": "contentDetails,statistics",
            "id": ",".join(video_ids),
            "key": api_key,
        }
        details_resp = requests.get(YOUTUBE_VIDEOS_URL, params=details_params, timeout=10)
        details_resp.raise_for_status()
        details_data = details_resp.json()

        # Build details map
        details_map = {}
        for item in details_data.get("items", []):
            vid = item["id"]
            duration = _parse_duration(item.get("contentDetails", {}).get("duration", ""))
            views = _format_views(item.get("statistics", {}).get("viewCount", "0"))
            details_map[vid] = {"duration": duration, "views": views}

        # Combine results
        results = []
        for item in items:
            video_id = item["id"]["videoId"]
            snippet = item["snippet"]
            detail = details_map.get(video_id, {})
            results.append({
                "title": snippet["title"],
                "video_id": video_id,
                "thumbnail": f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg",
                "channel": snippet.get("channelTitle", ""),
                "views": detail.get("views", ""),
                "duration": detail.get("duration", ""),
                "url": f"https://www.youtube.com/watch?v={video_id}",
            })

        return results

    except Exception as e:
        logger.warning(f"YouTube API error: {e}. Falling back to Invidious.")
        return _search_invidious(query, max_results)


# Global tracker for failing instances to avoid repeatedly timing out
_FAILED_INSTANCES = set()

def _search_invidious(query: str, max_results: int) -> list[dict]:
    """Fallback: search using the free Invidious API (no key needed)."""
    instances = [
        "https://vid.puffyan.us",
        "https://invidious.snopyta.org",
        "https://y.com.sb",
        "https://invidious.nerdvpn.de",
        "https://inv.tux.pizza",
        "https://invidious.jing.rocks"
    ]

    for base_url in instances:
        if base_url in _FAILED_INSTANCES:
            continue
        try:
            url = f"{base_url}/api/v1/search"
            params = {"q": f"{query} tutorial", "type": "video", "sort_by": "relevance"}
            resp = requests.get(url, params=params, timeout=5) # increased timeout to 5s
            resp.raise_for_status()
            data = resp.json()

            results = []
            for v in data[:max_results]:
                if not isinstance(v, dict):
                    continue
                video_id = v.get("videoId", "")
                results.append({
                    "title": v.get("title", query),
                    "video_id": video_id,
                    "thumbnail": f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg",
                    "channel": v.get("author", ""),
                    "views": _format_views(str(v.get("viewCount", 0))),
                    "duration": _seconds_to_duration(v.get("lengthSeconds", 0)),
                    "url": f"https://www.youtube.com/watch?v={video_id}",
                })
            if results:
                return results
        except Exception as e:
            logger.warning(f"Invidious instance {base_url} failed: {e}")
            _FAILED_INSTANCES.add(base_url)
            continue

    # All instances failed — return a YouTube search link
    return _fallback_search_link(query)


def _fallback_search_link(query: str) -> list[dict]:
    """Ultimate fallback: return a YouTube search URL."""
    search_url = f"https://www.youtube.com/results?search_query={quote_plus(query + ' tutorial')}"
    return [{
        "title": f"Search: {query} tutorial",
        "video_id": "",
        "thumbnail": "",
        "channel": "YouTube",
        "views": "",
        "duration": "",
        "url": search_url,
    }]


def _parse_duration(iso_duration: str) -> str:
    """Convert ISO 8601 duration (PT1H2M3S) to readable format (1:02:03)."""
    if not iso_duration:
        return ""
    import re
    match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso_duration)
    if not match:
        return ""
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    return f"{minutes}:{seconds:02d}"


def _seconds_to_duration(seconds: int) -> str:
    """Convert seconds to readable duration."""
    if not seconds:
        return ""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def _format_views(count_str: str) -> str:
    """Format view count: 1234567 → '1.2M'."""
    try:
        count = int(count_str)
    except (ValueError, TypeError):
        return ""
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M"
    if count >= 1_000:
        return f"{count / 1_000:.0f}K"
    return str(count)
