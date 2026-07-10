from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl, ConfigDict


class SchemeCategory(str, Enum):
    financial = "financial"
    health = "health"
    energy = "energy"
    social = "social"
    education = "education"
    employment = "employment"
    housing = "housing"


class SchemeStatus(str, Enum):
    active = "active"
    closed = "closed"
    paused = "paused"
    draft = "draft"


class BenefitType(str, Enum):
    cash = "cash"
    subsidy = "subsidy"
    insurance = "insurance"
    service = "service"
    other = "other"


class EligibilityCriteria(BaseModel):
    age_range: Optional[str] = Field(
        None,
        description="Age eligibility range, for example '18 to 59'.",
        alias="ageRange",
    )
    income_range: Optional[str] = Field(
        None,
        description="Income eligibility threshold or band.",
        alias="incomeRange",
    )
    categories: List[str] = Field(
        default_factory=list,
        description="Applicable beneficiary categories, e.g. 'BPL', 'SC/ST'.",
    )
    residency_required: Optional[str] = Field(
        None,
        description="Residency requirement, such as 'Indian citizen'.",
        alias="residencyRequired",
    )
    other_conditions: Optional[str] = Field(
        None,
        description="Additional eligibility conditions.",
        alias="otherConditions",
    )

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


class Benefit(BaseModel):
    type: BenefitType = Field(
        ..., description="Benefit type, e.g. 'cash', 'subsidy', 'service'."
    )
    description: str = Field(..., description="Description of the benefit.")
    amount: Optional[str] = Field(
        None, description="Monetary amount or value description."
    )
    frequency: Optional[str] = Field(
        None, description="Payment or benefit frequency."
    )
    max_coverage: Optional[str] = Field(
        None,
        description="Maximum coverage for the benefit, if applicable.",
        alias="maxCoverage",
    )

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


class ApplicationProcess(BaseModel):
    mode: List[str] = Field(
        default_factory=list,
        description="Application channels, e.g. 'online', 'offline'.",
    )
    steps: List[str] = Field(
        default_factory=list,
        description="High-level application steps.",
    )
    website: Optional[HttpUrl] = Field(
        None,
        description="Official application or information URL.",
    )
    contact_number: Optional[str] = Field(
        None,
        description="Helpdesk or support phone number.",
        alias="contactNumber",
    )

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


class DocumentRequirement(BaseModel):
    name: str = Field(..., description="Document name.")
    optional: bool = Field(
        False,
        description="Whether the document is optional for the application.",
    )
    description: Optional[str] = Field(
        None,
        description="Additional detail about the required document.",
    )

    model_config = ConfigDict(extra="forbid")


class Geography(BaseModel):
    national: bool = Field(
        False,
        description="Whether the scheme is available nationwide.",
    )
    states: List[str] = Field(
        default_factory=list,
        description="States where the scheme is available.",
    )
    districts: List[str] = Field(
        default_factory=list,
        description="Districts where the scheme is available.",
    )

    model_config = ConfigDict(extra="forbid")


class SchemeBase(BaseModel):
    scheme_id: str = Field(
        ..., description="Unique scheme identifier.", alias="schemeId"
    )
    name: str = Field(..., description="Official scheme name.")
    description: str = Field(..., description="Short scheme summary.")
    category: SchemeCategory = Field(..., description="Primary scheme category.")
    sub_category: Optional[str] = Field(
        None,
        description="Optional finer-grained classification.",
        alias="subCategory",
    )
    ministry: str = Field(..., description="Implementing ministry.")
    implementing_agency: Optional[str] = Field(
        None,
        description="Implementing agency.",
        alias="implementingAgency",
    )
    target_population: Optional[str] = Field(
        None,
        description="High-level target population.",
        alias="targetPopulation",
    )
    eligibility_criteria: EligibilityCriteria = Field(
        default_factory=EligibilityCriteria,
        alias="eligibilityCriteria",
    )
    benefits: List[Benefit] = Field(default_factory=list, description="List of benefits.")
    application_process: Optional[ApplicationProcess] = Field(
        None, alias="applicationProcess"
    )
    documents_required: List[DocumentRequirement] = Field(
        default_factory=list,
        alias="documentsRequired",
        description="Documents required for application.",
    )
    geography: Geography = Field(default_factory=Geography)
    status: SchemeStatus = Field(..., description="Current scheme status.")
    launch_date: date = Field(..., alias="launchDate")
    last_updated: datetime = Field(..., alias="lastUpdated")
    tags: List[str] = Field(default_factory=list, description="Search-friendly tags.")
    source_url: Optional[HttpUrl] = Field(
        None, alias="sourceUrl", description="Authoritative reference URL."
    )
    notes: Optional[str] = Field(None, description="Internal maintainer notes.")

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


class SchemeCreate(SchemeBase):
    pass


class SchemeResponse(SchemeBase):
    pass
