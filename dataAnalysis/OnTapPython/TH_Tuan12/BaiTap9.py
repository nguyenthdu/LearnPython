#Hãy viết chương trình đọc file in.txt và hiển thị ra màn hình nội dung từng dòng trong file đó
with open('file/in.txt','r') as f:
     for line in f:
        print(line)
