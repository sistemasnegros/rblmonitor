# rblmonitor
### Allow watch list ip if they are listed in RBL blacklist.


## Requeriments.
```
pip install rblwatch
```

## Download Binario from windows.
[https://github.com/sistemasnegros/rblmonitor/blob/master/dist/rblmonitor.exe](https://github.com/sistemasnegros/rblmonitor/raw/master/dist/rblmonitor.exe)

## Generate binary for windows pyinstaller.
```
pyinstaller src/main.py --onefile --name rblmonitor --icon=resources\icon.ico
```


#### Example used check ip google.
```
python main.py -i 8.8.8.8
```

#### Example used check ip google with delay 10 seconds.
```
python main.py -i 8.8.8.8 -d 10
```

### Example used with binary in windows.
```
rblmonitor.exe -i 8.8.8.8
```

### Output
```
==================================================
Cancel process Control+C

--- DNSBL Report for 8.8.8.8 ---
TIME:  25 Sep 19 - 08:23:13
==================================================
==================================================
Cancel process Control+C

--- DNSBL Report for 8.8.8.8 ---
TIME:  25 Sep 19 - 08:24:15
==================================================
==================================================
Cancel process Control+C

--- DNSBL Report for 8.8.8.8 ---
TIME:  25 Sep 19 - 08:25:17
==================================================

```
Author
==
- Kevin Franco <sistemasnegros@gmail.com>

License
==
This code is released under the MIT license.


### You like script .
