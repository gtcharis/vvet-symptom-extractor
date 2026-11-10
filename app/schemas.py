from typing import Literal
from pydantic import BaseModel, Field, ConfigDict


SignValue = Literal["yes", "no", "not_sure"]


class ExtractRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    message: str = Field(min_length=1)


class Finding(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sign_id: Literal[
        "reduced_appetite",
        "weakness",
        "swelling",
        "rapid_breathing",
        "cloudy_eye",
        "froth_nose_mouth",
        "red_urine",
        "unable_to_stand",
        "ticks"
    ]

    value: SignValue

    quote: str = Field(min_length=1)


class ExtractResponse(BaseModel):
    findings: list[Finding]
    escalate: bool
    reason: str