"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Lead capture for consultations
class Lead(BaseModel):
    """
    Leads captured from the website
    Collection name: "lead"
    """
    name: str = Field(..., description="Contact person full name", min_length=2)
    email: EmailStr = Field(..., description="Work email")
    company: Optional[str] = Field(None, description="Company or organization")
    role: Optional[str] = Field(None, description="Role or title")
    phone: Optional[str] = Field(None, description="Phone number")
    project_type: Optional[str] = Field(None, description="Type of development (e.g., residential, commercial)")
    timeline: Optional[Literal['<3 months','3-6 months','6-12 months','>12 months']] = Field(None, description="Indicative timeline")
    budget_range: Optional[Literal['< $1M','$1M-$5M','$5M-$20M','> $20M']] = Field(None, description="Budget range")
    message: Optional[str] = Field(None, max_length=2000, description="Short project brief")
    source: Optional[str] = Field('website', description="Lead source")
    consent: bool = Field(..., description="Consent to be contacted")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
