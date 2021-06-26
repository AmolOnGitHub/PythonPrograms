# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, 
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import

import time

amount = 0
def request_counter():
    global amount
    amount += 1
    if amount == 50:
        print("Slowing down...")
        time.sleep(60)
        amount = 0
