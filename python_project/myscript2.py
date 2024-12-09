# import sys
# day=sys.argv[1]
# if day == "sunday":
#     print("today is " + day)
# elif day == "saturday":
#     print("today is " + day)
# else:
#     print("today is not " + day)

#list is mutable that it can be changed
students_names = ["naveen", "kumar", "kavin"]
print(students_names)
s3_bucket_names=["naveen-s3", "kumar-s3", "kavin-s3"]
# print(s3_bucket_names)
#tuple
#tuples are immutable
# s3_bucket_names.append("ravina-s3")
# s3_bucket_names.remove("file-s3")
print(s3_bucket_names)
#when i create a list and python create index for each object in list
print(s3_bucket_names[0])
print(len(s3_bucket_names)) #get length
print(s3_bucket_names[0:2]) #
numbers=[1,4,3,6]
numbers.sort() #sort the list
print(numbers)
print(s3_bucket_names[0] + s3_bucket_names[1]) #concatinating
random_list =  [1,2,3,"naveen",4]
print(random_list)
print(random_list[3])
##################