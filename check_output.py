import subprocess
from collections import defaultdict

cmd = ["pytest"]

proc = subprocess.Popen(cmd, text=True, stdout=subprocess.PIPE)
while True:
    line = proc.stdout.readline()
    if not line:
        break
    print(line)


#output = subprocess.check_output(["pytest", "--co", "-q"], text=True)
#print(output)

#tests: dict[str, list] = defaultdict(list)
#number_of_tests = 0
#for line in output.split("\n"):
    #if ".py::" in line:
        #test_file, test_name = line.split("::")
        #tests[test_file].append(test_name)
    #if "tests collected in" in line:
        #number_of_tests = int(line.split()[0])

#print(tests)
#print(f"Number of tests found: {number_of_tests}")