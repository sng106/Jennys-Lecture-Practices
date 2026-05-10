def paint_calculation (height,width, cover):
  area=height*width
  no_of_cans=area/cover
  print (f"You will need {no_of_cans} cans of paint.")
  
h=int (input("Enter the height of wall in meters:\n"))
w=int (input("Enter the width of wall in meters: \n"))
coverage=7
paint_calculation (width=w, height=h, cover=coverage)
