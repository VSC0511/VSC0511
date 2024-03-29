class CsvFileWriter:
    def __init__(self, file_name: str,
                 headers: list,
                 *rows: list
                ) -> None:
        
        self.file_name = file_name
        self.headers = headers
        self.rows = rows
        
        
    def __check_length(self) -> None:
        """_summary_

        Raises:
            ValueError: if lengths of the lists are diifferent
        """
        
        all_length = [len(l) for l in self.rows]
        if max(all_length) != min(all_length):
            raise ValueError('Length is different')
        
    
    def clean_file(self) -> None:
        """_summary_
        
        Point: eraise all the information in the file
        """
        
        open(self.file_name, 'w').close()
        
        
    def csv_file_handler(self, mode: str='w') -> None:
        """_summary_

        Args:
            mode (str, optional): _description_. Defaults to 'w'.
            In default file mode is 'W'-write 
            but we can change it to any available modes
        
        Description:
            Sorts lists in a way to write data to the file
            formats the data to allow pandas to understand the csv file
        """
        
        self.__check_length()
        data = [] # Future data
        
        list_to_add = []

        # Prepares data for future writing
        for index in range(len(self.rows[0])):
            for value in self.rows:
                list_to_add.append(value[index])
            else:
                data.append(list_to_add)
                list_to_add = []

        
        with open(self.file_name, mode) as csvfile:
            for indx_one, header in enumerate(self.headers):
                if indx_one == len(self.headers)-1:
                    csvfile.write(f"{header}\n")

                else:
                    csvfile.write(f"{header},")
            
            for preplist in data:
                for indx_two, val in enumerate(preplist):
                    if indx_two == len(preplist)-1:
                        csvfile.write(f"{val}\n")
                    
                    else:
                        csvfile.write(f"{val},")


