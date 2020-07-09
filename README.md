# MS-WinX-ProductKey-Calculator
This Project contains information and tools to extract Windows 10 Keys from the encrypted DigitalProductId


The example implementation will be in python. Feel free to add implementations in other languages or improved ones.

## Usage

```
python WinXKeyDecryptor_productID.py
```

This will return the currently activated key.  
However there may be 'older' keys in the registry in a different location.  



###### To validate your key with official tools
```
slmgr /dli
```
This will return the last block (last 5 figures) of the used key.
