"""Used for testing read Write file """
import os

class Write:
    """static method returns file path """
    # pylint: disable=too-few-public-methods
    @staticmethod
    def dataframetocsvfile(filename, df_data):
        """static method returns file path """
        return df_data.to_csv(os.path.abspath(filename),float_format='%.2f',
                              index=True,
                              header=True)
