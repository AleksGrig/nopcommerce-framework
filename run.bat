rem chrome
pytest -v --capture=tee-sys -n=2 -m "sanity" --html=reports/report_chrome.html testcases/ --browser chrome
rem pytest -v --capture=tee-sys -n=2 -m "sanity or regression" --html=reports/report_chrome.html testcases/ --browser chrome
rem pytest -v --capture=tee-sys -n=2 -m "sanity and regression" --html=reports/report_chrome.html testcases/ --browser chrome
rem pytest -v --capture=tee-sys -n=2 -m "regression" --html=reports/report_chrome.html testcases/ --browser chrome

rem firefox
rem pytest -v --capture=tee-sys -n=2 -m "sanity" --html=reports/report_firefox.html testcases/ --browser firefox
rem pytest -v --capture=tee-sys -n=2 -m "sanity or regression" --html=reports/report_firefox.html testcases/ --browser firefox
rem pytest -v --capture=tee-sys -n=2 -m "sanity and regression" --html=reports/report_firefox.html testcases/ --browser firefox
rem pytest -v --capture=tee-sys -n=2 -m "regression" --html=reports/report_firefox.html testcases/ --browser firefox

rem edge
rem pytest -v --capture=tee-sys -n=2 -m "sanity" --html=reports/report_edge.html testcases/ --browser edge
rem pytest -v --capture=tee-sys -n=2 -m "sanity or regression" --html=reports/report_edge.html testcases/ --browser edge
rem pytest -v --capture=tee-sys -n=2 -m "sanity and regression" --html=reports/report_edge.html testcases/ --browser edge
rem pytest -v --capture=tee-sys -n=2 -m "regression" --html=reports/report_edge.html testcases/ --browser edge