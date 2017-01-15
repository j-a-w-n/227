echo first test run -- no args supplied
pause 
python command_line_parameters.py
echo second test run -- five args supplied
python command_line_parameters.py 1 2 3 4 5
echo third test run -- too many args supplied
python command_line_parameters.py 1 2 3 4 5 6 7 8 9 10 11
echo fourth test run -- complex strings included
python command_line_parameters.py 1 2 3 "four" "five, six & seven"
echo exit from the test file
