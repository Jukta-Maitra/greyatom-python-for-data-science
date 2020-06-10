# --------------
def read_file(path):
    file=open(path,mode='r')
    sentence=file.readlines()
    return sentence

sample_message = read_file(file_path)

message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
print(message_1)
print(message_2)

def fuse_msg(message_a,message_b):
     strings1=[str(integer) for integer in message_a]
     a_string="".join(strings1)
     integer_a=int(a_string)
     string2=[str(integer) for integer in message_b]
     b_string="".join(string2)
     integer_b=int(b_string)
     quotient=integer_b//integer_a
     return str(quotient)

secret_msg_1 = fuse_msg(message_1,message_2)

message_3 = read_file(file_path_3)
print(message_3)

def substitute_msg(message_c):
    strings1=[str(integer) for integer in message_c]
    message_c="".join(strings1)

    sub=None
    if message_c == 'Red':
        sub="Army"
    if message_c == 'Green':
        sub = "Data Scientist"
    if message_c == 'Blue':
        sub = "Merine Biologist"
# check for conditions
    return sub
secret_msg_2=substitute_msg(message_3)

message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
print(message_4)
print(message_5)
def compare_msg(message_d,message_e):

    a_list=message_d[0].split()
    b_list=message_e[0].split()
    c_list=[]
    for ele in a_list:
        if not ele in b_list:
            c_list.append(ele)
    
    final_msg=" ".join(c_list)
    return final_msg

secret_msg_3=compare_msg(message_4,message_5)    

message_6=read_file(file_path_6)
print(message_6)

def extract_msg(message_f):
     a_list=message_f[0].split()
     even_word=lambda x:len(x)%2==0
     b_list=list(filter(even_word,a_list))
     final_msg=" ".join(b_list)
     return final_msg

secret_msg_4=extract_msg(message_6)

message_parts=[]
message_parts.extend(secret_msg_3)
message_parts.extend(" "+secret_msg_1)
message_parts.extend(" "+secret_msg_4)
message_parts.extend(" "+secret_msg_2)
strings1=[str(integer) for integer in message_parts]
secret_msg="".join(strings1)

def write_file(secret_msg,path):
    f=open(path,mode='a+')
    f.write(secret_msg)
    f.close()
final_path= user_data_dir + '/secret_message.txt'

write_file(secret_msg,final_path)
print(secret_msg)




