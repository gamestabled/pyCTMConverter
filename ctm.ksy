meta:
  id: ctm
  file-extension: ctm
  endian: le
seq:
  - id: header
    type: header
instances:
  inputs:
    pos: 0x100
    type: input_chunk
    repeat: expr
    repeat-expr: header.input_count
types:
  header:
    seq:
      - id: magic
        contents: ['CTM', 0x1B]
      - id: title_id
        type: u8
      - id: version
        size: 0x14
      - id: clock_init_time
        type: u8
      - id: movie_id
        type: u8
      - id: author
        type: str
        encoding: ASCII
        size: 0x20
      - id: rerecords
        type: u4
      - id: input_count # divided by 2?
        type: u4
  
  input_chunk:
    seq:
      - id: pad_and_circle_input # always exists first
        type: input
      - id: touch_input # always exists second
        type: input
      # - id: other_inputs # other inputs can follow, but skipping those for now
  
  input:
    seq:
      - id: type
        type: u1
        enum: input_type
      - id: data
        type:
          switch-on: type
          cases:
            'input_type::pad_and_circle': pad_and_circle
            'input_type::touch': touch
            'input_type::accelerometer': accelerometer_and_gyroscope
            'input_type::gyroscope': accelerometer_and_gyroscope
            'input_type::ir_rst': ir_rst
            'input_type::extra_hid_response': extra_hid_response
        size: 6
    enums:
      input_type:
        0: pad_and_circle
        1: touch
        2: accelerometer
        3: gyroscope
        4: ir_rst
        5: extra_hid_response
    types:
      pad_and_circle:
        seq:
          - id: button_data
            type: button_data
          - id: circle_pad_x
            type: u2
          - id: circle_pad_y
            type: u2
        types:
          button_data:
            meta:
              bit-endian: be
            seq:
              - id: unused
                type: b2
              - id: gpio14
                type: b1
              - id: debug
                type: b1
              - id: y
                type: b1
              - id: x
                type: b1
              - id: l
                type: b1
              - id: r
                type: b1
              - id: d_down
                type: b1
              - id: d_up
                type: b1
              - id: d_left
                type: b1
              - id: d_right
                type: b1
              - id: start
                type: b1
              - id: select
                type: b1
              - id: b
                type: b1
              - id: a
                type: b1
      touch: 
        seq:
          - id: x
            type: u2
          - id: y
            type: u2
          - id: is_touched
            type: u2
      accelerometer_and_gyroscope:
        seq:
          - id: x
            type: u2
          - id: y
            type: u2
          - id: z
            type: u2
      ir_rst:
        seq:
          - id: data
            size: 6
      extra_hid_response:
        seq:
          - id: data
            size: 6
