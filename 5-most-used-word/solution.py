l = ['Though', 'yet', 'of', 'Hamlet', 'our', 'dear', "brother's", 'death', 
'The', 'memory', 'be', 'green,', 'and', 'that', 'it', 'us', 'befitted', 'To', 
'bear', 'our', 'hearts', 'in', 'grief', 'and', 'our', 'whole', 'kingdom', 'To', 
'be', 'contracted', 'in', 'one', 'brow', 'of', 'woe,', 'Yet', 'so', 'far', 
'hath', 'discretion', 'fought', 'with', 'nature', 'That', 'we', 'with', 
'wisest', 'sorrow', 'think', 'on', 'him,', 'Together', 'with', 'remembrance', 
'of', 'ourselves.', 'Therefore', 'our', 'sometime', 'sister,', 'now', 'our', 
'queen,', 'The', 'imperial', 'jointress', 'to', 'this', 'warlike', 'state,', 
'Have', 'we,', 'as', "'twere", 'with', 'a', 'defeated', 'joy,--', 'With', 'an', 
'auspicious', 'and', 'a', 'dropping', 'eye,', 'With', 'mirth', 'in', 'funeral', 
'and', 'with', 'dirge', 'in', 'marriage,', 'In', 'equal', 'scale', 'weighing', 
'delight', 'and', 'dole,--', 'Taken', 'to', 'wife:', 'nor', 'have', 'we', 
'herein', "barr'd", 'Your', 'better', 'wisdoms,', 'which', 'have', 'freely', 
'gone', 'With', 'this', 'affair', 'along.', 'For', 'all,', 'our', 'thanks.', 
'Now', 'follows,', 'that', 'you', 'know,', 'young', 'Fortinbras,', 'Holding', 
'a', 'weak', 'supposal', 'of', 'our', 'worth,', 'Or', 'thinking', 'by', 'our', 
'late', 'dear', "brother's", 'death', 'Our', 'state', 'to', 'be', 'disjoint', 
'and', 'out', 'of', 'frame,', 'Colleagued', 'with', 'the', 'dream', 'of', 'his', 
'advantage,', 'He', 'hath', 'not', "fail'd", 'to', 'pester', 'us', 'with', 
'message,', 'Importing', 'the', 'surrender', 'of', 'those', 'lands', 'Lost', 
'by', 'his', 'father,', 'with', 'all', 'bonds', 'of', 'law,', 'To', 'our', 
'most', 'valiant', 'brother.', 'So', 'much', 'for', 'him.', 'Now', 'for', 
'ourself', 'and', 'for', 'this', 'time', 'of', 'meeting:', 'Thus', 'much', 
'the', 'business', 'is:', 'we', 'have', 'here', 'writ', 'To', 'Norway,', 
'uncle', 'of', 'young', 'Fortinbras,--', 'Who,', 'impotent', 'and', 'bed-rid,', 
'scarcely', 'hears', 'Of', 'this', 'his', "nephew's", 'purpose,--to', 'suppress', 
'His', 'further', 'gait', 'herein;', 'in', 'that', 'the', 'levies,', 'The', 
'lists', 'and', 'full', 'proportions,', 'are', 'all', 'made', 'Out', 'of', 'his', 
'subject:', 'and', 'we', 'here', 'dispatch', 'You,', 'good', 'Cornelius,', 'and', 
'you,', 'Voltimand,', 'For', 'bearers', 'of', 'this', 'greeting', 'to', 'old', 
'Norway;', 'Giving', 'to', 'you', 'no', 'further', 'personal', 'power', 'To', 
'business', 'with', 'the', 'king,', 'more', 'than', 'the', 'scope', 'Of', 'these', 
'delated', 'articles', 'allow.', 'Farewell,', 'and', 'let', 'your', 'haste', 
'commend', 'your', 'duty']

seen_words = [] # list of words seen so far
word_frequency = {} # frequency of each word seen so far

for word in l:
    if word in seen_words:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
        seen_words.append(word)

list_of_words = [(word[1], word[0]) for word in word_frequency.items()]
list_of_words.sort(reverse=True)
print('The two words with highest usages are: {} and {}'.format(list_of_words[0], list_of_words[1]))