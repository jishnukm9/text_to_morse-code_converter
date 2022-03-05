
letter_list=["._",'_...','_._.','_..','.','.._.','__.','....','..','.___','_._','._..','__','_.','___','.__.','__._','._.','...','_','.._','..._','.__','_.._','_.__','__..']
string_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def repeat():
    user_input=input("Encode or Decode?(E/D) :").lower()
    #encoding english language to morse code
    if user_input=='e':
        def encode(sentence):
            code=''
            sentence_list=sentence.split(' ')
            for word in sentence_list:
                conv_word = ''
                for let in range(len(word)):
                    if let!=len(word)-1:
                        for alphabet in range(len(string_list)):
                            if word[let] == string_list[alphabet]:
                                conv_word+=letter_list[alphabet]+' '
                    else:
                        for alphabet in range(len(string_list)):
                            if word[let] == string_list[alphabet]:
                                conv_word+=letter_list[alphabet]+'   '
                code+=conv_word
            return code

        sentence=input('Sentence to be encoded : ').lower()
        code=encode(sentence)
        print(code)
    #decoding morse code to english language
    elif user_input=='d':
        code=input('Code to be decoded : ')
        list_code=code.split('   ')
        try:
            list_code.remove('')
        except:
            pass
        deco=""
        for codes in list_code:
            code_list=codes.split(' ')

            for letters in range(len(code_list)):
                if len(code_list)-1 != letters:
                    deco+=string_list[letter_list.index(code_list[letters])]
                else:
                    deco+=string_list[letter_list.index(code_list[letters])]+' '
        print(deco)
    yes_or_no=input('Do you want to Encode/Decode again?(Y/N)').lower()
    if yes_or_no=='y':
        repeat()
    else:
        pass
repeat()




