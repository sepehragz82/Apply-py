from sqlalchemy.orm import Session

from src import crud, models
from src.core.config import settings
from src.database import base  # keep

professors = [
    {
        "professor_f_name": "Sulaymon",
        "professor_m_name": "",
        "professor_l_name": "Eshkabilov",
        "prof_gender": False,
        "prof_code_in_uni": "",
        "university_id": "",
        "department_id": "",
        "email": "sulaymon.eshkabilov@ndsu.edu",
        "linkedin": "https://www.linkedin.com/in/sulaymon-eshkabilov-3778745/",
        "google_scholar": "https://scholar.google.com/citations?hl=en&user=edIEM5oAAAAJ",
        "h_index": "13",
        "profile_uni_site": "https://www.ndsu.edu/aben/faculty_staff/dr_sulaymon_eshkabilov_assistant_professor/",
        "education_description": "",
        "extra_description": "",
        "academic_rank_id": "",
    },
    {
        "professor_f_name": "Yanning ",
        "professor_m_name": "",
        "professor_l_name": "Shen",
        "prof_gender": False,
        "prof_code_in_uni": "",
        "university_id": "University of California, Irvine",
        "department_id": "Electrical",
        "email": "yannings@uci.edu",
        "linkedin": "https://www.linkedin.com/in/yanning-shen-a4b27061/",
        "google_scholar": "https://scholar.google.com/citations?hl=en&user=MfzntAIAAAAJ",
        "h_index": "23",
        "profile_uni_site": "https://engineering.uci.edu/users/yanning-shen",
        "education_description": "",
        "extra_description": "",
        "academic_rank_id": "Assistant Professor",
    },
]


def init_db(db: Session):
    for item in professors:
        db_record = models.Professor(
            professor_f_name=item["professor_f_name"],
            professor_m_name=item["professor_m_name"],
            professor_l_name=item["professor_l_name"],
            prof_gender=item["prof_gender"],
            prof_code_in_uni=item["prof_code_in_uni"],
            university_id=item["university_id"],
            department_id=item["department_id"],
            email=item["email"],
            linkedin=item["linkedin"],
            google_scholar=item["google_scholar"],
            h_index=item["h_index"],
            profile_uni_site=item["profile_uni_site"],
            education_description=item["education_description"],
            extra_description=item["extra_description"],
            academic_rank_id=item["academic_rank_id"],
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
