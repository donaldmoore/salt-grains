# @author donnie moore (donnie.m@gvocom.com)
# @purpose salt grain to detect infected boxes

import os

# real library file size of libkeyutils.so.1.3
REAL_LIBRARY_SIZE = 10192

def ebury_detect():
  # look first in /lib64, if not found it's in /lib
  root_path = 'lib64' if os.path.isfile('/lib64/libkeyutils.so.1.3') else 'lib'
  # grab the file size of the potentially infected library  
  size = os.path.getsize('/%(root_path)s/libkeyutils.so.1.3' % locals())
  
  is_ebury = 'True' if size > REAL_LIBRARY_SIZE else 'False'
  return {'ebury': is_ebury }

if __name__ == '__main__':
  ebury_detect()
