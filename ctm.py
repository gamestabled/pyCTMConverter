# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ctm(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = Ctm.Header(self._io, self, self._root)

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x43\x54\x4D\x1B":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x54\x4D\x1B", self.magic, self._io, u"/types/header/seq/0")
            self.title_id = self._io.read_u8le()
            self.version = self._io.read_bytes(20)
            self.clock_init_time = self._io.read_u8le()
            self.movie_id = self._io.read_u8le()
            self.author = (self._io.read_bytes(32)).decode(u"ASCII")
            self.rerecords = self._io.read_u4le()
            self.input_count = self._io.read_u4le()


    class InputChunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pad_and_circle_input = Ctm.Input(self._io, self, self._root)
            self.touch_input = Ctm.Input(self._io, self, self._root)


    class Input(KaitaiStruct):

        class InputType(Enum):
            pad_and_circle = 0
            touch = 1
            accelerometer = 2
            gyroscope = 3
            ir_rst = 4
            extra_hid_response = 5
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(Ctm.Input.InputType, self._io.read_u1())
            _on = self.type
            if _on == Ctm.Input.InputType.gyroscope:
                self._raw_data = self._io.read_bytes(6)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Ctm.Input.AccelerometerAndGyroscope(_io__raw_data, self, self._root)
            elif _on == Ctm.Input.InputType.ir_rst:
                self._raw_data = self._io.read_bytes(6)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Ctm.Input.IrRst(_io__raw_data, self, self._root)
            elif _on == Ctm.Input.InputType.pad_and_circle:
                self._raw_data = self._io.read_bytes(6)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Ctm.Input.PadAndCircle(_io__raw_data, self, self._root)
            elif _on == Ctm.Input.InputType.touch:
                self._raw_data = self._io.read_bytes(6)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Ctm.Input.Touch(_io__raw_data, self, self._root)
            elif _on == Ctm.Input.InputType.accelerometer:
                self._raw_data = self._io.read_bytes(6)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Ctm.Input.AccelerometerAndGyroscope(_io__raw_data, self, self._root)
            elif _on == Ctm.Input.InputType.extra_hid_response:
                self._raw_data = self._io.read_bytes(6)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Ctm.Input.ExtraHidResponse(_io__raw_data, self, self._root)
            else:
                self.data = self._io.read_bytes(6)

        class ExtraHidResponse(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.data = self._io.read_bytes(6)


        class PadAndCircle(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.button_data = Ctm.Input.PadAndCircle.ButtonData(self._io, self, self._root)
                self.circle_pad_x = self._io.read_u2le()
                self.circle_pad_y = self._io.read_u2le()

            class ButtonData(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.unused = self._io.read_bits_int_be(2)
                    self.gpio14 = self._io.read_bits_int_be(1) != 0
                    self.debug = self._io.read_bits_int_be(1) != 0
                    self.y = self._io.read_bits_int_be(1) != 0
                    self.x = self._io.read_bits_int_be(1) != 0
                    self.l = self._io.read_bits_int_be(1) != 0
                    self.r = self._io.read_bits_int_be(1) != 0
                    self.d_down = self._io.read_bits_int_be(1) != 0
                    self.d_up = self._io.read_bits_int_be(1) != 0
                    self.d_left = self._io.read_bits_int_be(1) != 0
                    self.d_right = self._io.read_bits_int_be(1) != 0
                    self.start = self._io.read_bits_int_be(1) != 0
                    self.select = self._io.read_bits_int_be(1) != 0
                    self.b = self._io.read_bits_int_be(1) != 0
                    self.a = self._io.read_bits_int_be(1) != 0



        class AccelerometerAndGyroscope(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.x = self._io.read_u2le()
                self.y = self._io.read_u2le()
                self.z = self._io.read_u2le()


        class Touch(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.x = self._io.read_u2le()
                self.y = self._io.read_u2le()
                self.is_touched = self._io.read_u2le()


        class IrRst(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.data = self._io.read_bytes(6)



    @property
    def inputs(self):
        if hasattr(self, '_m_inputs'):
            return self._m_inputs

        _pos = self._io.pos()
        self._io.seek(256)
        self._m_inputs = []
        for i in range(self.header.input_count):
            self._m_inputs.append(Ctm.InputChunk(self._io, self, self._root))

        self._io.seek(_pos)
        return getattr(self, '_m_inputs', None)


