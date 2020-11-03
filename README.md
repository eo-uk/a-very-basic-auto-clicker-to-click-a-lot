# a-very-basic-auto-clicker-to-click-a-lot
A Python auto clicker that starts and stops with a customized hotkey.

## Usage
The default keyboard shortcut for starting/stopping auto clicking is "a, s, d". To use some other shortcut, instantiate the AutoClicker class with your own "shortcut" keyword argument (a list of letters) as below:  

```python
AutoClicker(shortcut=['c', 's', 't', 'm']).run()
```
The above code starts the auto clicker with a shortcut of c + s + t + m.
