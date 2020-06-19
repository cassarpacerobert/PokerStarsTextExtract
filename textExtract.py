# Robert Cassar Pace
# This script will extract all of the relevant information from the PokerStars gameplay text files.

import os

folderPath = "./textFiles"

myFileHandsID = []
myFileCardHands = []


def myFilesAddEmptyLine():
    # This finds each file in the directory and appends a blank line at the very top.
    for file in os.listdir(folderPath):
        if file.endswith(".txt"):
            with open(os.path.join(folderPath, file), "r+") as myFile:
                fileContent = myFile.read()
                myFile.seek(0, 0)
                myFile.write("\n" + fileContent)


myFilesAddEmptyLine()


def extractDataFromFiles():
    for file in os.listdir(folderPath):
        if file.endswith(".txt"):
            with open(os.path.join(folderPath, file), "r") as myFileData:
                fileData = myFileData.readlines()
                for line in fileData:
                    if line.startswith('PokerStars'):
                        # This retrieves the hand ID.
                        # print("\nHand ID:", line[26:39])

                        # This appends the hand ID to the array.
                        myFileHandsID.append(int(line[27:39]))

                    elif line.startswith("Dealt to"):
                        # This prints the hands that the player was dealt ONLY.
                        # print(line[-13:-2])

                        # This prints the whole line.
                        # print(line[0:len(line)-1])

                        # This appends the whole line to the array.
                        myFileCardHands.append(line[0:len(line)-1])
    # This returns the retrieved details from each file in the folder.
    return(myFileHandsID, myFileCardHands)  # , myFileSeatInfo


extractDataFromFiles()


# This zips all of the returned information into one array.
myFilesArray = list(zip(myFileHandsID, myFileCardHands))  # , myFileSeatInfo

# This sorts the array.
myFilesArray.sort()

# for item in myFilesArray:
#     print(item)


def prettyPrint():
    # This part retrieves the original array and appends the same values (excluding duplicates) in another array.
    seen = set()
    unique = []
    for hand in myFileHandsID:
        if hand not in seen:
            unique.append(hand)
            seen.add(hand)

    # This sorts the newly created array.
    unique.sort()

    # This checks whether the final file exists or not. If it does, delete it before appending (to avoid duplicated content).
    if os.path.exists("finalFile.txt"):
        os.remove("finalFile.txt")

    # For each item in the array called 'unique' it is going to iterate the following:
    for item in unique:
        with open("finalFile.txt", "a") as finalFile:
            finalFile.write("\n")
            finalFile.write("Hand ID: " + str(item) + "\n")
            for hands in myFilesArray:
                # If the first column from 'myFilesArray' is equal to the unique item, print the hands accordingly.
                if(hands[0] == item):
                    finalFile.write(hands[1] + "\n")


prettyPrint()
