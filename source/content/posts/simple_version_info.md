title: Access python version info
tags: sys, python version
category: quick_tips
---

import sys

>>> print(sys.version_info)
sys.version_info(major=3, minor=3, micro=0, releaselevel='final', serial=0)

# check if greater than 3.0
if sys.version_info > (3,0):
  print('watch yo syntax homie.')