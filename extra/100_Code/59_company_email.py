import re

def get_company_name() -> str:
    email = "jagan.dream@accenture.com"
    pat2 = "(\w+)@(\w+)\.(\w+)"
    r2 = re.match(pat2, email)
    print(r2.group(1))

if __name__ == "__main__":
    print(get_company_name())
