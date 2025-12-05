from pydantic import BaseModel, Field
from typing import List, Optional



class InternationalCooperation(BaseModel):
    exchange_programs: str = Field(..., description="Программы обмена")
    partner_universities: str = Field(..., description="Университеты-партнеры")



class AcademicProgram(BaseModel):
    id: int
    program_name: str
    description: str


    score: float = Field(..., description="Мин. проходной балл (ЕНТ)")
    duration: int = Field(4, description="Длительность обучения (годы)")



class University(BaseModel):

    id: int
    name: str
    mission: str
    achievements: str
    admission_requirements: str


    tour_link: Optional[str] = None


    programs: List[AcademicProgram]


    cooperation: InternationalCooperation