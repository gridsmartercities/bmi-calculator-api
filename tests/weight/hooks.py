import dredd_hooks as hooks


@hooks.before("/ideal-weight > GET > 500 > application/json")
def before_bmi_get_500(transaction):
    transaction["skip"] = True


@hooks.before("/ideal-weight > GET > 400 > application/json")
def before_bmi_get_400(transaction):
    transaction["request"]["uri"] = transaction["request"]["uri"].replace("180", "0")
    transaction["fullPath"] = transaction["fullPath"].replace("180", "0")
