# @author donnie moore (donnie.m@gvocom.com)
# @purpose salt grain to detect infected boxes

import os

def ebury_detect():
  root_path = 'lib64' if os.path.isfile('/lib64/libkeyutils.so.1.3') else 'lib'
  size = os.path.getsize('/%(root_path)s/libkeyutils.so.1.3' % locals())
  is_ebury = 'True' if size > 32768 else 'False'
  return {'ebury': is_ebury }

if __name__ == '__main__':
  ebury_detect()
