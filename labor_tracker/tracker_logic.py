LABOR_CAP = 5000
LABOR_INCREMENT = 10
LABOR_INCREMENT_FREQUENCY_SECONDS = 300


def add_account(username, account, labor, timestamp):
    print(f"{username}, {account}, {labor}, {timestamp}")
    return None


def set_labor(username, account, labor, timestamp):
    return None


def get_labor(username, account, timestamp):
    return 0


def get_accounts(username):
    return []


def remove_account(username, account):
    return None


def print_accounts(username, timestamp):
    output = f'{username}:\n'
    accounts = get_accounts(username)
    if not accounts:
        return output + "\t No Accounts\n"
    for account in accounts:
        labor = get_labor(username, account, timestamp)
        output += f"\t{account}: {labor}\n"
    return output
