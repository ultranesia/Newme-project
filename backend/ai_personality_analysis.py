"""
AI-Powered Personality Analysis Enhancement
Uses OpenAI GPT to generate personalized, deep insights
"""
import os
from openai import OpenAI
import json

# Initialize OpenAI with Emergent LLM key
EMERGENT_LLM_KEY = os.environ.get("EMERGENT_LLM_KEY", "")
client = None

if EMERGENT_LLM_KEY:
    client = OpenAI(
        api_key=EMERGENT_LLM_KEY,
        base_url="https://api.studio.emergentagent.com/v1"
    )


async def generate_ai_personality_insights(
    answers_data: dict,
    basic_analysis: dict,
    test_type: str = "free"
) -> dict:
    """
    Generate deep, personalized AI analysis based on test results.
    
    Args:
        answers_data: Dict with question texts and answers
        basic_analysis: Basic scoring analysis (elements, personality type, etc)
        test_type: "free" or "paid"
    
    Returns:
        Dict with AI-generated insights
    """
    if not client or not EMERGENT_LLM_KEY:
        return {
            "aiAnalysis": None,
            "aiGenerated": False,
            "error": "AI analysis not available"
        }
    
    try:
        # Build comprehensive context for AI
        context = f"""
Kamu adalah seorang psikolog profesional dan career counselor yang ahli dalam analisis kepribadian NEWME.

HASIL ANALISIS DASAR:
- Tipe Kepribadian: {basic_analysis.get('personalityType', 'Unknown')}
- Elemen Dominan: {basic_analysis.get('dominantElement', 'Unknown')}
- Interest Dominan: {basic_analysis.get('dominantInterest', 'Unknown')}
- Talent Dominan: {basic_analysis.get('dominantTalent', 'Unknown')}

SKOR DETAIL:
- Element Scores: {json.dumps(basic_analysis.get('elementScores', {}), ensure_ascii=False)}
- Interest Scores: {json.dumps(basic_analysis.get('interestScores', {}), ensure_ascii=False)}
- Talent Scores: {json.dumps(basic_analysis.get('talentScores', {}), ensure_ascii=False)}

JAWABAN USER (sample):
{json.dumps(list(answers_data.items())[:5], ensure_ascii=False, indent=2)}

TEST TYPE: {"PREMIUM (25 soal)" if test_type == "paid" else "GRATIS (5 soal)"}

TUGAS KAMU:
Berikan analisis kepribadian yang mendalam, personal, dan actionable dalam format JSON dengan struktur berikut:

{{
  "ringkasanKepribadian": "Paragraf 2-3 kalimat yang menggambarkan kepribadian unik user secara holistik",
  "kekuatanUtama": [
    "3-5 kekuatan spesifik dengan penjelasan singkat"
  ],
  "areasPengembanganDiri": [
    "3-5 area yang bisa dikembangkan dengan saran konkret"
  ],
  "rekomendasiKarirSpesifik": [
    {{
      "bidang": "Nama bidang karir",
      "alasan": "Mengapa cocok dengan kepribadian user",
      "roleContoh": ["Contoh posisi 1", "Contoh posisi 2"]
    }},
    // 3-5 rekomendasi karir
  ],
  "strategiPengembanganDiri": [
    {{
      "area": "Area pengembangan",
      "langkahKonkret": ["Langkah 1", "Langkah 2", "Langkah 3"]
    }},
    // 2-3 strategi
  ],
  "tipsPraktis": [
    "5-7 tips praktis sehari-hari yang sesuai dengan kepribadian"
  ],
  "motivationalMessage": "Pesan motivasi personal yang inspiring (2-3 kalimat)"
}}

PENTING:
- Gunakan bahasa Indonesia yang natural dan personal
- Hindari klise atau template umum
- Berikan insights yang spesifik berdasarkan kombinasi unik dari scores
- Fokus pada actionable advice
- Tone: supportive, insightful, empowering
"""

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Kamu adalah psikolog profesional dan career counselor yang memberikan analisis kepribadian mendalam dan personal."
                },
                {
                    "role": "user",
                    "content": context
                }
            ],
            temperature=0.7,
            max_tokens=2000,
            response_format={"type": "json_object"}
        )
        
        # Parse AI response
        ai_content = response.choices[0].message.content
        ai_insights = json.loads(ai_content)
        
        return {
            "aiAnalysis": ai_insights,
            "aiGenerated": True,
            "model": "gpt-4o-mini",
            "timestamp": response.created
        }
        
    except Exception as e:
        print(f"Error generating AI insights: {e}")
        return {
            "aiAnalysis": None,
            "aiGenerated": False,
            "error": str(e)
        }


async def enhance_analysis_with_ai(
    answers: dict,
    questions_data: list,
    basic_analysis: dict,
    test_type: str
) -> dict:
    """
    Enhance basic analysis with AI-generated insights.
    
    Returns complete analysis with both basic and AI insights.
    """
    # Build answers data with context
    answers_data = {}
    for q_id, answer_idx in answers.items():
        question = next((q for q in questions_data if str(q.get('_id')) == str(q_id)), None)
        if question:
            options = question.get('options', [])
            if isinstance(answer_idx, int) and 0 <= answer_idx < len(options):
                answers_data[q_id] = {
                    "question": question.get('text', ''),
                    "category": question.get('category', ''),
                    "answer": options[answer_idx].get('text', ''),
                    "answerIndex": answer_idx
                }
    
    # Generate AI insights
    ai_result = await generate_ai_personality_insights(
        answers_data=answers_data,
        basic_analysis=basic_analysis,
        test_type=test_type
    )
    
    # Merge basic and AI analysis
    enhanced_analysis = {
        **basic_analysis,
        "aiInsights": ai_result.get("aiAnalysis"),
        "aiGenerated": ai_result.get("aiGenerated", False),
        "analysisVersion": "2.0-ai-enhanced"
    }
    
    return enhanced_analysis
