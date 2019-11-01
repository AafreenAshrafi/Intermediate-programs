import xml.etree.ElementTree as ET
import sys
import os

#file size check for question file
def file_size(fname):
    global size_file
    statinfo= os.stat(fname)
    size_file =statinfo.st_size
    #print('file size is',size_file)

def main_function():
    try:
        #input from user
        dict= []
        #global dict
        total_marks= int(input('Enter the total no of Marks of Question Paper '))
        easy_cent= float(input('Enter the percentage of easy difficulty marks in Question Paper '))
        medium_cent= float(input('Enter the percentage of medium difficulty marks in Question Paper '))
        hard_cent= float(input('Enter the percentage of hard difficulty marks in Question Paper '))
        
        #calculate the no of marks required to generate for each difficulty level
        total_percentage= int(easy_cent+medium_cent+hard_cent)
        if total_percentage == 100 :
            easy_M= int((total_marks*easy_cent)/100)
            medium_M= int(total_marks*(1/100)*medium_cent)
            hard_M= int(total_marks*(1/100)*hard_cent)
            #global easy_M
            print('easy_M {} medium_M {} hard_M {}'.format(easy_M,medium_M,hard_M))
        else :
            print('''Please enter proper dificulty percentage as total of easy,medium and 
            hard difficulty percentage is not or is more than 100% ''' )

        #parse the XML question file take out diff question with sum(marks) =easy_M and print QID
        file_size("C:/Users/aafreen.ashrafi/Desktop/Aafreen_information/python/Intermediate Projects/project//QuestionFile.xml")
        if (size_file==0):
            # Write a new file**********************************
            print('the question file is 0 KB we need to enter the questions details ')
            dificulty_level1= input('enter the difficulty level of question in small letters(lower case supported)')
            marks_assigned1= input('enter the marks for this question ')
            Qid1= input('enter question id eg:Q99 ')

            data = ET.Element('data')
            items = ET.SubElement(data,'items')
            item1 = ET.SubElement(items,'item')
            item1.set('dificulty_level',dificulty_level1)
            item1.set('marks_assigned',marks_assigned1)
            item1.text =Qid1
            mydata = (ET.tostring(data).decode('utf-8'))
            myfile = open('C:/Users/aafreen.ashrafi/Desktop/Aafreen_information/python/Intermediate Projects/project//QuestionFile.xml','w')
            myfile.write(str(mydata))
            myfile.close()

        else:
            #Modify a new file******************************************
            print('adding question to question file ')
            option=input('enter N for Exit and Y for continue to add question')
            if option=='Y' or option=='y':
                dificulty_level1= input('enter the difficulty level of question')
                marks_assigned1= input('enter the marks for this question')
                Qid1= input('enter question id eg:Q99')
                tree = ET.parse('C:/Users/aafreen.ashrafi/Desktop/Aafreen_information/python/Intermediate Projects/project//QuestionFile.xml')
                root = tree.getroot()
                attrib={}
                attrib = {'dificulty_level':dificulty_level1,'marks_assigned':marks_assigned1}
                subelement = root[0].makeelement('item',attrib)
                ET.SubElement(root[0],'item',attrib)
                d=(len(root[0]))
                #print(d)
                root[0][d-1].text =Qid1
                tree.write('C:/Users/aafreen.ashrafi/Desktop/Aafreen_information/python/Intermediate Projects/project//QuestionFile.xml') 
            else : 
                print('exiting the Question file without modifying and generating question paper')
                #exit
            #generate question Paper from QuestionFile.xml
        def check():
            tree = ET.parse('C:/Users/aafreen.ashrafi/Desktop/Aafreen_information/python/Intermediate Projects/project//QuestionFile.xml')
            root = tree.getroot()
            found = False
            totalsum_easy =0
            totalsum_medium=0
            totalsum_hard=0
            for elem in root:
                found = False
                for subelem in elem:
                    d = subelem.attrib
                    easy='easy'
                    medium='medium'
                    hard='hard'
                    #global totalsum
                    if easy in d['dificulty_level']:
                        
                                    for eachvalue in  d['marks_assigned']:
                                        #totalsum =0
                                        if totalsum_easy <easy_M and int(eachvalue) <=easy_M:
                                            #if int(eachvalue) <=easy_M:
                                                #print(int(eachvalue))
                                                #print(totalsum)
                                                Qid=(subelem.text)
                                                dict.append(Qid)
                                                totalsum_easy = totalsum_easy + int(eachvalue)
                                                if totalsum_easy >easy_M:
                                                    totalsum_easy= totalsum_easy-int(eachvalue)
                                                    dict.remove(Qid) 
                                                                                                  
                                        

                    if medium in d['dificulty_level']:
                        
                                    for eachvalue in  d['marks_assigned']:
                                        #totalsum =0
                                        if totalsum_medium <medium_M and int(eachvalue) <=medium_M:
                                            #if int(eachvalue) <=easy_M:
                                                #print(int(eachvalue))
                                                #print(totalsum)
                                                Qid=(subelem.text)
                                                dict.append(Qid)
                                                totalsum_medium = totalsum_medium + int(eachvalue)
                                                if totalsum_medium >medium_M:
                                                    totalsum_medium= totalsum_medium-int(eachvalue)
                                                    dict.remove(Qid)
                    if hard in d['dificulty_level']:
                        
                                    for eachvalue in  d['marks_assigned']:
                                        #totalsum =0
                                        if totalsum_hard <hard_M and int(eachvalue) <=hard_M:
                                            #if int(eachvalue) <=easy_M:
                                                #print(int(eachvalue))
                                                #print(totalsum_hard)
                                                Qid=(subelem.text)
                                                dict.append(Qid)
                                                totalsum_hard = totalsum_hard + int(eachvalue)
                                                if totalsum_hard >hard_M:
                                                    totalsum_hard= totalsum_hard-int(eachvalue)
                                                    dict.remove(Qid)

                found=True                            
            print(totalsum_easy)
            print(totalsum_medium)
            print(totalsum_hard)
            if totalsum_easy != easy_M or totalsum_medium !=medium_M or totalsum_hard != hard_M:
                print('the data in QuestionFile.xml is not proper as it cant generate desired marks and difficulty level question. Please verify the data')        
            else:
                print(dict)
            
            if found != True:
                    #print('calling main function')
                    print('the data in QuestionFile.xml is not proper as it cant generate desired marks and difficulty level question. Please verify the data')
        check()
    except Exception as e:
        print(str(e))
main_function()



