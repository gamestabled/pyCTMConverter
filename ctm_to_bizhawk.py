from ctm import Ctm
from bizhawk_movie import BizhawkMovie

def ctmInputChunkToBizhawkMovieFrame(ctmInputChunk: Ctm.InputChunk) -> BizhawkMovie.Frame:
    bizhawkMovieFrame = BizhawkMovie.Frame()
    bizhawkMovieFrame._circle_pad_x = ctmInputChunk.pad_and_circle_input.data.circle_pad_x
    bizhawkMovieFrame._circle_pad_y = ctmInputChunk.pad_and_circle_input.data.circle_pad_y
    bizhawkMovieFrame._touch_x = ctmInputChunk.touch_input.data.x
    bizhawkMovieFrame._touch_y = ctmInputChunk.touch_input.data.y
    bizhawkMovieFrame._a = ctmInputChunk.pad_and_circle_input.data.button_data.a
    bizhawkMovieFrame._b = ctmInputChunk.pad_and_circle_input.data.button_data.b
    bizhawkMovieFrame._x = ctmInputChunk.pad_and_circle_input.data.button_data.x
    bizhawkMovieFrame._y = ctmInputChunk.pad_and_circle_input.data.button_data.y
    bizhawkMovieFrame._up = ctmInputChunk.pad_and_circle_input.data.button_data.d_up
    bizhawkMovieFrame._down = ctmInputChunk.pad_and_circle_input.data.button_data.d_down
    bizhawkMovieFrame._left = ctmInputChunk.pad_and_circle_input.data.button_data.d_left
    bizhawkMovieFrame._right = ctmInputChunk.pad_and_circle_input.data.button_data.d_right
    bizhawkMovieFrame._l = ctmInputChunk.pad_and_circle_input.data.button_data.l
    bizhawkMovieFrame._r = ctmInputChunk.pad_and_circle_input.data.button_data.r
    bizhawkMovieFrame._start = ctmInputChunk.pad_and_circle_input.data.button_data.start
    bizhawkMovieFrame._select = ctmInputChunk.pad_and_circle_input.data.button_data.select
    bizhawkMovieFrame._touch = ctmInputChunk.touch_input.data.is_touched
    return bizhawkMovieFrame
