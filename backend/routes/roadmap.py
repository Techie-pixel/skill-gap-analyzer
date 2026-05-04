from fastapi import APIRouter, Query

from models.schemas import (
    AIRoadmapResponse,
    AIYoutubeVideo,
    LearningRoadmapRequest,
    SkillGapDetectionRequest,
)
from services.ai_service import generate_ai_roadmap
from services.skill_service import detect_skill_gaps

router = APIRouter()


@router.get("/roadmap", response_model=AIRoadmapResponse)
def get_roadmap(
    target_role: str = Query(..., description="Target job role (e.g., 'Backend Developer')"),
    missing_skills: list[str] = Query(..., description="Skills the student is missing"),
):
    """Generate an AI-powered learning roadmap for missing skills using Nebius API."""
    result = generate_ai_roadmap(target_role, missing_skills)
    return result


def _extract_video_id(url: str) -> str:
    """Extract YouTube video ID from a URL, or return the URL as-is."""
    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return url


def _add_fallback_videos(item: dict):
    """Populate youtube_videos with real, hardcoded video IDs as fallback."""
    skill_lower = item.get("skill", "").lower()
    if "html" in skill_lower:
        item["youtube_videos"] = [
            {"title": "HTML Tutorial for Beginners", "video_id": "qz0aGYrrlhU", "thumbnail": ""},
            {"title": "HTML Full Course", "video_id": "kUMe1ly46wI", "thumbnail": ""}
        ]
    elif "css" in skill_lower and "tailwind" not in skill_lower:
        item["youtube_videos"] = [
            {"title": "CSS Tutorial - Zero to Hero", "video_id": "1Rs2ND1ryYc", "thumbnail": ""},
            {"title": "CSS Flexbox in 100 Seconds", "video_id": "u044iM9xsWU", "thumbnail": ""}
        ]
    elif "tailwind" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Tailwind CSS Full Course", "video_id": "lCxcTsOHrjo", "thumbnail": ""},
            {"title": "Tailwind in 100 Seconds", "video_id": "mr15Xzb1Ook", "thumbnail": ""}
        ]
    elif "react" in skill_lower:
        item["youtube_videos"] = [
            {"title": "React for Beginners", "video_id": "SqcY0GlETPk", "thumbnail": ""},
            {"title": "React Course - Beginner's Tutorial", "video_id": "bMknfKXIFA8", "thumbnail": ""}
        ]
    elif "angular" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Angular Tutorial for Beginners", "video_id": "3qBXWUpoPHo", "thumbnail": ""},
            {"title": "Angular Crash Course", "video_id": "T_Fe4IaG0KU", "thumbnail": ""}
        ]
    elif "vue" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Vue.js Course for Beginners", "video_id": "FXpIoQ_rT_c", "thumbnail": ""},
            {"title": "Vue 3 Tutorial", "video_id": "YrxBCBibVo0", "thumbnail": ""}
        ]
    elif "next" in skill_lower and "js" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Next.js Tutorial for Beginners", "video_id": "ZVnjOPwW4ZA", "thumbnail": ""},
            {"title": "Next.js Full Course", "video_id": "wm5gMKuwSYk", "thumbnail": ""}
        ]
    elif "javascript" in skill_lower or "js" in skill_lower:
        item["youtube_videos"] = [
            {"title": "JavaScript Full Course for Beginners", "video_id": "PkZNo7MFNFg", "thumbnail": ""},
            {"title": "JavaScript Tutorial", "video_id": "W6NZfCJ1udo", "thumbnail": ""}
        ]
    elif "typescript" in skill_lower:
        item["youtube_videos"] = [
            {"title": "TypeScript Full Course for Beginners", "video_id": "30LWjhZzg50", "thumbnail": ""},
            {"title": "Advanced TypeScript - Matt Pocock", "video_id": "F7O4gA0GXqI", "thumbnail": ""}
        ]
    elif "node" in skill_lower or "express" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Node.js Tutorial for Beginners", "video_id": "TlB_eWDSMt4", "thumbnail": ""},
            {"title": "Express.js Crash Course", "video_id": "L72fhGm1tfE", "thumbnail": ""}
        ]
    elif "python" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Python for Beginners", "video_id": "kqtD5dpn9C8", "thumbnail": ""},
            {"title": "Python Full Course", "video_id": "_uQrJ0TkZlc", "thumbnail": ""}
        ]
    elif "django" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Django for Beginners - Full Tutorial", "video_id": "rHux0gMZ3Eg", "thumbnail": ""},
            {"title": "Django REST Framework Course", "video_id": "c708Nf0cHrs", "thumbnail": ""}
        ]
    elif "flask" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Flask Course - Python Web Development", "video_id": "Qr4QMBUPxWo", "thumbnail": ""},
            {"title": "REST APIs with Flask", "video_id": "GMppyAPbLYk", "thumbnail": ""}
        ]
    elif "java" in skill_lower and "script" not in skill_lower:
        item["youtube_videos"] = [
            {"title": "Java Tutorial for Beginners", "video_id": "eIrMbAQSU34", "thumbnail": ""},
            {"title": "Java Full Course", "video_id": "xk4_1vDrzzo", "thumbnail": ""}
        ]
    elif "sql" in skill_lower or "database" in skill_lower:
        item["youtube_videos"] = [
            {"title": "SQL Tutorial - Full Database Course", "video_id": "HXV3zeQKqGY", "thumbnail": ""},
            {"title": "MySQL Full Course", "video_id": "7S_tz1z_5bA", "thumbnail": ""}
        ]
    elif "git" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Git and GitHub for Beginners", "video_id": "RGOj5yH7evk", "thumbnail": ""},
            {"title": "Git Tutorial for Beginners", "video_id": "8JJ101D3knE", "thumbnail": ""}
        ]
    elif "docker" in skill_lower or "container" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Docker Crash Course for Absolute Beginners", "video_id": "pg19Z8LL06w", "thumbnail": ""},
            {"title": "Docker Tutorial for Beginners", "video_id": "pTFZFxd4hOI", "thumbnail": ""}
        ]
    elif "kubernetes" in skill_lower or "k8s" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Kubernetes Tutorial for Beginners", "video_id": "X48VuDVv0do", "thumbnail": ""},
            {"title": "Kubernetes Course - Full Beginners Tutorial", "video_id": "d6WC5n9G_sM", "thumbnail": ""}
        ]
    elif "aws" in skill_lower or "cloud" in skill_lower:
        item["youtube_videos"] = [
            {"title": "AWS Certified Cloud Practitioner", "video_id": "SOTamWNgDKc", "thumbnail": ""},
            {"title": "Cloud Computing Full Course", "video_id": "2LaAJq1lB1Q", "thumbnail": ""}
        ]
    elif "machine learning" in skill_lower or "ml" in skill_lower:
        item["youtube_videos"] = [
            {"title": "Machine Learning Course for Beginners", "video_id": "NWONeJKn6kc", "thumbnail": ""},
            {"title": "Machine Learning with Python", "video_id": "7eh4d6sabA0", "thumbnail": ""}
        ]
    elif "api" in skill_lower or "rest" in skill_lower:
        item["youtube_videos"] = [
            {"title": "APIs for Beginners", "video_id": "GZvSYJDk-us", "thumbnail": ""},
            {"title": "RESTful APIs in 100 Seconds", "video_id": "-MTSQjw5DrM", "thumbnail": ""}
        ]
    elif "system design" in skill_lower:
        item["youtube_videos"] = [
            {"title": "System Design for Beginners", "video_id": "MbjObHmDbZo", "thumbnail": ""},
            {"title": "Scalability & System Design", "video_id": "uw-gcK9bjkk", "thumbnail": ""}
        ]
    else:
        # Generic programming tutorials with real YouTube video IDs
        item["youtube_videos"] = [
            {"title": "How to Learn to Code - 8 Hard Truths", "video_id": "NtfbWkxJTHw", "thumbnail": ""},
            {"title": "Programming Full Course - Beginner to Advanced", "video_id": "zOjov-2OZ0E", "thumbnail": ""},
            {"title": "Computer Science Concepts in 12 Minutes", "video_id": "SzJ46YA_RaA", "thumbnail": ""}
        ]
    item["is_sample_videos"] = True


