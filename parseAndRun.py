import csv
import time

from puzzleSolver import solve_puzzle


def parse_puzzle_file(file_path):
    # Parse puzzle tests file to extract all test cases.
    with open(file_path, 'r') as file:
        content = file.read()

    # Splitting sections by the hash line
    tests_raw = content.split("##########################")
    tests = []

    for test in tests_raw:
        if test.strip():
            lines = [line.strip() for line in test.split("\n") if line.strip()]
            test_details = {}
            for line in lines:
                if '=' in line:
                    key, value = line.split('=')
                    key = key.strip().lower()
                    value = value.strip()
                    if key == 'init':
                        value = eval(value)
                    else:
                        value = int(value)
                    test_details[key] = value
            if test_details:
                tests.append(test_details)

    return tests


def solve_all_tests(test_cases):
    # Solve all test cases using the A* algorithm, display results and write it to CSV.
    for index, test in enumerate(test_cases):
        initial_state = test["init"]
        full = test["full"]
        size = test["size"]
        start_time = time.time()  # Start timing here
        num_moves, num_tries, solution_path = solve_puzzle(initial_state, size)
        end_time = time.time()  # End timing here
        execution_time = end_time - start_time
        print(f"Test Case Index: {index}")
        print(f"Number of Moves: {num_moves}")
        print(f"Total Checks: {num_tries}")
        # print(f"Solution Path: {solution_path}")
        print(f"Execution Time: {execution_time}")
        print("\n" + "=" * 50 + "\n")  # Separator between test results

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([index, num_moves, num_tries,  execution_time, solution_path])
    return


csv_file = 'puzzle_results.csv'
# Make CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Test ID", "Moves Count", "Visited States Count", "Execution Time", "Path"])

# Solving all parsed tests
test_file_name = 'Instances.txt'
tests = parse_puzzle_file(test_file_name)
solve_all_tests(tests)
