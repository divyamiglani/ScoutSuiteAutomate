import sys
import os
import json

report_root = 'scoutsuite-report'
report_path = os.path.join(report_root,'scoutsuite-results')
json_reports = []
break_level = 'danger'
   
def extract_result():
    for file in os.listdir(report_path):
        if(file.startswith('scoutsuite_results_aws') and file.endswith('.js')):
            file_path=os.path.join(report_path,file)
            with open(file_path) as f:
                json_payload_str = f.readlines()
                json_payload_str.pop(0)
                json_payload_str = ''.join(json_payload_str)
                json_payload = json.loads(json_payload_str)
                json_reports.append(json_payload)
    return json_reports
    
def check_for_vul():
    has_error = 0
    for report_payload in json_reports:
        report_summary = report_payload['last_run']['summary']
        for service, report in report_summary.items():
            if report['max_level'] == break_level:
                print(f"{service} has vulnerability level of {break_level}")
            has_error = 1
    return has_error
    
if __name__ == "__main__": 
    extract_result()
    sys.exit(check_for_vul())
