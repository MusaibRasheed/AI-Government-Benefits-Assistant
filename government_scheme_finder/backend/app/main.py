"""Minimal FastAPI application for the Government Scheme Finder backend."""

from fastapi import FastAPI


app = FastAPI(
    title="Government Scheme Finder API",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a welcome message for the API root endpoint."""
    return {"message": "Welcome to Government Scheme Finder API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return a simple health status payload."""
    return {"status": "healthy"}
