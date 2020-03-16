
import hashlib
from preprocessor import Preprocessor


class WinnowedDoc:
    '''
    WinnowedDoc is a class that takes in a piece of text and generates fingerprints for that text. Fingerprints are numerical
    representations (generated via hashes) of certain pieces of text in the document. 

    Each code file in the corpus of assignments will have to be fingerprinted using this class. 

    Attributes
    ----------
    hashes: list of ints
        The set of all hashed k-grams. 

    fingerprints: list of ints
        A subset of all hashes as chosen by the Winnowing Algorithm. These fingerprints identify a document. These
        fingerprints will be compared against other document fingerprints to see how similar they are to each other.
    '''
    def __init__(self, text, k, w, use_rolling_hash=False):
        self.text = Preprocessor.remove_common_code(Preprocessor.clean_text(text))
        # print("\n\n=========\n Cleaned Code is" + self.text)
        # self.uncleaned_text = text
        # print("Len of uncleaned_text is: ", len(self.uncleaned_text))
        # print("len of cleaned text is: ", len(self.text))
        self.k = k
        self.w = w
        if eval(use_rolling_hash) == True:
            self.hashes = self.rolling_hash(self.text)
        else:
            self.hashes = self.hash_kgram(self.text)
        self.fingerprints = self.select_fingerprints(self.hashes, self.w)

    def custom_hash(self, text):
        '''
        This is just a hash function that will be applied to a  a piece of text. Chose MD5 as per other
        Winnowing Algorithm implementations

        Parameters
        ----------
        text: str
            Input string to be hashed

        Returns
        -------
        hs : int
            a numerical representation of a string generated via hash
        '''
        text = text.encode('utf-8')
        hs = hashlib.md5(text)
        hs = hs.hexdigest()
        hs = int(hs, 16)
        return hs


    # Helper function used by the Rolling Hash Algorithm
    def horners_rule(self, some_str):
        length = len(some_str)
        result = ord(some_str[0])
        for i in range(1, length):
            result = (result * 10) + (ord(some_str[i]))
        return result

    def hash_kgram(self, text):
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
                # k_gram = self.clean_text(k_gram)
                # after cleaning up our k-gram, we can end up with a much smaller string that is below the denoted k-gram length
                # if this is the case, then we will continually add the missing length to the string we are slicing
                while(len(k_gram) < self.k):
                    end = end + (self.k - len(k_gram)) # we will need to add as many letters as are missing from the k-gram
                    k_gram = text[start: end]    
                    # k_gram = self.clean_text(k_gram)
                k_grams.append(self.custom_hash(k_gram))
        return k_grams

    def rolling_hash(self,text):
        '''
        rolling_hash is another means of generating a numerical representation of a document (if you choose not to
        go with the default). This function will return the hashes for all k-grams in o(n) and can be used if 
        computation complexity is a problem

        Parameters
        ----------
        text: str
            The entire document to be generate hashed k-grams

        Returns
        -------
        hashes: list of int
            A list of all hashed k-grams
        '''
        print("--- Using Rolling Hash ---")
        hashes= []
        E = 10 **(self.k - 1)
        text = str(text)
        next_str = text[0:self.k]
        next_hash = self.horners_rule(next_str)
        # print(next_str)
        # print(next_hash)
        # hashes.append(( next_hash, 0, next_str))
        hashes.append(next_hash)
        for i in range(0, len(text) - self.k):
            current_str = next_str
            current_hash = next_hash
            if text[i] != " ": 
                # get the new stuff
                next_str = text[i + 1: self.k + i + 1]
                next_hash = ((current_hash - (ord(current_str[0]) * E)) * 10) + ord(next_str[self.k - 1])
                # hashes.append((next_hash, i + 1, next_str))
                hashes.append(next_hash)
        return hashes

    def select_fingerprints(self, hash_list, w):
        '''
        This helper function takes in a  set of 

        Parameters
        ----------
        hash_list : list of (int, int)
        
        w : int
            w represents the window size for which we select a rightmost minimum
        
        Returns
        -------
        fingerprints : list of int
        '''
        fingerprints = []
        min_index = -1
        prev_min_index = -1
        # traverse over the hash_list
        for hash_index in range(len(hash_list) - w +1):
            min_value =  float("inf")
            #traverse over each window
            for window_index in range(hash_index, hash_index + w ):
                if hash_list[window_index] <= min_value:
                    min_index = window_index
                    min_value = hash_list[window_index]
            # If the minimum value of the previous window is no longer the minimum value
            if min_index != prev_min_index:
                prev_min_index = min_index
                fingerprints.append(hash_list[min_index])
        return fingerprints



