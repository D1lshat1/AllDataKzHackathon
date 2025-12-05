from fastapi import FastAPI, HTTPException, Query
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic_models import University, AcademicProgram, InternationalCooperation



app = FastAPI(
    title="DataHub VUZ API",
    description="API для каталога университетов РК (MVP Хакатон)",
    version="1.0.0"
)



origins = [
    "*",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

fake_db = [
    University(
        id=1,
        name="Национальный Технический ВУЗ (НТВ)",
        mission="Лидер в области IT и инженерии. Основан в 1990 г.",
        achievements="Лучший ВУЗ РК по IT-направлениям (2024).",
        admission_requirements="ЕНТ от 115 баллов, Математика (Профильный).",
        tour_link="https://ntv.edu/3d-tour",

        programs=[
            AcademicProgram(id=101, program_name="Информатика", description="Разработка ПО.", score=4.5, duration=4),
            AcademicProgram(id=102, program_name="Кибербезопасность", description="Защита информации.", score=4.8,
                            duration=4),
        ],
        cooperation=InternationalCooperation(
            exchange_programs="Программы обмена с Кореей и Германией.",
            partner_universities="Seoul Tech, TU Berlin."
        )
    ),
    University(
        id=2,
        name="Гуманитарный Университет Астана (ГУА)",
        mission="Развитие социальных наук и искусства.",
        achievements="Награды за исследования в области истории и филологии.",
        admission_requirements="ЕНТ от 85 баллов, История (Профильный).",
        tour_link=None,

        programs=[
            AcademicProgram(id=201, program_name="История", description="Изучение культурного наследия.", score=3.9,
                            duration=4),
            AcademicProgram(id=202, program_name="Дизайн", description="Графический и веб-дизайн.", score=4.2,
                            duration=4),
        ],
        cooperation=InternationalCooperation(
            exchange_programs="Программы обмена с Францией и Италией.",
            partner_universities="Sorbonne Université, Università di Bologna."
        )
    )
]





@app.get("/api/universities/", response_model=List[University], tags=["Университеты"])
async def get_universities():
    return fake_db



@app.get("/api/universities/{uni_id}", response_model=University, tags=["Университеты"])
async def get_university_detail(uni_id: int):


    uni = next((u for u in fake_db if u.id == uni_id), None)

    if uni is None:
        raise HTTPException(status_code=404, detail="Университет не найден")
    return uni



@app.get("/api/compare/", response_model=List[University], tags=["Сравнение"])
async def compare_universities(
        u_ids: List[int] = Query(..., description="Список ID ВУЗов для сравнения")
):


    results = [u for u in fake_db if u.id in u_ids]

    if not results:
        raise HTTPException(status_code=404, detail="Не найдены ВУЗы по указанным ID")

    return results