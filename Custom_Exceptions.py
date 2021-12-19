class EmptyFileException(Exception):
    """
    Here exception is raised if an empty resource file is provided as input.
    """

    def __init__(self,message=" The input file is empty or the object repository worksheet does not have any content"):
        self.message=message
        super().__init__(self.message)