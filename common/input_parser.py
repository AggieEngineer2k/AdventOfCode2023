import os

class InputParser:
    def getInputPath(scriptpath, filename):
        return os.path.abspath(os.path.join(os.path.dirname(scriptpath),filename))

    def parse_line(scriptpath : str, inputfilename : str) -> str:
        inputpath = InputParser.getInputPath(scriptpath, inputfilename)
        with open(inputpath,'r') as file:
            return file.readline().strip()

    def parse_lines(scriptpath : str, inputfilename : str) -> "list[str]":
        inputpath = InputParser.getInputPath(scriptpath, inputfilename)
        with open(inputpath,'r') as file:
            return [line.strip() for line in file.readlines()]