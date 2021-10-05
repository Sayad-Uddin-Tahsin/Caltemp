# -*- mode: python -*-

block_cipher = None


a = Analysis(['Calculator.py'],
             pathex=['C:\\Users\\prana\\AppData\\Local\\Programs\\Python\\Python39'],
             binaries=[],
             datas=[],
             hiddenimports=["PyPI-Browser", "bs4", "beautifulsoup4", "requests", "lxml"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('BMI.ico','F:\\My_Calculator\\Icons\\BMI.ico', "DATA"),
            ('Calculator.ico','F:\\My_Calculator\\Icons\\Calculator.ico', "DATA"),
            ('Info.ico','F:\\My_Calculator\\Icons\\Info.ico', "DATA"),
            ('Scientific Calculator.ico','F:\\My_Calculator\\Icons\\Scientific Calculator.ico', "DATA"),
            ('Splash_Screen.png','F:\\My_Calculator\\Icons\\Splash_Screen.png', "DATA"),
            ("What's new.ico","F:\\My_Calculator\\Icons\\What's new.ico", "DATA")]


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Calculator',
          debug=False,
          strip=False,
          upx=True,
          console=True,
          icon="F:\\My_Calculator\\Icons\\Calculator.ico"
          )