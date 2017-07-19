import sys

def main():
    letter_map={}
    with open('upper_case.txt','r') as src:
         for line in src.readlines():
             item=line.strip().split(u' ')
             for letter in item[1].split(u','):
                 print ord(letter)
                 letter_map[ord(letter)]=ord(item[0])

    
    with open('lower_case.txt','r') as src:
         for line in src.readlines():
             item=line.strip().split(u' ')
             for letter in item[1].split(u','):
                 print ord(letter)
                 letter_map[ord(letter)]=ord(item[0])
    
    with open('test.txt','r') as src:
         line=unicode(src.readlines()[0])
         line=line.translate(letter_map)
         print line

if __name__ == '__main__':
   reload(sys)
   sys.setdefaultencoding('utf-8')
   main()