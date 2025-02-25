import os
from new_dtect_logging.logger import DtectLogging
import simple_calculator.configuration as config

if __name__ == "__main__":
    # when debugging
    log_file_name = __file__.split(os.sep)[-2] + "_" + __file__.split(os.sep)[-1].split(".")[0]
    lobj_log = DtectLogging(log_file_name)
else:
    # used in parent module
    lobj_log = DtectLogging()

class SimpleCalculator:
    def __init__(self, gstr_n: str):
        try:
            self.gstr_n = gstr_n  # Shared parameter (name)
        except Exception as e:
            lobj_log.logger.error(f"Error initializing SimpleCalculator: {e}",exc_info=True)

    def main(self, pint_operation_option: int, pint_num_one: float, pint_num_two: float):
        try:
            lobj_log.logger.info(f"{self.gstr_n} is choosing operation: {pint_operation_option}")
            if pint_operation_option == 1:
                return self.addition(pint_num_one, pint_num_two)
            elif pint_operation_option == 2:
                return self.subtraction(pint_num_one, pint_num_two)
            elif pint_operation_option == 3:
                return self.multiplication(pint_num_one, pint_num_two)
            elif pint_operation_option == 4:
                return self.division(pint_num_one, pint_num_two)
            else:
                lobj_log.logger.warning(f"Invalid operation choice: {pint_operation_option}")
                return "Invalid option"
        except Exception as e:
            lobj_log.logger.error(f"Error in main operation: {e}")
            return f"An error occurred: {e}"

    def addition(self, pint_num_one: float, pint_num_two: float) -> float:
        try:
            result = pint_num_one + pint_num_two
            lobj_log.logger.info(f"Addition result: {result}")
            return result  # Return float directly
        except Exception as e:
            lobj_log.logger.error(f"Error in addition: {e}")
            return float('nan')  # Return NaN if an error occurs

    def subtraction(self, pint_num_one: float, pint_num_two: float) -> float:
        try:
            result = pint_num_one - pint_num_two
            lobj_log.logger.info(f"Subtraction result: {result}")
            return result  # Return float directly
        except Exception as e:
            lobj_log.logger.error(f"Error in subtraction: {e}")
            return float('nan')  # Return NaN if an error occurs

    def multiplication(self, pint_num_one: float, pint_num_two: float) -> float:
        try:
            result = pint_num_one * pint_num_two
            lobj_log.logger.info(f"Multiplication result: {result}")
            return result  # Return float directly
        except Exception as e:
            lobj_log.logger.error(f"Error in multiplication: {e}")
            return float('nan')  # Return NaN if an error occurs

    def division(self, pint_num_one: float, pint_num_two: float) -> float:
        try:
            if pint_num_two == 0:
                raise ValueError("Division by zero is not allowed")
            result = pint_num_one / pint_num_two
            lobj_log.logger.info(f"Division result: {result}")
            return result  # Return float directly
        except ValueError as e:
            lobj_log.logger.error(f"Error during division: {e}")
            return float('nan')  # Return NaN if an error occurs
        except Exception as e:
            lobj_log.logger.error(f"Unexpected error in division: {e}")
            return float('nan')  # Return NaN if an error occurs

    def modulus(self, pint_num_one: float, pint_num_two: float) -> float:
        try:
            if pint_num_two == 0:
                raise ValueError("Modulus by zero is not allowed")
            result = pint_num_one % pint_num_two
            lobj_log.logger.info(f"Modulus result: {result}")
            return result  # Return float directly
        except ValueError as e:
            lobj_log.logger.error(f"Error during modulus operation: {e}")
            return float('nan')  # Return NaN if an error occurs
        except Exception as e:
            lobj_log.logger.error(f"Unexpected error in modulus operation: {e}")
            return float('nan')  # Return NaN if an error occurs


# This section remains the same, as it is used to demonstrate the functionality
if __name__ == "__main__":
    lstr_name = str(config.GLOBAL_SAMPLE_NAME)
    lobj_log.logger.info(f"User {lstr_name} has started the program.")
    print(f"{lstr_name.upper()}, {config.LOCAL_VARIABLE}")
    print(f"{config.GLOBAL_STR1} {lstr_name} {config.GLOBAL_STR2}")

    ans = SimpleCalculator(lstr_name)
    print(f"Hello! {lstr_name}")

    lint_1, lint_2 = 0, 0
    result = 0

    try:
        lint_1 = config.LOCAL_NUM_1
        lobj_log.logger.info(f"User {lstr_name} entered first number: {lint_1}")
    except ValueError as e:
        print(f"ERROR!! Wrong input provided, please check input data and format, {e}")
        lobj_log.logger.error(f"User {lstr_name} entered an invalid first number: {e}")

    try:
        lint_2 = config.LOCAL_NUM_2
        lobj_log.logger.info(f"User {lstr_name} entered second number: {lint_2}")
    except ValueError as e:
        print(f"ERROR!! Wrong input provided, please check input data and format, {e}")
        lobj_log.logger.error(f"User {lstr_name} entered an invalid second number: {e}")

    try:
        lint_value = config.LOCAL_OPERATION
    except ValueError as e:
        print(f"ERROR!! Wrong input provided, please check input data and format, {e}")
        lobj_log.logger.error(f"User {lstr_name} entered an invalid operation choice: {e}")
    else:
        result = ans.main(lint_value, lint_1, lint_2)
        print(result)
        lobj_log.logger.info(f"User {lstr_name} has exited the program.")
        print(f"Goodbye, {lstr_name}!")
