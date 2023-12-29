Apologies for the ongoing issue. Here's the fixed version of the code:

```python
def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    
    rows = [""] * numRows
    index, step = 0, 1
    
    for char in s:
        rows[index] += char
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
    
    return "".join(rows)


# Unit tests
assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert convert("A", 1) == "A"
assert convert("HELLO", 2) == "HLOLE"
assert convert("WORLD", 5) == "WRLOD"
```