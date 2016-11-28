"""
Copyright 2016 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import time
import win32ui

class WptRecord:
  def __init__(self):
    self.window = None
    self.UWM_PREPARE = (0x8000 + 0)
    self.UWM_START   = (0x8000 + 1)
    self.UWM_STOP    = (0x8000 + 2)
    self.UWM_PROCESS = (0x8000 + 3)
    self.UWM_DONE    = (0x8000 + 4)

  def Prepare(self, test_info):
    # Todo: launch the recorder process
    # Wait for the recorder window to be available for 30 seconds
    start = time.time()
    while self.window is None and time.time() - start < 30:
      try:
        self.window = win32ui.FindWindow("wptRecord", "wptRecord")
      except:
        time.sleep(0.1)

    if self.window is not None:
      try:
        self.window.SendMessage(self.UWM_PREPARE, 0, 0)
      except:
        pass

  def Start(self):
    if self.window is not None:
      try:
        self.window.PostMessage(self.UWM_START, 0, 0)
      except:
        pass

  def Stop(self):
    if self.window is not None:
      try:
        self.window.SendMessage(self.UWM_STOP, 0, 0)
      except:
        pass

  def Process(self):
    if self.window is not None:
      try:
        self.window.SendMessage(self.UWM_PROCESS, 0, 0)
      except:
        pass

  def Done(self):
    if self.window is not None:
      try:
        self.window.SendMessage(self.UWM_DONE, 0, 0)
      except:
        pass