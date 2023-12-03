import os

class InputParser:
    def getInputPath(scriptpath, filename):
        return os.path.abspath(os.path.join(os.path.dirname(scriptpath),filename))

    def parse_lines(scriptpath : str, inputfilename : str) -> "list[str]":
        inputpath = InputParser.getInputPath(scriptpath, inputfilename)
        with open(inputpath,'r') as file:
            return [line.strip() for line in file.readlines()]
        
    def parse_line(scriptpath : str, inputfilename : str) -> str:
        return InputParser.parse_lines(scriptpath, inputfilename)[0]
