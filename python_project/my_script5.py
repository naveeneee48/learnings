#this is the Dictionary
student_char={
    "name": "naveen",
    "age": "27",
    "status": "married"

}
print(student_char["age"])

#here there is a DIct inside the Lists
ec2_instance_info=[
    {
        "name": "ec2-1",
        "type": "t2.micro"
    },
    {
        "name": "ec2-2",
        "type": "t2.medium"
    },
    {
        "name": "ec3",
        "type": "t2.large"
    }
]
print(ec2_instance_info[2]["name"])