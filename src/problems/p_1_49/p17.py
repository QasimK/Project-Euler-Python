'''
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words, how many letters
would be used?

NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two)contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance
with British usage.
'''

def get_word_of_number(number):
    """Return the word equivalent of a number from 0-999999"""
    
    assert number >= 0 and number <= 999999
    
    hundred_word = "hundred"
    thousand_word = "thousand"
    
    #For splitting the problem up
    def get_into_columns(number):
        """Split a number into columns, like "thousands", "hundreds",
        "tens", "units"
        
        Returns a dictionary of those columns"""
        
        assert number >= 0 and number <= 999999
        
        strnum = str(number)
        columns = {}
        
        #Start from the units (end of string)
        for i, char in enumerate(reversed(strnum)):
            if i == 0:
                #Units
                columns["units"] = int(char)
            elif i == 1:
                #Tens
                columns["tens"] = int(char)
            elif i == 2:
                #Hundreds
                columns["hundreds"] = int(char)
            elif i == 3 or i == 4 or i == 5:
                #Thousands (1 thousand, 10 thousand, 100 thousand)
                if i == 3:
                    columns["thousands"] = int(char)
                else:
                    columns["thousands"] = int(char+str(columns["thousands"]))
        
        return columns
    
    
    def get_word_for_little(number):
        """Return the word for a number less than 100"""
        assert number >= 0 and number < 100
        singles = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
        }
        teens = {
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
        }
        doubles = {
            2: 'twenty',
            3: 'thirty',
            4: 'forty',
            5: 'fifty',
            6: 'sixty',
            7: 'seventy',
            8: 'eighty',
            9: 'ninety',
        }
        
        #Number 0-9
        if number in singles:
            return singles[number]
        #Number 10-19
        if number in teens:
            return teens[number]
        #Number 20-90 (multiples of ten)
        if number/10 in doubles:
            return doubles[number/10]
        
        #Remaining numbers 21-99
        columns = get_into_columns(number)
        tens = columns["tens"]
        units = columns["units"]
        
        final_string = ""
        
        final_string += doubles[tens]
        final_string += "-"
        final_string += singles[units]
        
        return final_string


    #If little
    if number < 100:
        return get_word_for_little(number)
    
    #Big, deal with each part seperately
    split = get_into_columns(number)
    final_string = ""
    
    is_big_part = False
    is_thousands = False
    #Thousands part
    if "thousands" in split:
        thousands_part_number = split["thousands"]
        thousands_number = (get_word_for_little(thousands_part_number) +
                            " " + thousand_word)
        final_string += thousands_number
        is_big_part = True
        is_thousands = True
    
    if "hundreds" in split:
        hundreds_part_number = split["hundreds"]
        if hundreds_part_number != 0:
            hundreds_number = (get_word_for_little(hundreds_part_number)
                               + " " + hundred_word)
            
            if is_thousands:
                final_string += " "
            
            final_string += hundreds_number
            is_big_part = True
    
    #Get the small number part
    small_number_part = int(str(split["tens"]) + str(split["units"]))
    if small_number_part != 0:
        small_number = get_word_for_little(small_number_part)
        
        if is_big_part:
            final_string += " and "
        
        final_string += small_number
    
    return final_string

if __name__ == '__main__':
    #Testing:
    #===========================================================================
    # def test_num(number):
    #    print(number, get_word_of_number(number))
    # test_num(0)
    # test_num(5)
    # test_num(11)
    # test_num(15)
    # test_num(90)
    # test_num(50)
    # test_num(77)
    # test_num(100)
    # test_num(250)
    # test_num(999)
    # test_num(1000)
    # test_num(10000)
    # test_num(1245)
    # test_num(19999)
    # test_num(999999)
    #===========================================================================
    
    words = []
    for number in range(1, 1001):
        the_word = get_word_of_number(number)
        important_chars = the_word.replace(" ", "")
        important_chars = important_chars.replace("-", "")
        words.append(important_chars)
    
    #Count the characters
    n = 0
    for word in words:
        n += len(word)
    
    print(n)

