__author__ = 'zhangyanni'

# -*- coding:UTF-8 -*-
import codecs
import json
import os
import os.path
#�������е���md��ʽ�洢���ļ�����������⣩
def walk_md_list():

    file_dir="G:\GitHub\os_course_exercise_library\\"
    for i in range(1,16):
        fileDir=file_dir+str(i)
        for parent,dirnames,filenames in os.walk(fileDir):
            for filename in filenames:
                fileName=os.path.join(parent,filename)
                #����md2json�����ѵ�ǰ�ļ�ת��Ϊjson��ʽ�洢
                json_data=md2json(fileName)
                #�½�Ŀ¼������
                dir_new=os.path.join(r"G:\md2json",str(i))
                if(os.path.exists(dir_new) is not True):
                    os.makedirs(dir_new)
                (shortname,extension) = os.path.splitext(filename)
                saveFile(dir_new,shortname,json_data)


#��md��ʽ���ļ�ת��Ϊ����õ�json���ݸ�ʽ�洢
def md2json(file_name):
    fileObj=codecs.open(file_name, encoding='utf-8')
    #ת����Ľ��������result�ֵ���
    #options: ��options��ֵ�ǿ�ѡ���б�
    #question:��question��ֵ�����
    #answer:��answer��ֵ�ǲο���
    #type:��type����ֵ����Ŀ����
    result={}
    result["options"]=""
    result["question"]=""
    try:
        num=1
        answer=""
        #���ж��ļ� line_num:�кţ�value:��������
        for (line_num,value) in enumerate(fileObj):
            #�ɵ�һ�л���ļ�����
            if(line_num==0):
                type_num=value
                result["type"]=value
            #'-'��ͷ���д������ѡ�������
            elif value[0]=='-':
                result["options"]+=value[5:]
            #��һ�� '>'�������֪ʶ��;�ڶ���'>'���������Ŀ��Դ;������'>'��������Ѷ�;'>'���ĸ�������Ǵ�
            elif(value[0]=='>'):
                if(num==1):
                    result["knowledge"]=value[6:]
                elif (num==2):
                    result["source"]=value [5:]
                elif(num==3):
                    result["degree_of_difficulty"]=value [5:]
                elif(num==4):
                    #��ѡ���ж�
                    if (int(type_num)==1or int(type_num)==3):
                        for i in value[2:3]:
                            if i.isupper():
                                answer+=i
                        break
                    #��ѡ
                    elif(int(type_num)==2):
                        for i in value[2:6]:
                            if (i.isupper()):
                                answer+=i
                            elif (i.isspace()):
                                break
                    #�ʴ�
                    else:
                        answer=value[2:len(value)-2]
                    result["answer"]=answer

                num+=1
            #���
            else:
                result["question"]+=value
        #��dictת��Ϊjson����
        result_jsonObj=json.dumps(result)
        #��������
        data=json.loads(result_jsonObj)
        json_data=json.dumps(data,ensure_ascii=False)
        return json_data
    except:
        print "cannot read!"
    finally:
        fileObj.close()

def saveFile(file_path,file_name,data):
    output = codecs.open(file_path+"\\"+file_name+".json",'w',"utf-8")
    output.write(data)
    output.close()


if __name__ == '__main__':
    walk_md_list()









