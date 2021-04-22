if __name__ == '__main__':
    fav_lang = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
    }

    print("Jen's favourtie language is: " +
          fav_lang['jen'].title() +
          ".")

    for name, language in fav_lang.items():
        print(name.title() + "'s favourite language is: "
              + language.title() + ".\n")

    # It does the same if keys() isn't there
    # Only there to be more readable
    for name in fav_lang.keys():
        print(name.title())
    print("\n\n")

    ###
    friends = ['phil', 'sarah']
    for name in fav_lang.keys():
        print(name.title())

        if name in friends:
            print("Hi " + name.title() +
                  ", I see your favourite language is " +
                  fav_lang[name].title() + "!")
    print("\n\n")

    # Access sorted dictionary
    for name in sorted(fav_lang.keys()):
        print(name.title() + ", thanks for taking the poll!")

    # Loop through values on dictionary
    # set() takes out repeated values
    print("\n\nLanguages mentioned: ")
    for lang in set(fav_lang.values()):
        print(lang.title())
