# Долевое строительство (task_01.py)
Дан набор из N долей, представленных в виде N рациональных. Необходимо представить эти доли в процентном выражении c точностью до трех знаков после запятой.

### Входные данные <br>
Первая строка содержит значение N - число долей, каждая последующая содержит числовое выражение доли. <br>

4 <br>
1.5 <br>
3 <br>
6 <br>
1.5 <br>

### Выходные данные <br>
N строк с процентным выражением долей. Значение в строке k является процентным выражение доли из строки k+1 входных данных <br>
<br>
0.125 <br>
0.250 <br>
0.500 <br>
0.125 <br>
#
# Мегатрейдер (task_02.py)
Допустим, что на рынке существует некое множество облигаций с номиналом 1000 условных единиц, по которым каждый день выплачивается купон размером 1 уе. Погашение номинала облигации (то есть выплата 1000 условных единиц) происходит в конце срока. <br>

Каждая облигация на рынке характеризуется названием (некая строка) и ценой, цена выражается в виде процентов от номинала, то есть цена 98.5 соответствует цене 98,5% * 1000 = 985 условных единиц. <br>

У некоего трейдера есть информация о том какие предложения по облигациям будут на рынке в ближайшие N дней. По каждому дню он знает, какие лоты будут представлены на бирже: название облигации, цену и количество в штуках. Каждый день на рынке может быть от 0 до M лотов. Трейдер располагает суммой денежных средств в количестве S. <br>

Необходимо определить какие лоты в какие дни нужно купить, чтобы получить максимальный доход с учетом следующих условий: <br>

Трейдер может только покупать облигации. Купленные облигации не продаются. <br>
Трейдер может купить только весь лот целиком при наличии доступных денежных средств.<br>
Выплаченные купоны по купленным облигациям не реинвестируются, то есть не увеличивают сумму доступных денежных средств.<br>
Все купленные облигации будут погашены в день N+30.<br>
Доход рассчитывается на день N+30, то есть после погашения облигаций.<br>
### Входные данные <br>
На первой строке будут даны числа N, M и S. Далее будет идти k строк вида “<день> <название облигации в виде строки без пробелов> <цена> <количество>”. Ввод будет завершен пустой строкой.<br>

2 2 8000 <br>
1 alfa-05 100.2 2 <br>
2 alfa-05 101.5 5 <br>
2 gazprom-17 100.0 2 <br>

### Выходные данные <br>
В первой строке необходимо указать сумму дохода, полученного трейдером на день N+30. В последующих строках привести купленные лоты в таком же формате, который используется во входных данных. Последняя строка должна быть пустой. <br>

135 <br>
2 alfa-05 101.5 5 <br>
2 gazprom-17 100.0 2 <br>