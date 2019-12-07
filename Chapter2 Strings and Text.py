import re
# line = 'asdf   fjdk; afed, fjek,asdf, foo'
# import re
# print(re.split(r'[;,\s]\s*', line))
# print(re.split(r'(;|,|\s)\s*', line))
# name = 'Robinzlc slll'
# print(name.endswith(('z', 'll')))
# datepat = re.compile(r'\d+/\d+/\d+')
# datepat2 = re.compile(r'.*\d+/\d+/\d+.*')
# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# print(datepat.findall(text))
# m = datepat2.match(text)
# print(m.groups())
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1---\2', text)
print(text)