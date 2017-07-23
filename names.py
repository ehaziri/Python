#1
# students = [
#     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# for dictionary in students:
#         print dictionary["first_name"], dictionary["last_name"]


#2
users = {
    'Students' : [
        {'first_name' : "Michael", "last_name" : 'Jordan'},
        {'first_name' : "John", "last_name" : 'Rosales'},
        {'first_name' : "Mark", "last_name" : 'Guillen'},
        {'first_name' : "KB", "last_name" : 'Tonel'}
    ],
    'Instructors' : [
        {'first_name' : "Michael", "last_name" : 'Choi'},
        {'first_name' : "Martin", "last_name" : 'Puryear'}
    ]
}



for key, data in users.items():
    print key
    i = 1
    for value in data:
            fn = value["first_name"]
            fn_len = len(fn)
            ln = value["last_name"]
            ln_len = len(ln)
            full_len = fn_len + ln_len
            print  i, "-", fn.upper() , ln.upper() , "-", full_len
            i += 1
