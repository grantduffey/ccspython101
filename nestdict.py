def countFriends(dictionary):
    count = 0
    while count < len(dictionary["friends"]):
        count += 1
    dictionary["friends_count"] = count
    return dictionary

ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
        'name': 'Jasmine',
        'email': 'jasmine@yahoo.com',
        'interests': ['photography', 'tennis']
        },
        {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
        }
    ]
}

print("Ramit's email address: %s" % ramit["email"])
print("Ramit's first interest: %s" % ramit["interests"][0])
print("Jasmine's email: %s" % ramit["friends"][0]["email"])
print("Jan's second interest: %s" % ramit["friends"][1]["interests"][1])

ramit = countFriends(ramit)
print("Ramit's number of friends: %s" % ramit["friends_count"])
