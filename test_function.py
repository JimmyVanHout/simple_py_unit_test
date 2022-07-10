import time

def test_func(func, inputs, expected_outputs):
    print("Testing {func_name}:\n".format(func_name=func.__name__))
    passed_all = True
    test_num = 1
    did_not_pass = []
    for input, expected_output in zip(inputs, expected_outputs):
        start_time = None
        end_time = None
        received_output = None
        print("\tTest " + str(test_num) + "...", end="")
        try:
            start_time = time.process_time()
            received_output = func(input)
            end_time = time.process_time()
        except Exception as e:
            passed_all = False
            did_not_pass.append((test_num, "error", e))
            print("ERROR")
        else:
            if expected_output == received_output:
                total_time = end_time - start_time
                print("PASSED in {time:.2e}s".format(time=total_time))
            else:
                passed_all = False
                did_not_pass.append((test_num, "failed", received_output))
                print("FAILURE")
        test_num += 1
    num_tests = len(inputs)
    num_passed = num_tests - len(did_not_pass)
    print("\n\tPassed {num_passed}/{num_tests} tests".format(num_passed=num_passed, num_tests=num_tests))
    if not passed_all:
        print()
    for test_num, status, value in did_not_pass:
        if status == "error":
            print("\tTest {test_num}: Error: From input {input}, expected {expected_output} but received the following error: {error}".format(test_num=test_num, input=inputs[test_num - 1], expected_output=expected_outputs[test_num - 1], error=value))
        else:
            print("\tTest {test_num}: Failure: From input {input}, expected {expected_output} but received {received_output}".format(test_num=test_num, input=inputs[test_num - 1], expected_output=expected_outputs[test_num - 1], received_output=value))
    if passed_all:
        print("\tPassed all tests for {func_name}\n".format(func_name=func.__name__))
    else:
        print()
    print("Finished testing {func_name}".format(func_name=func.__name__))
    return passed_all