def _attach_youtube_videos(result: dict) -> dict:
    """Attach real YouTube videos from YouTube Data API to each roadmap skill."""
    from services.youtube_service import search_youtube_videos

    roadmap = result.get("roadmap", [])
    if not roadmap:
        return result

    for item in roadmap:
        skill_name = item.get("skill", "")
        try:
            videos = search_youtube_videos(skill_name, max_results=2)
            yt_videos = []
            for v in videos:
                if v.get("video_id"):
                    yt_videos.append(AIYoutubeVideo(
                        title=v["title"],
                        video_id=v["video_id"],
                        thumbnail=v.get("thumbnail"),
                    ))
            if yt_videos:
                item["youtube_videos"] = [v.model_dump() for v in yt_videos]
                item["is_sample_videos"] = False
            else:
                _add_fallback_videos(item)
        except Exception:
            _add_fallback_videos(item)

    return result


@router.post("/learning-roadmap", response_model=AIRoadmapResponse)
def post_learning_roadmap(request: LearningRoadmapRequest):
    """Generate an AI-powered learning roadmap.

    Accepts the frontend format: {skills: [{name, level}], target_role}.
    First detects missing skills, then generates a roadmap for them.
    """
    gap_request = SkillGapDetectionRequest(
        student_skills=[s.name for s in request.skills],
        target_role=request.target_role,
    )
    gap_result = detect_skill_gaps(gap_request)

    if not gap_result.missing_skills:
        return AIRoadmapResponse(roadmap=[])

    result = generate_ai_roadmap(request.target_role, gap_result.missing_skills)
    result = _attach_youtube_videos(result)
    return result
