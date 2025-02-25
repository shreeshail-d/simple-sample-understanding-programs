import configparser  # For reading the config.ini file

import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from simple_calculator.simple_calculator import SimpleCalculator

from OperationModel import OperationModel

app = FastAPI()

# Read configuration from config.ini
lobj_config = configparser.ConfigParser()
lobj_config.read(
    '/home/cerelabs/Workarea/shreeshail/practice/perform_arithmetic_operation/perform_arithmetic_operation/data/config.ini')

lstr_host = lobj_config.get('ENVIRONMENT', 'LOCAL_HOST')
lint_port = lobj_config.getint('ENVIRONMENT', 'LOCAL_PORT')
lint_custom_success_status_code = lobj_config.getint('ENVIRONMENT',
                                                     'LOCAL_CUSTOM_SUCCESS_STATUS_CODE')  # Custom success status code


class PerformArithmeticOperation:
    """Class to handle arithmetic operations."""

    def __init__(self):
        self.lobj_calculator = SimpleCalculator("Instance1")

    def calculate(self, data: OperationModel):
        pfl_first_number = data.lfl_first_number
        pfl_second_number = data.lfl_second_number
        pstr_operation = data.lstr_operation.lower()

        # Perform the respective arithmetic operation
        if pstr_operation == "addition":
            return self.lobj_calculator.addition(pfl_first_number, pfl_second_number)
        elif pstr_operation == "subtraction":
            return self.lobj_calculator.subtraction(pfl_first_number, pfl_second_number)
        elif pstr_operation == "multiplication":
            return self.lobj_calculator.multiplication(pfl_first_number, pfl_second_number)
        elif pstr_operation == "division":
            if pfl_second_number == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return self.lobj_calculator.division(pfl_first_number, pfl_second_number)
        elif pstr_operation == "modulus":
            if pfl_second_number == 0:
                raise ZeroDivisionError("Cannot perform modulus by zero.")
            return self.lobj_calculator.modulus(pfl_first_number, pfl_second_number)
        else:
            raise ValueError(
                "Invalid operation. Choose from addition, subtraction, multiplication, division, or modulus."
            )


lobj_operation_handler = PerformArithmeticOperation()


@app.post("/arithmetic_operation", status_code=status.HTTP_200_OK)
async def perform_arithmetic_operation(data: OperationModel):
    try:
        result = lobj_operation_handler.calculate(data)

        # Return success response
        return JSONResponse(
            content={
                "status": "success",
                "message": "Operation completed successfully",
                "first_number": data.lfl_first_number,
                "second_number": data.lfl_second_number,
                "operation": data.lstr_operation.lower(),
                "result": result,
            },
            status_code=status.HTTP_200_OK,
        )

    except ZeroDivisionError as e:
        # Handle division by zero errors
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except ValueError as e:
        # Handle any value errors that might arise during the operation
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except AttributeError as e:
        # Handle missing attribute errors, in case the request body is invalid
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Missing attribute in the request data: {str(e)}",
        )
    except TypeError as e:
        # Handle incorrect data type errors
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Incorrect data type in the request data: {str(e)}",
        )
    except Exception as e:
        # Catch any unexpected errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}",
        )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # Custom error handler for validation errors
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status": "error",
            "message": "Validation error occurred",
            "detail": exc.errors(),
        },
    )


if __name__ == "__main__":
    uvicorn.run(app, host=lstr_host, port=lint_port)
