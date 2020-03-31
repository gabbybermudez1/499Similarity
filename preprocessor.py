import json
import config as cfg
import re

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
        text = str(text)
        cleaned_text = re.sub(r"http\S+", '', text)
        cleaned_text = cleaned_text.lower()
        cleaned_text= cleaned_text.replace(" ", "") #remove whitespace
        cleaned_text= cleaned_text.replace("\n", "") #remove the newline character
        cleaned_text= cleaned_text.replace("\t", "") #remove the newline character
       
        return cleaned_text

    @staticmethod
    def remove_common_code(text):
        '''
        Function that removes code or text snippets that are expected in all submissions

        Parameters
        ----------
        text : str
            The student's code that we want to remove common code for 

        Returns
        -------
        text: str
            A cleaned up version of the text with the common parts removed
        '''
        text = str(text)
        # with open("config.json") as config_file:
        #     cfg = json.load(config_file)
        common_code = cfg.cfg["common_code"]
        for code in common_code:
            code = Preprocessor.clean_text(code)
            text = text.replace(code, "")
        return text


    
    