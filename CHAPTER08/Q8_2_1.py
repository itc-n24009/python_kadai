import pathlib
p = pathlib.Path(".")
for pf inn p.iterdir():
    if pf.is_file():
        print(str(pf))
#カレントディレクトリにあるファイルを表示する。
