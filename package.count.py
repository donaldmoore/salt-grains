# @author Donald Ray Moore Jr (dmoore@suspectedterrorist.org)
# @purpose salt grain to count redhat packages

import os

def package_count():
  return {'packages': os.popen("rpm -qa | wc -l").readline().rstrip()}

if __name__ == '__main__':
  package_count()
