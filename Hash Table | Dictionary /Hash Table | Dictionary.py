def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
''' Returns a list of grouped anagrams.
Args:
    strs (list): List of anagram words
    
'''
    # Sort the list of anagram words to be used as the key to dictionary
    sorted_strs = list(map(lambda x: "".join(sorted(x)),strs))
    
    # Dictionary of grouped anagrams 
    groups = {}

    # Loop through sorted strings of anagram
    for idx,val in enumerate(sorted_strs):

        # Append the word to the sorted anagram as key
        try:
            groups[val].append(strs[idx])

        # If not, then make the key and initialize empty list as value
        except KeyError:
            groups[val] = []
            groups[val].append(strs[idx])

  # Returning list of grouped anagrams
  return [val for key, val in groups.items()]
