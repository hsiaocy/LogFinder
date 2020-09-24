import dev

# dev.build_test_files()


res_path = r"C:\Users\ALLENHSIAO\SWE\SS-LIB-PYN-Test-MonitorLog\LogSeeker\search_result\\"
test_dir = r"C:\Users\ALLENHSIAO\SWE\SS-LIB-PYN-Test-MonitorLog\LogSeeker\test_dir\\"
dev.findLog('hello', 'world', 'goodbye', folder_path=test_dir, save_path=res_path)