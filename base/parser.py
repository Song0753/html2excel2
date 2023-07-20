
from typing import List, Union, Iterator
from bs4.element import Tag

class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.get_cell_to_dataframe()

    def get_cell_to_dataframe(self):

        '''
            reads file and loads it into respective format
            ready for dumping to file
        '''
        raise NotImplemented

    def _read_file(self):
        """
        returns the data contained in a file
        Returns
        -------
        data : bytes
                File stream
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = f.read()
            return data
        except:
            raise Exception("Error while reading input file")

    def _get_row(self, table: Tag, tags: Union[List, str]) -> Iterator[Tag]:
        '''
            reads all tags present inside a parent tag
            and returns a generator
            Parameters
            ----------
            table : Tag
                    parent tag
            tags : List[str] or str
                    tags to search for in parent tag `table`
            Returns
            -------
            iter_tag : Iterator[Tag]
                    Generator consisting of all occurences of `tags` in `table`
        '''
        row_data = table.find_all(tags)
        for each in row_data:
            yield each           

