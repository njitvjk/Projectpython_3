import os

class Write:
    @staticmethod
    def DataFrameToCSVFile(filename, df):
        return df.to_csv(os.path.abspath(filename),float_format='%.2f', index=True, header=True)
