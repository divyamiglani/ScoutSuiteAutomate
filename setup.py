import sys
import os
from ScoutSuite.__main__ import run_from_cli

report_root = 'scoutsuite-report'
    
if __name__ == "__main__": 
    os.system("rm -rf "+report_root)
    run_from_cli()
    sys.exit(0)
