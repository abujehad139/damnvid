import os
import shutil
import re

while not os.path.lexists('./DamnVid.py'):
    os.chdir('./../')
def shazarr(f):
    print 'Cleaning up:',f
    if os.path.isdir(f):
        shutil.rmtree(f)
    else:
        os.remove(f)
def cleanDir(d,deletables):
    if d[-1]==os.sep:
        d=d[0:-1]
    for i in deletables:
        if i.find('*')!=-1:
            r=re.compile(re.escape(i).replace('\\*','.*'),re.IGNORECASE)
            for f in os.listdir(d):
                if r.match(f):
                    shazarr(d+os.sep+f)
        elif os.path.lexists(d+os.sep+i):
            shazarr(d+os.sep+i)
cleanDir('.',['COPYING','DamnVid.exe.manifest','required-files.txt','package','DamnVid.app','*.module.damnvid','*.so','*.so.*','library.zip','py','DamnVid'])
cleanDir('./modules',['*.module.damnvid'])