import json

class Preprocessor:

    @staticmethod
    def clean_text(text):
        """
        Takes in a piece of text and eliminates unnecessary features such as capitalization, trailing or leading 
        whitespaces, and spaces between words. 

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
        cleaned_text = text.lower()
        cleaned_text= cleaned_text.replace(" ", "") #remove whitespace
        cleaned_text= cleaned_text.replace("\n", "") #remove the newline character
        return cleaned_text

    @staticmethod
    def remove_common_code(text):
        text = str(text)
        with open("config.json") as config_file:
            cfg = json.load(config_file)
            common_code = cfg["common_code"]
        for code in common_code:
            text = text.replace(code, "")
        return text


    
    