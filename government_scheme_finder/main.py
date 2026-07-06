"""Search feature for Government Scheme Finder."""

from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class Scheme:
    """Represents a government scheme and its eligibility rules."""

    name: str
    category: str
    state: str
    description: str
    eligibility: str
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    occupations: Tuple[str, ...] = field(default_factory=tuple)
    max_income: Optional[int] = None
    eligible_genders: Tuple[str, ...] = field(
        default_factory=lambda: ("All",)
    )


def _normalize(value: str) -> str:
    """Return a lowercase, trimmed version of a text value."""
    return value.strip().lower()


def search_schemes(
    schemes: Sequence[Scheme],
    *,
    state: Optional[str] = None,
    age: Optional[int] = None,
    occupation: Optional[str] = None,
    income: Optional[int] = None,
    gender: Optional[str] = None,
) -> List[Scheme]:
    """Return schemes that match the provided search criteria."""

    normalized_state = _normalize(state) if state else None
    normalized_occupation = _normalize(occupation) if occupation else None
    normalized_gender = _normalize(gender) if gender else None

    matching_schemes: List[Scheme] = []

    for scheme in schemes:
        if normalized_state and _normalize(scheme.state) != normalized_state:
            continue

        if age is not None:
            if scheme.min_age is not None and age < scheme.min_age:
                continue
            if scheme.max_age is not None and age > scheme.max_age:
                continue

        if normalized_occupation:
            if not any(
                _normalize(job) == normalized_occupation
                for job in scheme.occupations
            ):
                continue

        if income is not None and scheme.max_income is not None:
            if income > scheme.max_income:
                continue

        if normalized_gender:
            normalized_eligible_genders = {
                _normalize(gender_option)
                for gender_option in scheme.eligible_genders
            }
            if "all" not in normalized_eligible_genders and (
                normalized_gender not in normalized_eligible_genders
            ):
                continue

        matching_schemes.append(scheme)

    return matching_schemes


def create_sample_schemes() -> List[Scheme]:
    """Return a small sample dataset for early development."""
    return [
        Scheme(
            name="Pradhan Mantri Awas Yojana",
            category="Housing",
            state="India",
            description="Housing support for economically weaker sections.",
            eligibility="Low-income families are eligible.",
            min_age=18,
            max_age=70,
            occupations=("Any",),
            max_income=500000,
            eligible_genders=("All",),
        ),
        Scheme(
            name="PM-KISAN",
            category="Agriculture",
            state="India",
            description="Income support for eligible farmer families.",
            eligibility="Small and marginal farmer families are eligible.",
            min_age=18,
            max_age=75,
            occupations=("Farmer", "Agricultural Worker"),
            max_income=300000,
            eligible_genders=("All",),
        ),
        Scheme(
            name="National Scholarship Portal",
            category="Education",
            state="India",
            description="Financial aid for eligible students.",
            eligibility="Students meeting academic and income criteria can apply.",
            min_age=16,
            max_age=30,
            occupations=("Student",),
            max_income=800000,
            eligible_genders=("Male", "Female", "Transgender"),
        ),
    ]


def main() -> None:
    """Run a small demonstration of the search feature."""
    schemes = create_sample_schemes()
    results = search_schemes(
        schemes,
        state="India",
        age=30,
        occupation="Farmer",
        income=250000,
        gender="Male",
    )

    print("Government Scheme Finder India")
    print("Matching schemes:")

    for scheme in results:
        print(f"- {scheme.name} ({scheme.category})")


if __name__ == "__main__":
    main()

