from pydantic import BaseModel


class InputData(BaseModel):
    age: int
    num_sexual_partners: int
    first_sexual_intercourse: int
    num_pregnancies: int
    smoking_years: float
    hormonal_contraceptives_years: float
    iud_years: float
    num_stds: int
    stds_condylomatosis: int
    stds_cervical_condylomatosis: int
    stds_hiv: int
    stds_hpv: int
    dx_cin: int
    dx_hpv: int