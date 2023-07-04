def mad_libs_generator():
    story = "Once upon a time in a [noun], there was a [adjective] [noun] who loved to [verb]. One day, while [verb-ing], the [noun] found a [adjective] [noun]. They decided to [verb] together and had a [adjective] time."

    # Prompt the user to enter words
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    noun2 = input("Enter another noun: ")
    verb1 = input("Enter a verb: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    adjective2 = input("Enter another adjective: ")
    verb2 = input("Enter another verb: ")
    adjective3 = input("Enter a final adjective: ")

    # Replace placeholders in the story with user input
    story = story.replace("[noun]", noun1)
    story = story.replace("[adjective]", adjective1)
    story = story.replace("[noun]", noun2, 1)
    story = story.replace("[verb]", verb1, 1)
    story = story.replace("[verb-ing]", verb_ing)
    story = story.replace("[noun]", noun2, 1)
    story = story.replace("[adjective]", adjective2)
    story = story.replace("[verb]", verb2, 1)
    story = story.replace("[adjective]", adjective3)

    # Print the final Mad Libs story
    print("\n--- Your Mad Libs Story ---\n")
    print(story)

# Call the function to generate a Mad Libs story
mad_libs_generator()