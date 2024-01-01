from bizhawk_movie import BizhawkMovie
from typing import BinaryIO, TextIO
from struct import *
import math
import yaml

def clamp(x, minimum, maximum):
    return max(minimum, min(x, maximum))


def setBit(value: int, bitIndex: int) -> int:
    return value | (1 << bitIndex)


def bizhawkCirclePadCoordToCTM(bizhawkCoord: int) -> int:
    if bizhawkCoord < 0:
        ctmCoord = round((bizhawkCoord * 0.9905) - 20.731)
    else:
        ctmCoord = round((bizhawkCoord * 0.9905) + 20.731)

    if abs(ctmCoord) <= 21:
        return 0
    else:
        return clamp(ctmCoord, -154, 154)


def bizhawkButtonDataToCTMButtonData(bizhawkMovieFrame: BizhawkMovie.Frame) -> bytes:
    buttonData1: int = 0
    if bizhawkMovieFrame._r:
        buttonData1 = setBit(buttonData1, 0)
    if bizhawkMovieFrame._l:
        buttonData1 = setBit(buttonData1, 1)
    if bizhawkMovieFrame._x:
        buttonData1 = setBit(buttonData1, 2)
    if bizhawkMovieFrame._y:
        buttonData1 = setBit(buttonData1, 3)
    if bizhawkMovieFrame._debug:
        buttonData1 = setBit(buttonData1, 4)
    if bizhawkMovieFrame._gpio14:
        buttonData1 = setBit(buttonData1, 5)

    buttonData2: int = 0
    if bizhawkMovieFrame._a:
        buttonData2 = setBit(buttonData2, 0)
    if bizhawkMovieFrame._b:
        buttonData2 = setBit(buttonData2, 1)
    if bizhawkMovieFrame._select:
        buttonData2 = setBit(buttonData2, 2)
    if bizhawkMovieFrame._start:
        buttonData2 = setBit(buttonData2, 3)
    if bizhawkMovieFrame._right:
        buttonData2 = setBit(buttonData2, 4)
    if bizhawkMovieFrame._left:
        buttonData2 = setBit(buttonData2, 5)
    if bizhawkMovieFrame._up:
        buttonData2 = setBit(buttonData2, 6)
    if bizhawkMovieFrame._down:
        buttonData2 = setBit(buttonData2, 7)

    return pack("BB", buttonData2, buttonData1)


def getPadAndCircleBytesFromBizhawkMoveFrame(bizhawkMovieFrame: BizhawkMovie.Frame) -> bytes:
    padAndCircleBytes: bytearray = []
    padAndCircleBytes.append(0)
    padAndCircleBytes.extend(bizhawkButtonDataToCTMButtonData(bizhawkMovieFrame))
    padAndCircleBytes.extend(pack("<h", bizhawkCirclePadCoordToCTM(bizhawkMovieFrame._circle_pad_x)))
    padAndCircleBytes.extend(pack("<h", bizhawkCirclePadCoordToCTM(bizhawkMovieFrame._circle_pad_y)))
    return bytes(padAndCircleBytes)


def getTouchBytesFromBizhawkMoveFrame(bizhawkMovieFrame: BizhawkMovie.Frame) -> bytes:
    touchBytes: bytearray = []
    touchBytes.append(1)
    touchBytes.extend(pack("<H", bizhawkMovieFrame._touch_x))
    touchBytes.extend(pack("<H", bizhawkMovieFrame._touch_y))
    touchBytes.extend(pack("?x", bizhawkMovieFrame._touch))
    return bytes(touchBytes)


def getInputChunkFromBizhawkMovieFrame(bizhawkMovieFrame: BizhawkMovie.Frame) -> bytes:
    inputChunk: bytearray = []
    inputChunk.extend(getPadAndCircleBytesFromBizhawkMoveFrame(bizhawkMovieFrame))
    inputChunk.extend(getTouchBytesFromBizhawkMoveFrame(bizhawkMovieFrame))
    return bytes(inputChunk)


def getInputInstancesFromBizhawkMovie(bizhawkMovie: BizhawkMovie) -> (int, bytes):
    inputInstances: bytearray = []

    INPUTS_PER_SECOND = 234
    FRAMES_PER_SECOND = 59.83122493939037

    totalInputsRaw: float = 0.0
    numInputsProduced: int = 0
    frameNum: int = 0

    for bizhawkMovieFrame in bizhawkMovie._frames:
        totalInputsRaw = totalInputsRaw + (INPUTS_PER_SECOND / FRAMES_PER_SECOND)
        numInputsByEndOfFrame: int = math.floor(totalInputsRaw + 0.00201) # magic adjustment factor that helps it line up in some near misses
        frameNum = frameNum + 1
        while numInputsProduced < numInputsByEndOfFrame:
            inputInstances.extend(getInputChunkFromBizhawkMovieFrame(bizhawkMovieFrame))
            numInputsProduced = numInputsProduced + 1

    return (numInputsProduced, bytes(inputInstances))


def createCtmHeader(title_id: int, version: bytes, clock_init_time: int, movie_id: int,
                    author: bytes, rerecords: int, input_count: int) -> bytes:
    return pack("<4sQ20sQQ32sII168x", b"CTM\x1B", title_id, version, clock_init_time,
                movie_id, author, rerecords, input_count)


def createCtmHeaderFromConfig(inFile: TextIO, input_count: int) -> bytes:
    config = yaml.safe_load(inFile)
    return createCtmHeader(config["title_id"], config["version"], config["clock_init_time"],
                           config["movie_id"], config["author"].encode('ascii'), config["rerecords"],
                           input_count)


def writeCtmFromBizhawkMovie(bizhawkMovie: BizhawkMovie, configFile: TextIO, outFile: BinaryIO) -> None:
    (inputCount, inputInstances) = getInputInstancesFromBizhawkMovie(bizhawkMovie)
    header = createCtmHeaderFromConfig(configFile, inputCount)
    outFile.write(header)
    outFile.write(inputInstances)

