import dredd_hooks as hooks


@hooks.before("/bmi > GET > 500 > application/json")
def before_a_lambda_get_500(transaction):
    transaction["skip"] = True


@hooks.before("/bmi > GET > 400 > application/json")
def before_a_lambda_get_500(transaction):
    transaction["skip"] = True
