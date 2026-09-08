from pydantic import BaseModel, Field
from typing import Optional
# ============================================================
# TODO: Create Employee Model
# ============================================================

# Fields:
#   - id: int
#   - name: str
#       → Must contain at least 3 characters
#
#   - department: Optional[str]
#       → Defaults to "General" if not provided
#
#   - salary: float
#       → Must be greater than or equal to 10,000
# ============================================================

class Employee(BaseModel):
    id: int

    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples=["Waseem Ahmed"]
    )

    department: str | None = "General"

    salary: float = Field(..., ge=10000)