# Government Scheme Data Model

## Purpose

This document captures the Phase 3 data modeling outcome for the Government Scheme Finder backend. It explains the JSON schema, the shape of scheme records, and the roadmap for using this model in later phases.

## Schema location

- `backend/app/schemas/government_scheme.schema.json`
- `backend/app/data/government_schemes.json`

## Model overview

The model represents each government scheme as a structured object with the following main sections:

- `schemeId`, `name`, `description`: canonical identity and description
- `category`, `subCategory`, `tags`: classification and search metadata
- `ministry`, `implementingAgency`: governance and execution ownership
- `targetPopulation`: user-facing audience signal
- `eligibilityCriteria`: structured rules for matching beneficiaries
- `benefits`: the actual outcomes and entitlements
- `applicationProcess`: how people apply
- `documentsRequired`: supporting evidence needed for application
- `geography`: coverage scope by national/state/district
- `status`, `launchDate`, `lastUpdated`: lifecycle and freshness metadata
- `sourceUrl`: authoritative reference link
- `notes`: internal maintainer guidance

## Why this model

- It keeps all scheme records consistent across the backend.
- It makes eligibility and benefit matching machine-readable.
- It separates metadata, benefits, and process details for cleaner query design.
- It supports both national and region-specific schemes.
- It is intentionally easy to migrate later to a relational data model.

## Migration strategy to PostgreSQL

### Option 1: normalized relational tables

Create a `schemes` table for primary scalar fields, and child tables for structured arrays:

- `scheme_eligibility`
- `scheme_benefits`
- `scheme_application_steps`
- `scheme_documents`
- `scheme_geography_states`
- `scheme_tags`

This approach is ideal for query performance and relational integrity.

### Option 2: hybrid relational + JSONB

Store core scheme fields in `schemes` and keep flexible sections as `JSONB`:

- `eligibility_criteria jsonb`
- `benefits jsonb`
- `application_process jsonb`
- `documents_required jsonb`
- `geography jsonb`

This approach is useful for rapid prototyping and when the shape may evolve.

### Validation and governance

- Use the JSON Schema as the authoritative application-level validator before persistence.
- Enforce `schemeId` uniqueness in PostgreSQL.
- Add indexes on `category`, `status`, and `tags` for search.
- Use `created_at` / `updated_at` columns in the database for data lifecycle tracking.

## Next logical step

Phase 4 should focus on:

1. defining the data ingestion and validation process for incoming scheme records
2. building a seed loader for the sample scheme data
3. wiring the schema into the backend so all scheme entries are validated before use
4. planning the first set of eligibility query patterns

This document is intentionally non-code so it remains a pure design artifact for the backend architecture.
