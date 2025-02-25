import os

from cognitive_framework_commons.common_operations.common_operations import CommonOperations
from new_dtect_logging.logger import DtectLogging

if __name__ == "__main__":
    # when debbuging
    log_file_name = __file__.split(
        os.sep)[-2] + "_" + __file__.split(os.sep)[-1].split(".")[0]
    lobj_dtect_logger = DtectLogging(log_file_name)

else:
    # used in parent module
    lobj_dtect_logger = DtectLogging()

try:
    # =======================================================================
    # creates i/p used for reading configurations from a file.
    # =======================================================================
    lstr_config_file_path = os.path.dirname(
        os.path.realpath(__file__)) + os.path.sep + "data" + os.path.sep + "config.ini"
    ldict_sections_and_dict_of_properties = dict()

    ldict_sections_and_dict_of_properties["ENVIRONMENT"] = {
        "INPUT_PATH": "",
    }

    # =======================================================================
    # read config
    # =======================================================================
    lobj_common_operations = CommonOperations()
    ldict_configurations = lobj_common_operations.read_all_configs(
        ldict_sections_and_dict_of_properties, lstr_config_file_path)

    # ===================================================================
    # Environment Variables
    # ===================================================================
    INPUT_PATH = str(ldict_configurations['INPUT_PATH'])

except Exception as ex:
    lobj_dtect_logger.logger.error("\nError: " + str(ex), exc_info=True)
