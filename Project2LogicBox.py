   #Logic Box: Pattern Generator and Number Analyzer


print("Welcome to Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Number")
    print("3. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        rows = int(input("Enter the number of rows: "))
            

        
        #option 1    
        print("Pattern:")

        for i in range(1,rows +1):
            
                 print("*"* i)
                
        #option2
    elif choice ==2:  
         start= int(input("Enter the start number:"))
         end= int(input("Enter the end number:"))
         if end<start:
             print("Invalid range!")
             continue

         total=0
         print("Number Analysis:")
         for i in range(start,end+1):
             if i==0:
                 pass
             if i%2==0: 
                print(i,"is Even")
             else:
                print(i,"is Odd")

             total=total+i

         print("Sum of all numbers:",total)

         #option3
    elif choice==3:
            print("Existing the program.Goodbye!")
            break
    else: 
        print("Invalid choice!")
        continue
        
