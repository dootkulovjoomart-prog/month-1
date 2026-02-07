# Повторение, подготовка к тесту.

keywords_list = """
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
""".split()
keywords_dic={}
for keyword in keywords_list:
    while True:

            answer = input(f'проходили ли мы ключевое слово - {keyword}? ')
            if answer == '1':
                keywords_dic[keyword] = True
                break
            elif answer == '0':
                keywords_dic[keyword] = False
                break
            else:
                print('Ошибка вводить только 1 или 0 !')
total=len(keywords_dic)
passed_keywords=[]
for key, value in keywords_dic.items():
    if value ==True:
        passed_keywords.append(key)

not_passed_keywords=[]
for key, value in keywords_dic.items():
    if value==False:
        not_passed_keywords.append(key)
procent_passed_keywords=(len(passed_keywords)/total)*100
procent_not_passed_keywords=(len(not_passed_keywords)/total)*100
procent_passed_keywords=round(procent_passed_keywords,2)
procent_not_passed_keywords=round(procent_not_passed_keywords, 2)
print(f'общее количество ключевых слов{total}')
print(f'Вывести пройденные ключевые слова:{passed_keywords}')
print(f'Вывести не пройденные ключевые слова:{not_passed_keywords}')
print(f'проентное соотношение:пройденные ключевые слова{procent_passed_keywords}%/100%,не пройденные ключевые слова:{procent_not_passed_keywords}%/100%')




