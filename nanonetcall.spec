languages = []
images = []

from PyInstaller.utils.hooks import copy_metadata

a = Analysis(['nanonet/nanonetcall.py'],
             #pathex=['c:\\Python27\\Scripts'],
             hiddenimports=['pyopencl'],
             hookspath=None,
             runtime_hooks=None,
             binaries=[
                 ('nanonetdecode.*', '.'),
                 ('nanonetfilters.*', '.'),
             ],
             datas=[
                 ('nanonet/data/*', 'nanonet/data')
             ] + copy_metadata('pyopencl') 
             )
pyz = PYZ(a.pure)

options = [('u', None, 'OPTION'), ('u', None, 'OPTION'), ('u', None, 'OPTION')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          options,
          languages, # Add them in to collected files
          images, # Same here.
          name='nanonet',
          debug=False,
          strip=None,
          upx=True,
          console=True,
          windowed=False,
)
