import logging
import traceback

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from rbac.application.common.http_response.code_enum import CodeEnum
from rbac.application.common.http_response.http_api_response import HttpApiResponse
from rbac.application.exception.application_exception import ApplicationException

logger = logging.getLogger(__name__)

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(ApplicationException)
    async def application_exception_handler(request: Request, e: ApplicationException):
        logger.error(f"ApplicationException occurred. code={e.code.name}, message={e.message}")
        logger.error("".join(traceback.format_exception(type(e), e, e.__traceback__)))

        if e.code == CodeEnum.FRS_002:
            return JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content=HttpApiResponse.from_exception_message(
                    code=e.code,
                    message=e.message,
                    data=e.data
                ).__dict__
            )

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=HttpApiResponse.from_exception_message(
                code=e.code,
                message=e.message,
                data=e.data
            ).__dict__
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, e: RequestValidationError):
        logger.error(f"RequestValidationError occurred. message={str(e)}")
        logger.error("".join(traceback.format_exception(type(e), e, e.__traceback__)))

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=HttpApiResponse.from_exception_message(
                code=CodeEnum.FRS_003,
                message=e.args[0][0]["msg"],
                data={
                    "input":e.args[0][0]["input"]
                }
            ).__dict__
        )


    @app.exception_handler(Exception)
    def general_exception_handler(request: Request, e: Exception):
        logger.error(f"Exception occurred. message={str(e)}")
        logger.error("".join(traceback.format_exception(type(e), e, e.__traceback__)))

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=HttpApiResponse.from_exception_message(
                code=CodeEnum.FRS_004,
                message=CodeEnum.FRS_004.description,
                data={}
            ).__dict__
        )
