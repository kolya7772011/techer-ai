from enum import Enum
from typing import Dict, List


class Subject(str, Enum):
    """Available subjects."""
    MATH = "Matematika"
    CS = "Informatika"
    PHYSICS = "Fizika"
    CHEMISTRY = "Kimyo"
    BIOLOGY = "Biologiya"
    ENGLISH = "Ingliz tili"
    UZBEK = "Ona tili"
    HISTORY = "Tarix"
    GEOGRAPHY = "Geografiya"


class LearningStyle(str, Enum):
    """Learning styles."""
    VISUAL = "Visual"
    AUDITORY = "Auditory"
    READING = "Reading"
    PRACTICE = "Practice"


class AchievementCode(str, Enum):
    """Achievement codes."""
    FIRST_LESSON = "first_lesson"
    XP_100 = "xp_100"
    XP_500 = "xp_500"
    XP_1000 = "xp_1000"
    STREAK_7 = "streak_7"
    STREAK_30 = "streak_30"
    TOP_STUDENT = "top_student"


TOPIC_MAP: Dict[str, List[str]] = {
    "Matematika": [
        "Raqamlar va amallar",
        "O'zgaruvchilar va tenglama",
        "Geometriya",
        "Trigonometriya",
        "Logaritmlar",
    ],
    "Informatika": [
        "Dasturlash asoslari",
        "O'zgaruvchilar",
        "Sikllar",
        "Funksiyalar",
        "Ma'lumotlar tuzilmasi",
    ],
    "Fizika": [
        "Mexanika",
        "Termodinamika",
        "Elektromagnetizm",
        "Optika",
        "Kvantum fizikasi",
    ],
    "Kimyo": [
        "Asosiy tushunchalar",
        "Davriy jadval",
        "Kimyoviy bog'lanishlar",
        "Reaktsiyalar",
        "Organik kimyo",
    ],
    "Biologiya": [
        "Hujayra",
        "Genetika",
        "Evolyutsiya",
        "Ekologiya",
        "Insan biologiyasi",
    ],
    "Ingliz tili": [
        "Grammatika",
        "Lug'at",
        "Gaplar",
        "Muloqot",
        "So'z birikmasi",
    ],
    "Ona tili": [
        "Grammatika",
        "Imlo",
        "Punktuatsiya",
        "Matn tahlili",
        "Ijod",
    ],
    "Tarix": [
        "Qadimgi davr",
        "O'rta asrlar",
        "Yangi tarix",
        "Buxoro davlati",
        "O'zbekiston tarixi",
    ],
    "Geografiya": [
        "Geografiya asoslari",
        "Kontinentlar",
        "Iqlim va ob-havo",
        "Aholisi",
        "Iqtisodiy geografiya",
    ],
}


ACHIEVEMENTS = {
    "first_lesson": {
        "name": "🎓 Birinchi dars",
        "description": "Birinchi darsni tugatdingiz",
        "xp": 10,
    },
    "xp_100": {
        "name": "⭐ 100 XP",
        "description": "100 XP yig'oldingiz",
        "xp": 0,
    },
    "xp_500": {
        "name": "✨ 500 XP",
        "description": "500 XP yig'oldingiz",
        "xp": 0,
    },
    "xp_1000": {
        "name": "🏆 1000 XP",
        "description": "1000 XP yig'oldingiz",
        "xp": 0,
    },
    "streak_7": {
        "name": "🔥 7 kunlik streyk",
        "description": "7 kunlik davamiylik",
        "xp": 50,
    },
    "streak_30": {
        "name": "🌟 30 kunlik streyk",
        "description": "30 kunlik davamiylik",
        "xp": 100,
    },
    "top_student": {
        "name": "👑 Top talaba",
        "description": "Liderlar ro'yxatida 1-o'rinda",
        "xp": 200,
    },
}
