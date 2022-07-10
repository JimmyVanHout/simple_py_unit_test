# Simple Python Unit Test

## About

> **Important**: This program was mainly created as an academic project and should **not** typically be used over more established and comprehensive unit testing programs such as the built-in Python unit testing module [unittest](https://docs.python.org/3/library/unittest.html) or [pytest](https://docs.pytest.org/).

This program facilitates the testing of Python functions. The function `test_function.test_func` tests a specified function, given the inputs to that function and the expected outputs. It then produces the test results in a nicely formatted way.

## Installation

Clone the repository from [GitHub](https://github.com/JimmyVanHout/simple_py_unit_test):

```
git clone https://github.com/JimmyVanHout/simple_py_unit_test.git
```

## Usage

`test_function.test_func` takes as arguments the function to test, a list of the inputs, and a list of the expected outputs. It then prints the test results to standard output. For example:

```
import test_function

def f(x):
    return x + 1

def test_f(function):
    inputs = [1, 2, 3]
    expected_outputs = [2, 3, 4]
    test_function.test_func(function, inputs, expected_outputs)

test_f(f)
```

The output looks like this:

```
Testing f:

	Test 1...PASSED in 1.46e-06s
	Test 2...PASSED in 7.19e-07s
	Test 3...PASSED in 6.14e-07s

	Passed 3/3 tests
	Passed all tests for f

Finished testing f
```

Another example is in the `test` directory, where `tested.py` is the file containing the functions that will be tested and `test_tested.py` is the file that will test them. The expected program output is in `test/test_output.txt`.

Note that the `import_module` helper function is provided in `import_helper.py` to import the `test_function` module (or any module) from wherever it is located on the filesystem. See the example in the `test` directory for usage (the function is reproduced rather than imported in `test_tested.py` in order to import the `test_function` module).

## Testing the Unit Testing Program

To test the unit testing program itself and see an example usage, run:

```
python3 test/test_tested.py
```

The expected output of the test program is in `test/test_output.txt`. To see the differences between the program's output to standard output and `test_output.txt`, run:

```
python3 test/test_tested.py | diff - test/test_output.txt
```

The only differences between the program's output to standard output and `test_output.txt` should be the execution times of the functions tested by `test_tested.py`:

```
3,5c3,5
< 	Test 1...PASSED in 1.63e-06s
< 	Test 2...PASSED in 7.50e-07s
< 	Test 3...PASSED in 6.54e-07s
---
> 	Test 1...PASSED in 1.40e-06s
> 	Test 2...PASSED in 7.42e-07s
> 	Test 3...PASSED in 6.16e-07s
```

## Support

You can file an issue on [GitHub](https://github.com/JimmyVanHout/simple_py_unit_test/issues).
