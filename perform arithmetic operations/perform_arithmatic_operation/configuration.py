"""
Created on 11-Dec-2024
"""
import os

from cognitive_framework_commons.common_operations.common_operations import CommonOperations
from new_dtect_logging.logger import DtectLogging

if __name__ == "__main__":
    # when debbuging
    log_file_name = __file__.split(os.sep)[-2] + "_" + __file__.split(os.sep)[-1].split(".")[0]
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
    ldict_values = dict()
    ldict_values["ENVIRONMENT"] = {
        "LOCAL_VARIABLE": "",
        "LOCAL_NUM_1": "",
        "LOCAL_NUM_2": "",
        "LOCAL_CUSTOM_SUCCESS_STATUS_CODE": "",
        "LOCAL_PORT": "",
        "LOCAL_HOST": "",
    }
    ldict_values["GENERAL"] = {
        "GLOBAL_SAMPLE_NAME": "",
        "GLOBAL_STR1": "",
        "GLOBAL_STR2": ""
    }

    # =======================================================================
    # read config
    # =======================================================================
    lobj_sample = CommonOperations()
    ldict_configurations = lobj_sample.read_all_configs(
        ldict_values,
        lstr_config_file_path)

    # ===================================================================
    # set class variables
    # ===================================================================

    LOCAL_VARIABLE = str(ldict_configurations['LOCAL_VARIABLE'])
    LOCAL_NUM_1 = int(ldict_configurations['LOCAL_NUM_1'])
    LOCAL_NUM_2 = int(ldict_configurations['LOCAL_NUM_2'])
    LOCAL_CUSTOM_SUCCESS_STATUS_CODE = int(ldict_configurations['LOCAL_CUSTOM_SUCCESS_STATUS_CODE'])
    LOCAL_PORT = int(ldict_configurations['LOCAL_PORT'])
    LOCAL_HOST = str(ldict_configurations['LOCAL_HOST'])

    GLOBAL_SAMPLE_NAME = str(ldict_configurations['GLOBAL_SAMPLE_NAME'])
    GLOBAL_STR1 = str(ldict_configurations['GLOBAL_STR1'])
    GLOBAL_STR2 = str(ldict_configurations['GLOBAL_STR2'])

except Exception as ex:
    print(f"UNEXPECTED ERROR OCCURRED: {ex}")

# pip install --upgrade pip setuptools wheel
