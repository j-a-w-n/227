@echo When you continue you will see the first test run ...
@pause
python converter.py
@echo When you continue you will see the second test run ...
@pause
python converter.py time
@echo When you continue you will see the third test run ...
@pause
python converter.py temp 100
@echo When you continue you will see the fourth test run ...
@pause
python converter.py ftemp 100 200
@echo When you continue you will see the fifth test run ...
python converter.py ftemp 100
@echo When you continue you will see the sixth test run ...
python converter.py ctemp -100
@echo When you continue you will see the seveth test run ...
python converter.py ctemp -40.00
@echo When you continue you will see the eigth test run ...
python converter.py ftemp 68.123415234
@echo When you continue you will see the ninth test run ...
python converter.py time 1000
@echo When you continue you will see the tenth test run ...
python converter.py time 180
@echo When you continue this batch file of test runs will terminate ...
@pause
