import datetime
from unittest import mock
from unit_tests.mock_examples import tested_module


DATETIME_MODULE = 'unit_tests.mock_examples.tested_module.datetime'

actual_date = tested_module.get_date()
print(str(actual_date))
#2019-05-30

with mock.patch(DATETIME_MODULE) as freezed_date:
    freezed_date.utcnow = \
        mock.Mock(return_value=datetime.datetime(2016, 11, 14))
    actual_date = tested_module.get_date()
    print(str(actual_date))
    #2016-11-14