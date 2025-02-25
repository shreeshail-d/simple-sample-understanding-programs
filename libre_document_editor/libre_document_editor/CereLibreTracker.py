import os

from new_dtect_logging.logger import DtectLogging
from odf.opendocument import load
from odf.text import P

import cere_libre_tracker.configuration as config

if __name__ == "__main__":
    # when debbuging
    log_file_name = __file__.split(
        os.sep)[-2] + "_" + __file__.split(os.sep)[-1].split(".")[0]
    lobj_dtect_logger = DtectLogging(log_file_name)
else:
    # used in parent module
    lobj_dtect_logger = DtectLogging()


class CereLibreTracker:
    """
        A utility class to modify ODT documents by adding, deleting, or replacing text.
        Uses the odfpy library to manipulate OpenDocument Text (ODT) files.

        Methods:
            add_text_after_match(odt_file_path, search_text, text_to_add):
                Adds text immediately after the first occurrence of search_text.

            delete_text(odt_file_path, text_to_delete):
                Deletes the first occurrence of text_to_delete from the document.

            replace_text(odt_file_path, search_text, replacement_text):
                Replaces the first occurrence of search_text with replacement_text.
        """

    @staticmethod
    def add_text_after_match(odt_file_path, search_text, text_to_add):
        """
        Adds text after the first occurrence of search_text in an ODT file.

        :param odt_file_path: Path to the ODT file.
        :param search_text: The text to find in the document.
        :param text_to_add: The text to add after the first occurrence of search_text.
        """
        try:
            doc = load(odt_file_path)
            modified = False

            for elem in doc.getElementsByType(P):
                if elem.hasChildNodes():
                    for child in elem.childNodes:
                        if child.nodeType == child.TEXT_NODE and search_text in child.data:
                            child.data = child.data.replace(search_text, search_text + text_to_add, 1)
                            modified = True
                            lobj_dtect_logger.logger.info(f"Added text after first occurrence of '{search_text}'.")
                            break
                if modified:
                    break

            if modified:
                doc.save(odt_file_path)
                lobj_dtect_logger.logger.info(f"File successfully updated and saved: {odt_file_path}")
            else:
                lobj_dtect_logger.logger.warning(f"Text '{search_text}' not found. No changes made.")
        except Exception as e:
            lobj_dtect_logger.logger.error(f"Failed to add text: {e}")

    @staticmethod
    def delete_text(odt_file_path, text_to_delete):
        """
        Deletes the first occurrence of text_to_delete in an ODT file.

        :param odt_file_path: Path to the ODT file.
        :param text_to_delete: The text to be deleted.
        """
        try:
            doc = load(odt_file_path)
            modified = False

            for elem in doc.getElementsByType(P):
                if elem.hasChildNodes():
                    for child in elem.childNodes:
                        if child.nodeType == child.TEXT_NODE and text_to_delete in child.data:
                            child.data = child.data.replace(text_to_delete, "", 1)
                            modified = True
                            lobj_dtect_logger.logger.info(f"Deleted first occurrence of '{text_to_delete}'.")
                            break
                if modified:
                    break

            if modified:
                doc.save(odt_file_path)
                lobj_dtect_logger.logger.info(f"File successfully updated and saved: {odt_file_path}")
            else:
                lobj_dtect_logger.logger.warning(f"Text '{text_to_delete}' not found. No changes made.")
        except Exception as e:
            lobj_dtect_logger.logger.error(f"Failed to delete text: {e}")

    @staticmethod
    def replace_text(odt_file_path, search_text, replacement_text):
        """
        Replaces the first occurrence of search_text with replacement_text in an ODT file.

        :param odt_file_path: Path to the ODT file.
        :param search_text: The text to find in the document.
        :param replacement_text: The text to replace search_text with.
        """
        try:
            doc = load(odt_file_path)
            modified = False

            for elem in doc.getElementsByType(P):
                if elem.hasChildNodes():
                    for child in elem.childNodes:
                        if child.nodeType == child.TEXT_NODE and search_text in child.data:
                            child.data = child.data.replace(search_text, replacement_text, 1)
                            modified = True
                            lobj_dtect_logger.logger.info(
                                f"Replaced first occurrence of '{search_text}' with '{replacement_text}'.")
                            break
                if modified:
                    break

            if modified:
                doc.save(odt_file_path)
                lobj_dtect_logger.logger.info(f"File successfully updated and saved: {odt_file_path}")
            else:
                lobj_dtect_logger.logger.warning(f"Text '{search_text}' not found. No changes made.")
        except Exception as e:
            lobj_dtect_logger.logger.error(f"Failed to replace text: {e}")


if __name__ == "__main__":
    try:
        file_path = config.INPUT_PATH
        lobj_dtect_logger.logger.info(f"Processing file: {file_path}")

        CereLibreTracker.add_text_after_match(file_path, "Read", "SAMPLE TEXT ADDED AFTER READ")
        CereLibreTracker.delete_text(file_path, "< CHECK TEXT FIVE>")
        CereLibreTracker.replace_text(file_path, "Input",
                                      "- output -")

        lobj_dtect_logger.logger.info("Processing completed.")
    except Exception as error:
        lobj_dtect_logger.logger.critical(f"Critical error in main execution: {error}")
