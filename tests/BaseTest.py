import pytest
from datetime import datetime

@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        return "sidhartha" + time_stamp + "@gmail.com"