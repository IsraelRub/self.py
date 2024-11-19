def inverse_dict(my_dict):
    new_dict ={}

    for key, value in my_dict.items():
        new_dict.setdefault(value, []).append(key)

    return new_dict

def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))

if __name__=='__main__':
    main()