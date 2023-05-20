has_high_income = True
good_credit = True
criminal_record = True

if has_high_income or good_credit:
    print('eligible for loan')


if has_high_income and good_credit:
    print('eligible for loan and lesser payment')

if has_high_income and not criminal_record:
    print('good for you')