# TODO: find out why doing the triple equals makes things slower
# TODO: implement rolling hashes
# TODO: make sure that you remove custom_hash in the revised_k_gram algo
# TODO: Consider whether or not adding punctuation removal might help
# TODO: Give revised_k_gram a new name


import hashlib
class Winnow:
    def __init__(self, text, k, w, use_rolling_hash=False):
        self.text =Winnow.clean_text(text)
        self.uncleaned_text = text
        print("Len of uncleaned_text is: ", len(self.uncleaned_text))
        print("len of cleaned text is: ", len(self.text))
        self.k = k
        self.w = w
        if use_rolling_hash == True:
            self.hashes = self.rolling_hash(self.text)
        else:
            self.hashes = self.revised_k_gram(self.text)
        self.fingerprints = self.select_fingerprints(self.hashes, self.w)

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

    # # TODO: decide if this is deprecated (in favour of rolling hash)
    def custom_hash(self, text):
        text = text.encode('utf-8')
        hs = hashlib.md5(text)
        hs = hs.hexdigest()
        hs = int(hs, 16)
        return hs

    def horners_rule(self, some_str):
        length = len(some_str)
        result = ord(some_str[0])
        for i in range(1, length):
            result = (result * 10) + (ord(some_str[i]))
        return result

    def revised_k_gram(self, text):
        '''
        This is the k-gram generator algorithm described in the Extended Winnowing Algorithm paper that accompanies this
        source code. This takes in a piece of text and an integer k that represents how long each K-gram is. This outputs
        the various k-grams as well as their location in the original text. 

        Sample input: "helloworld" , 5 

        Sample Output: [("hello",0) , ("ellow", 1), ("llowo",2), ("lowor",3), ("oworl",4), ("world", 5) ]

        Parameters
        ----------
        text : str
            This is the string that we want to derive k-grams for

        k : int
            This represents how big our k-gram is 

        Returns
            k_grams : list of typles (int, int)
                This represents a list of tuples.
        -------
        '''
        print("--- Using MD5 Hashing ---")
        # Explicit type casting to ensure proper behaviour
        text = str(text)
        k_grams = []
        for start in range(len(text) - self.k + 1):
            # only perform the work necessary if the current character is not a whitespace
            if text[start] != " ":
                end = self.k  
                k_gram = text[start:end]
                k_gram = self.clean_text(k_gram)
                # after cleaning up our k-gram, we can end up with a much smaller string that is below the denoted k-gram length
                # if this is the case, then we will continually add the missing length to the string we are slicing
                while(len(k_gram) < self.k):
                    end = end + (self.k - len(k_gram)) # we will need to add as many letters as are missing from the k-gram
                    k_gram = text[start: end]    
                    k_gram = self.clean_text(k_gram)
                k_grams.append((self.custom_hash(k_gram), start))
        return k_grams

    def rolling_hash(self,text):
        print("--- Using Rolling Hash ---")
        hashes= []
        E = 10 **(self.k - 1)
        text = str(text)
        next_str = text[0:self.k]
        next_hash = self.horners_rule(next_str)
        print(next_str)
        print(next_hash)
        hashes.append(( next_hash, 0, next_str))
        for i in range(0, len(text) - self.k):
            current_str = next_str
            current_hash = next_hash
            if text[i] != " ": 
                # get the new stuff
                next_str = text[i + 1: self.k + i + 1]
                next_hash = ((current_hash - (ord(current_str[0]) * E)) * 10) + ord(next_str[self.k - 1])
                hashes.append((next_hash, i + 1, next_str))
        return hashes

    def select_fingerprints(self, hash_list, w):
        '''
        Parameters
        ----------
        hash_list : list of (int, int)
        
        w : int
            w represents the window size for which we select a rightmost minimum
        
        Returns
        -------
        fingerprints : list of (int, int)
        '''
        fingerprints = []
        min_index = -1
        prev_min_index = -1
        # traverse over the hash_list
        for hash_index in range(len(hash_list) - w +1):
            min_value =  float("inf")
            #traverse over each window
            for window_index in range(hash_index, hash_index + w ):
                if hash_list[window_index][0] <= min_value:
                    min_index = window_index
                    min_value = hash_list[window_index][0]
            # If the minimum value of the previous window is no longer the minimum value
            if min_index != prev_min_index:
                prev_min_index = min_index
                fingerprints.append(hash_list[min_index])
        return fingerprints



