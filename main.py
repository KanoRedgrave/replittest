def main():
  #Introduction
    intro()

    try:
      #Input miles driven
        num_miles = int(input("Please enter total miles driven: ")) 
      
      #Converting miles to kilometers
        miles_to_kilometers(num_miles) 

    except:
        print()
        print("We only accept numbers here, my dude. Try again") 
        print()
        main()

  #Intro function displays on the intro screen
def intro():
    print("This will convert miles driven to kilometers.")
    print("Example: 1 miles = 1.60934 kilometers.")
    print()

  # miles_to_kilometers acccepts the number of miles driven and converts to kilometers
def miles_to_kilometers(num_miles):
    kilometers = num_miles * 1.60934
    print("Total distance:", kilometers,"kilometers")

  # calls the main function
main()