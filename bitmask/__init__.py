class Bitmask(list):
    def __init__(self, *args, columns=None):
        if isinstance(args[0], str):
            self.process_string(args[0], columns=columns)
        else:
            self.columns = columns
            self.string = ''
            for bit in args:
                if bit == True:
                    self.string += '1'
                elif bit == False:
                    self.string += '0'
                else:
                    self.string += 'X'
            super().__init__(args)
        
    def process_string(self, string, columns=None):
        mask_list = []
        for char in string:
            if char == '1':
                mask_list.append(True)
            elif char == '0':
                mask_list.append(False)
            else:
                mask_list.append(None)
        self.__init__(*mask_list, columns=columns)
        
    def __eq__(self, other):
        if isinstance(other, str):
            return self == Bitmask(other)
        elif isinstance(other, list) and not isinstance(other, Bitmask):
            return self == Bitmask(*other)
        elif isinstance(other, Bitmask):
            matches = True
            for bit1, bit2 in zip(self, other):
                if (bit1 is not None) and (bit2 is not None):
                    matches = matches and (bit1 == bit2)
                    if not matches:
                        return matches
        else:
            raise TypeError
        return matches

    def __repr__(self):
        return self.string

    def desc(self):
        if self.columns is not None:
            string = 'if '
            for bit, column in zip(self, self.columns):
                if bit is not None:
                    if bit:
                        bit_str = ''
                    else:
                        bit_str = 'not '
                    string += f'{bit_str}{column} and '
            string = string[:-5]
            return string
        else:
            return self.__repr__()