# Mainfunction

A very simple utility to allow for main functions to be specified with a decorator instead of if `__name__ == '__main__'`.

It's sugar all the way down.

## Usage:


```
from mainfunction import mainfunction

@mainfunction
def main():
    print "Hello, World."
```

You would write the equivalent program without mainfunction like this:

```
if __name__ == '__main__':
   print "Hello, World."
```

## Notes
  * Main functions must take no arguments
  * Main functions will only execute on import if they're in the `'__main__'` module
  * You may call main functions as regular functions
  * You can define as many main functions as you want, and any that are currently in the `'__main__'` module will execute
  * Having multiple main functions execute from one module will issue a warning (as it's probably a mistake)
