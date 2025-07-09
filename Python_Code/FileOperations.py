class FileOperations:
    '''This class has __init__ method to store the filepath to read the file from
    and has methods to read data from the file
    '''
    '''This method stores the filepath attribute'''
    def __init__(self, filepath):
        self.filepath=filepath
    
    '''this method reads data from file in multiple ways.'''
    def readdata(self):
        with open(self.filepath) as fileobj:
            '''this way it stores all the contents of file into single variable which can be printed into console using variable name. note the "read()" method'''
            contents= fileobj.read()
            print(contents)
            fileobj.seek(0)
            '''this way we can read line by line from the file and perform operations on the lines.'''
            for line in fileobj:
                print(line.rstrip())
            '''this way we can read lines and store them into a list so that we can work with the list later on even when with block is closed. note the "readlines()" method.'''
            fileobj.seek(0)
            content_list=fileobj.readlines()
            '''this way, we can use enumerate iterable on the fileobject which allows us to see line numbers and perform operations line wise.'''
            for linenum, line in enumerate(fileobj, start=1):
                if 'Medicare' in line:
                    print(f'line num: {linenum}')
                else:
                    continue
        '''this is different from previous way is here we are enumerating over list instead of directly on file object.'''
        for lnum, l in enumerate(content_list, start=1):
            if 'Medicare' in l:
                    print(f'line num: {lnum}')
            else:
                continue
        '''here we are using list comprehension to iterate over list, apply condition of searching a string in each line, applying expression of replacing string and storing the results into another list.'''
        medicare_elements = [c.replace('Medicare','SNAP') for c in content_list if 'Medicare' in c]
        print(medicare_elements)
                    
                    
p='C:/Users/bgurbuxsinghani/healthcare.csv'
f= FileOperations(p)
f.readdata()



