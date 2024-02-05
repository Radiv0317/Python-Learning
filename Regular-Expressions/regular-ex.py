import re

pattern = re.compile(r"\[(on|off)\]")
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50db][on]"))
print(re.search(pattern, "Nada....:-("))

def test_mail(my_pattern):
    if not my_pattern:
        print("Forgot to enter a pattern!")
        return

    pattern = re.compile(my_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]

    for email in emails:
        if not re.match(pattern, email):
            print("Failed to match %s" % (email))
        else:
            print("pass")

pattern = r""
test_mail(pattern)
