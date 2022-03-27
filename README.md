# Puzzling Tools
Requires python 3

## Character Math
### Addition
Add letters by numeric value with wrapping.
Options include 
- (default) `--char` or `-c` for summing all chars entered
- `--word` or `-w` for batching addition for two strings of chars
- `--file` or `-f` for batching addition for two files of chars

```
./add.py a b
>>> C
```
```
./add.py char ac
>>> D
```
```
./add.py char abcde
>>> O
```
```
./add.py --word <string1> <string2>
```
```
./add.py --file <file1> <file2>
```

### Subtraction
Subtract letters by numeric value with wrapping. This is absolute value of the difference, and does not wrap to negative values.
Options include 
- (default) `--char` or `-c` for getting the difference of the next two arguments
- `--word` or `-w` for batching subtraction for two strings of chars
- `--file` or `-f` for batching subtraction for two files of chars

```
./sub.py z x
>>> B
```
```
./sub.py --word <string1> <string2>
```
```
./sub.py --file <file1> <file2>
```