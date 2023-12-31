from typing import List, TextIO, Self

class BizhawkMovie:
    def __init__(self) -> None:
        self._frames: List[BizhawkMovie.Frame] = []


    def printTo(self, outFile: TextIO) -> None:
        outFile.write("[Input]\n")
        outFile.write("LogKey:#Circle Pad X|Circle Pad Y|C-Stick X|C-Stick Y|Touch X|Touch Y|Tilt X|Tilt Y|A|B|X|Y|Up|Down|Left|Right|L|R|Start|Select|Debug|GPIO14|ZL|ZR|Touch|Tilt|Reset|\n")
        for frame in self._frames:
            frame.printTo(outFile)
        outFile.write("[/Input]\n")


    def readFromFile(self, inFile: TextIO) -> None:
        lines = inFile.readlines()
        # assume first two lines and last line dont matter
        frameLines = lines[2:-1]
        for frameLine in frameLines:
            frame = BizhawkMovie.Frame()
            frame.readFromStr(frameLine)
            self.addFrame(BizhawkMovie.Frame().readFromStr(frameLine))


    def addFrame(self, frame: 'BizhawkMovie.Frame') -> None:
        self._frames.append(frame)


    class Frame:
        def __init__(self) -> None:
            self._circle_pad_x : int = 0
            self._circle_pad_y : int = 0
            self._c_stick_x : int = 0
            self._c_stick_y : int = 0
            self._touch_x : int = 0
            self._touch_y : int = 0
            self._tilt_x : int = 0
            self._tilt_y : int = 0
            self._a : bool = False
            self._b : bool = False
            self._x : bool = False
            self._y : bool = False
            self._up : bool = False
            self._down : bool = False
            self._left : bool = False
            self._right : bool = False
            self._l : bool = False
            self._r : bool = False
            self._start : bool = False
            self._select : bool = False
            self._debug : bool = False
            self._gpio14 : bool = False
            self._zl : bool = False
            self._zr : bool = False
            self._touch : bool = False
            self._tilt : bool = False
            self._reset : bool = False


        def coordString(self, coord: int) -> str:
            return "{0:5d}".format(coord)


        def buttonString(self, pressed: bool, symbol: str) -> str:
            if pressed:
                return symbol
            else:
                return '.'


        def printTo(self, outFile: TextIO) -> None:
            format_str = \
                f"|"\
                f"{self.coordString(self._circle_pad_x)},"\
                f"{self.coordString(self._circle_pad_y)},"\
                f"{self.coordString(self._c_stick_x)},"\
                f"{self.coordString(self._c_stick_y)},"\
                f"{self.coordString(self._touch_x)},"\
                f"{self.coordString(self._touch_y)},"\
                f"{self.coordString(self._tilt_x)},"\
                f"{self.coordString(self._tilt_y)},"\
                f"{self.buttonString(self._a, 'A')}"\
                f"{self.buttonString(self._b, 'B')}"\
                f"{self.buttonString(self._x, 'X')}"\
                f"{self.buttonString(self._y, 'Y')}"\
                f"{self.buttonString(self._up, 'U')}"\
                f"{self.buttonString(self._down, 'D')}"\
                f"{self.buttonString(self._left, 'L')}"\
                f"{self.buttonString(self._right, 'R')}"\
                f"{self.buttonString(self._l, 'l')}"\
                f"{self.buttonString(self._r, 'r')}"\
                f"{self.buttonString(self._start, 'B')}"\
                f"{self.buttonString(self._select, 's')}"\
                f"{self.buttonString(self._debug, 'X')}"\
                f"{self.buttonString(self._gpio14, 'X')}"\
                f"{self.buttonString(self._zl, 'z')}"\
                f"{self.buttonString(self._zr, 'z')}"\
                f"{self.buttonString(self._touch, 'T')}"\
                f"{self.buttonString(self._tilt, 't')}"\
                f"{self.buttonString(self._reset, 'R')}"\
                f"|\n"
            outFile.write(format_str)

        def readFromStr(self, string: str) -> Self:
            #remove whitespace and surrounding pipes
            string = string.strip()[1:-1]
            dataList = string.split(',')
            self._circle_pad_x = int(dataList[0])
            self._circle_pad_y = int(dataList[1])
            self._c_stick_x = int(dataList[2])
            self._c_stick_y = int(dataList[3])
            self._touch_x = int(dataList[4])
            self._touch_y = int(dataList[5])
            self._tilt_x = int(dataList[6])
            self._tilt_y = int(dataList[7])
            buttonChars = dataList[8]
            self._a = (buttonChars[0] != '.')
            self._b = (buttonChars[1] != '.')
            self._x = (buttonChars[2] != '.')
            self._y = (buttonChars[3] != '.')
            self._up = (buttonChars[4] != '.')
            self._down = (buttonChars[5] != '.')
            self._left = (buttonChars[6] != '.')
            self._right = (buttonChars[7] != '.')
            self._l = (buttonChars[8] != '.')
            self._r = (buttonChars[9] != '.')
            self._start = (buttonChars[10] != '.')
            self._select = (buttonChars[11] != '.')
            self._debug = (buttonChars[12] != '.')
            self._gpio14 = (buttonChars[13] != '.')
            self._zl = (buttonChars[14] != '.')
            self._zr = (buttonChars[15] != '.')
            self._touch = (buttonChars[16] != '.')
            self._tilt = (buttonChars[17] != '.')
            self._reset = (buttonChars[18] != '.')
            return self
