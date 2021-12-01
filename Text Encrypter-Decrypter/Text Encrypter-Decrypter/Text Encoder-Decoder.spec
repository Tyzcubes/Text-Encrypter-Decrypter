# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\Tyler Floyd\\Desktop\\Text Encrypter-Decrypter\\Text Encoder-Decoder.py'],
             pathex=['C:\\Users\\Tyler Floyd\\Desktop\\Text Encrypter-Decrypter'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Text Encoder-Decoder',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='C:\\Users\\Tyler Floyd\\Desktop\\Text Encrypter-Decrypter\\Main\\index.ico.ico')
