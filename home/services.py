import google.generativeai as genai
from django.conf import settings
import json

genai.configure(api_key=settings.API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text, job_description):

    prompt = f"""
    Analyze this resume against the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Return ONLY valid JSON:

    {{
        "match_score": 0,
        "ats_score": 0,
        "strengths": [],
        "missing_skills": [],
        "improvements": [],
        "interview_questions": [],
        "summary": ""
    }}
    """

    response = model.generate_content(prompt)

    try:
        return json.loads(response.text)
    except:
        return {
            "match_score": 0,
            "ats_score": 0,
            "strengths": [],
            "missing_skills": [],
            "improvements": [],
            "interview_questions": [],
            "summary": "Error processing analysis"
        }