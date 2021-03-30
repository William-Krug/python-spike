# Python Research Spike

## Install

- search for "Python" in vs code
- `install` "Python" by **ms-python.python**
- set the Python interpreter
- run code
  - can click the green "play" button at the top of the editor
  - can right-click the file and choose `Run Python File in Terminal`
  - can open the Command Palette (command + shift + p) and type `Python: Run Python File in Terminal`

## Basic Usage

### Create variable

- variableName = value
- ex. `msg = "hello"`

### Display

- `print(variableName)`
- ex. `print(msg)`

### While Loop

`number = 171`
`while number >= 0:`
`print(number)`
`number -= 3`

### For Loop

`number = 171`
`for i in range(number, 0, -3):`
`print(i)`

### Conditional

`newNumber = 3564`
`if newNumber < 3500:`
`print(newNumber, " is less than 3500")`
`elif newNumber == 3500:`
`print(newNumber, " is equal to 3500")`
`else:`
`print(newNumber, " is greater than 3500")`

### Functions

#### Declaring Functions

`def isEven(number):`
`return number % 2 == 0`

#### Calling Functions

`print('calling isEven() on 42, should return "True":', isEven(even))`
`print('calling isEven() on 69, should return "False":', isEven(odd))`
