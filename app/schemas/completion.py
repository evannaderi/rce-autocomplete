from pydantic import BaseModel, Field
from typing import Optional


class CompletionRequest(BaseModel):
    content_up_until_cursor: str = Field(..., description="The text to be completed"),
    all_content_in_rce : str = Field(..., description="The text to be completed"),
    max_tokens: Optional[int] = Field(
        100, description="Maximum tokens to generate"
    )
    temperature: Optional[float] = Field(
        0.8, description="Sampling temperature"
    )
    stream: Optional[bool] = Field(
        False, description="Whether to stream the response"
    )
    provider: Optional[str] = Field(
        "anthropic", description="The provider to use for completion"
    )
    model: Optional[str] = Field(
        "us.anthropic.claude-3-5-haiku-20241022-v1:0", description="The model to use for completion"
    )

class DummyCompletionRequest(BaseModel):
    content_up_until_cursor: str = Field(..., description="The text to be completed")
    all_content_in_rce : str = Field(..., description="The text to be completed")


# May have to edit
class CompletionResponse(BaseModel):
    suggestion: str
    tokens_used: int


class DummyCompletionResponse(BaseModel):
    suggestion: str
