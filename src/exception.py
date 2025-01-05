import sys ## sys library will have information of our exceptions
import logging

def error_message_detail(error,error_detail:sys):
    #The sys.exc_info() function returns a tuple containing the exception type, exception instance, and traceback object for the currently handled exception
    _,_,exc_tb = error_detail.exc_info()
    # This gives the file name 
    file_name = exc_tb.tb_frame.f_code.co_filename 
    line_no = exc_tb.tb_lineno
    error_message = "Error occured in the python script[{0}] line number[{1}]".format(file_name,line_no,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = eval(error_message,error_message_detail = error_detail)
    def __str__(self):
        return self.error_message
    
    