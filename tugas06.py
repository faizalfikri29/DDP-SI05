print("====No 01======")
number = [ 951, 402, 
          984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165,
          141, 501, 263, 617, 865, 575, 219, 
           390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 
           823, 566, 597, 978, 328, 615, 953, 345, 
           399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 
           217, 815, 67, 104, 58, 512, 24, 892, 894,
           767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 
           451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]

index = 0
while index <= len(number):
  if number[index] == 553:
    break
  if number[index] %2 == 1:
    print(number[index], end=" ")
  index +=1

print("====No 02======")
jumlah = 0 #untuk menampung hasil
string = "" #untuk menampung hasil jumlah dalam bentuk string
bilangan = 1
while bilangan <= 19:
  jumlah += bilangan
  string += str(bilangan) 
  if bilangan < 19:
    jumlah += bilangan
    string += "+"
  bilangan += 2
print(f"{string} = {jumlah}")

print("====No 03======")
baris = int(input("masukan jumlah baris :"))
for i in range(1, baris +1):
  print('*' * i)