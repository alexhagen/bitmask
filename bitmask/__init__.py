class Bitmask(list):
    def __init__(self, *args):
        if isinstance(args[0], str):
            self = Bitmask.from_string(args[0])
        super().__init__(*args)
        
    @classmethod
    def from_string(cls, string):
        mask_list = []
        for char in string:
            if int(char) == 1:
                mask_list.append(True)
            elif int(char) == 0:
                mask_list.append(False)
            else:
                mask_list.append(None)
        return Bitmask(*mask_list)
        
    def __equals__(self, other):
        pass