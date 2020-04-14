import json 
import re

from config import *

class Preprocessor:
    @staticmethod
    def clean_text(text):
        """
        Takes in a piece of text and eliminates unnecessary features such as capitalization, trailing or leading 
        whitespaces, and spaces between words. This will also remove URLs

        Parameters
        ----------
        text : str
            String that we want to clean up. In practice, this is source code. 
        
        Returns
        -------
        cleaned_text : str
            String that is the same as the input text but with the unnecessary features removed.
        """
        punctuation = ["\""]
        text = str(text)
        cleaned_text = re.sub(r"http\S+", '', text) #regex code to remove URLs
        cleaned_text = cleaned_text.lower()
        cleaned_text= cleaned_text.replace(" ", "") #remove whitespace
        cleaned_text= cleaned_text.replace("\n", "") #remove the newline character
        cleaned_text= cleaned_text.replace("\t", "") #remove the newline character
        for punctuation_mark in punctuation:
            cleaned_text = cleaned_text.replace(punctuation_mark, "")
        return cleaned_text

    # @staticmethod
    # def remove_common_code(text):
    #     '''
    #     Function that removes code or text snippets that are expected in all submissions

    #     Parameters
    #     ----------
    #     text : str
    #         The student's code that we want to remove common code for 

    #     Returns
    #     -------
    #     text: str
    #         A cleaned up version of the text with the common parts removed
    #     '''
    #     text = str(text) # explicit type casting 
    #     common_code = cfg["common_code"] # find all the pieces of text we should remove
    #     for code in common_code:
    #         code = Preprocessor.clean_text(code)
    #         text = text.replace(code, "")
    #     return text

    @staticmethod
    def remove_common_code(text):
        '''
        Function that removes common text and common code from 
        '''

        text = str(text) # explicit type casting 
        sample_submission = system_cfg["sample_solution"]
        with open(sample_submission) as sample_submission_file:
            contents = sample_submission_file.readlines()
        tokens_to_remove = [Preprocessor.clean_text(x) for x in contents]
        for token in tokens_to_remove:
            text = text.replace(token, "")
        return text


    


    
    