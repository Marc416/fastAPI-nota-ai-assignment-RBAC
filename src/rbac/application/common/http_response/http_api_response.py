from __future__ import annotations
from typing import Optional, Any, Dict
from pydantic import BaseModel

from rbac.application.common.http_response.code_enum import CodeEnum


class HttpApiResponse(BaseModel):
    code: CodeEnum
    message: Optional[str] = None
    data: Optional[Any] = None

    @classmethod
    def ok(cls) -> HttpApiResponse:
        return HttpApiResponse(
            code=CodeEnum.RS_000,
            message=CodeEnum.RS_000.description,
            data=None
        )

    @classmethod
    def of(cls, data: Optional[Any]) -> HttpApiResponse:
        return HttpApiResponse(
            code=CodeEnum.RS_000,
            message=CodeEnum.RS_000.description,
            data=data
        )

    @classmethod
    def from_exception_message(cls, message: str, code: CodeEnum, data: Dict[str, Any]) -> HttpApiResponse:
        return HttpApiResponse(
            code=code,
            message=message,
            data=data
        )
