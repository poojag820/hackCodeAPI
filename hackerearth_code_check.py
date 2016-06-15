"""
ihackerearth_code_check.py
compile and run script in different languages
Author:ABHISHEK GOSWAMI
"""


import requests
import config
import os


#parameters required
run_url = 'http://api.hackerearth.com/code/run/'
compile_url = 'http://api.hackerearth.com/code/compile/'


#dict for mapping languages
lang_dict = {
    'C':'C',
    'C++':'CPP',
    'C++11':'CPP11',
    'Cloure':'CLOJURE',
    'C#':'CSHARP',
    'Java':'JAVA',
    'Javascript':'JAVASCRIPT',
    'Haskell':'HASKELL',
    'Perl':'PERL',
    'PHP':'PHP',
    'Python':'PYTHON',
    'Ruby':'RUBY'
};


def run_code(data):
    #print data
    r = requests.post(run_url,data = data)
    r = r.json()
    #print r
    status = r['run_status']['status']
    if status == 'AC':
        output = r['run_status']['output']
        time_used = r['run_status']['time_used']
        memory_used = r['run_status']['memory_used']
        print 'status',status
        print 'Output:',output
        print 'Time Used',time_used
        print 'Memory Used',memory_used


def compile_code(data):
    #print data
    r = requests.post(compile_url,data = data)
    r = r.json()
    return r['compile_status']


def main():
    print 'The script is available for languages:'
    for keys,values in lang_dict.items():
        print keys


    #get inputs from the user
    lang = raw_input('Enter the language')
    file_name = raw_input('Enter the file name')
    if lang == '' or file_name == '':
        print 'Error:Language and file name are required'
        return
    elif not os.path.isfile(file_name):
        print 'Error:No such file exists'
        return


    #handle the case of language string
    lang = lang.lower()
    lang = lang[0].upper() + lang[1:]
    #print lang
    file_source = open(file_name).read()
    post_data_dict = {
        'client_secret':config.get_key(),
        'lang':lang_dict[lang],
        'source':file_source,
        'async':0,
        'time_limit':5,
        'memory_limit':262144
    }


    #complile the code first
    compile_result = compile_code(post_data_dict)
    if compile_result == 'OK':
        run_code(post_data_dict)
    else:
        print compile_result


if __name__ == '__main__':
    main()
