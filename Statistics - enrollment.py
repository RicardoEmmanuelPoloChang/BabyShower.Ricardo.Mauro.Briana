def zoo():
  count_2 = 0
  count_2_5 = 0
  count_5_10 = 0
  count_10 = 0

  while True:
      response = input("Is there another animal to be recorded? (yes/no): ").lower()

      if response == 'no':
          break 
      elif response != 'yes':
          print("Invalid input. Please enter 'yes' or 'no'.")
          continue  


      age = float(input("Enter the age of the animal (in years): "))

      if age < 2:
          count_2 += 1
      elif 2 <= age < 5:
          count_2_5 += 1
      elif 5 <= age < 10:
          count_10 += 1
      else:
          count_10 += 1


  total_animals = count_2 + count_2_5 + count_5_10 + count_10
  percentage_less_than_2 = (count_2 / total_animals) * 100
  percentage_2_to_5 = (count_2_5 / total_animals) * 100
  percentage_5_to_10 = (count_5_10 / total_animals) * 100
  percentage_greater_than_10 = (count_10 / total_animals) * 100

  print("\nZoo Statistics:")
  print(f"Number of animals less than 2 years: {count_2} ({percentage_less_than_2:.2f}%)")
  print(f"Number of animals between 2 and less than 5 years: {count_2_5} ({percentage_2_to_5:.2f}%)")
  print(f"Number of animals between 5 and less than 10 years: {count_5_10} ({percentage_5_to_10:.2f}%)")
  print(f"Number of animals greater than or equal to 10 years: {count_10} ({percentage_greater_than_10:.2f}%)")


zoo()
