# Phase 4: Scheme Ingestion and Validation

## Goal

Define how government scheme records enter the backend safely and consistently, using the Phase 3 schema as the authoritative contract.

## Focus areas

1. Data validation
   - Use `backend/app/schemas/government_scheme.schema.json` as the source of truth.
   - Validate every scheme record before it is accepted into the system.
   - Catch missing required fields, invalid values, and unexpected structure.

2. Data ingestion pipeline
   - Seed the system from `backend/app/data/government_schemes.json`.
   - Support future data import sources, including CSV, API feeds, or manual JSON uploads.
   - Keep ingestion decoupled from business logic.

3. Record lifecycle and provenance
   - Track `lastUpdated` and `sourceUrl` for each scheme.
   - Preserve original data shape and source metadata during ingestion.
   - Maintain a versioned data source for iterative updates.

4. Eligibility and query readiness
   - Ensure `eligibilityCriteria`, `benefits`, `applicationProcess`, and `geography` are normalized enough to support matching logic later.
   - Identify which fields will power user queries and filters.

## Recommended next artifacts

- `backend/app/docs/scheme-ingestion-validation.md` (this document)
- `backend/app/docs/scheme-query-patterns.md` (mapping user questions to schema fields)
- `backend/app/data/government_schemes.json` (seed data source)
- `backend/app/schemas/government_scheme.schema.json` (schema contract)

## Why this is the right next step

- It turns the static model into a usable data flow without adding API or persistence code.
- It creates a safe boundary for future development: any record must conform before being used.
- It preserves the production-quality approach by separating validation and ingestion from the service layer.

## Example Phase 4 deliverables

- A validation design that uses JSON Schema or Pydantic for input checks.
- A documented import workflow for new scheme datasets.
- A first draft of eligibility query patterns keyed to schema fields.

## Next confirmation

Once you confirm this direction, I can continue by drafting the eligibility query pattern document or by outlining the validation rules more formally.
