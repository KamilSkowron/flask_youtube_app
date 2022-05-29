
class TimeVideo():
    def __init__(self, time):
        self.time = time

    def __extract_data(self):
        res = {}
        data = ""
        for i in self.time:
            if i in 'HMS':
                res[i], data = data, ""
            else:
                data += i
        return res


    def repr(self):
        dict_time = self.__extract_data()
        if "H" in dict_time and "M" in dict_time and "S" in dict_time: return f'{dict_time["H"]}:{dict_time["M"]}:{dict_time["S"]}'
        elif "H" in dict_time and "S" in dict_time: return f'{dict_time["H"]}:00:{dict_time["S"]}'
        elif "H" in dict_time and "M" in dict_time: return f'{dict_time["H"]}:{dict_time["M"]}:00'
        elif "H" in dict_time: return f'{dict_time["H"]}:00:00'
        elif "M" in dict_time and "S" in dict_time: return f'{dict_time["M"]}:{dict_time["S"]}'
        elif "M" in dict_time: return f'{dict_time["M"]}:00'
        elif "S" in dict_time: return f'00:{dict_time["S"]}'
