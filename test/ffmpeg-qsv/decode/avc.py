###
### Copyright (C) 2018-2019 Intel Corporation
###
### SPDX-License-Identifier: BSD-3-Clause
###

from ....lib import *
from ..util import *
from .decoder import DecoderTest

spec = load_test_spec("avc", "decode")

class default(DecoderTest):
  def before(self):
    vars(self).update(
      caps      = platform.get_caps("decode", "avc"),
      ffdecoder = "h264_qsv",
      # default metric
      metric    = dict(type = "ssim", miny = 1.0, minu = 1.0, minv = 1.0),
    )
    super(default, self).before()

  @slash.requires(*platform.have_caps("decode", "avc"))
  @slash.requires(*have_ffmpeg_decoder("h264_qsv"))
  @slash.parametrize(("case"), sorted(spec.keys()))
  def test(self, case):
    vars(self).update(spec[case].copy())
    vars(self).update(case = case)
    self.decode()
