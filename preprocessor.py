import json 
import re

from config import system_cfg

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

    @staticmethod
    def remove_common_code(text):
        '''
        This function removes code that is expected to be in all assignments. This function reads in the sample solution 
        files specified in the config.py line-by-line and removes each of the lines from the text

        Parameters
        ----------
        text : str
            This is the string that we want to remove common code from
        
        Returns
        -------
        text : str
            the parameter text after removing all of the common text
        '''
        text = str(text) # explicit type casting 


        sample_submission = system_cfg["sample_solution"]
        with open(sample_submission) as sample_submission_file:
            contents = sample_submission_file.readlines()
        tokens_to_remove = [Preprocessor.clean_text(x) for x in contents]
        for token in tokens_to_remove:
            text = text.replace(token, "")
        return text


    


    
    