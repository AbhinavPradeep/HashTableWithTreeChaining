from HashTable import HashTable
from Node import Node
import random

#Try constant insert amortised logarithmic search

Table = HashTable()

print(Table.Table)

print("\n")

CollidingKeys = [[('jrptf', 'jhhmu', 0), ('kilow', 'qbhxi', 0), ('zmibj', 'srewo', 0), ('yhlhq', 'ptfwo', 0), ('pwsnr', 'nouas', 0), ('mcpjr', 'ctvud', 0), ('fhcqf', 'omaef', 0), ('owtog', 'kkiwp', 0), ('stxpk', 'shelz', 0), ('krlcp', 'butgt', 0)], 
[('xyovo', 'dxydn', 1), ('igyoo', 'hwaqb', 1), ('kjrlj', 'jxolt', 1), ('igqkq', 'dnkdr', 1), ('recto', 'ikbvq', 1), ('yrpqy', 'kxahq', 1), ('spjvd', 'grdlj', 1), ('dgkzw', 'lmwsx', 1), ('gjqdc', 'rthip', 1), ('lrnel', 'nwyru', 1)], 
[('xqoao', 'zhokb', 2), ('nhbew', 'mndyp', 2), ('grtri', 'swflv', 2), ('rfkle', 'iygmr', 2), ('kivas', 'basqm', 2), ('rbjdr', 'wmhht', 2), ('pryho', 'fjmdi', 2), ('xmmku', 'dplvr', 2), ('xahpw', 'kntwd', 2), ('ccfqc', 'nplik', 2)], 
[('psiwf', 'uyxdi', 3), ('wyhov', 'sdqmt', 3), ('rsmul', 'txtcf', 3), ('wnxtl', 'tyzeq', 3), ('bytya', 'rkpbf', 3), ('rvciu', 'hvsvl', 3), ('xrvzw', 'dzage', 3), ('tirpt', 'vbljq', 3), ('bngqw', 'rhgrb', 3), ('kyqzx', 'zulzh', 3)], 
[('szccc', 'fidxa', 4), ('femqm', 'tuqvx', 4), ('psxmb', 'lvtmg', 4), ('mbtvq', 'dkfre', 4), ('qhlpk', 'bppks', 4), ('qnbsl', 'zhyvm', 4), ('okwdu', 'camza', 4), ('gbuio', 'ljlhv', 4), ('flgdo', 'wcchg', 4), ('uhswc', 'fkcvb', 4)], 
[('pwnjl', 'mowxj', 5), ('okyqq', 'ntvxo', 5), ('wslbs', 'nhpsh', 5), ('srzdr', 'cqkwa', 5), ('txjja', 'vbivt', 5), ('asoeo', 'lwhvt', 5), ('mcixp', 'wexid', 5), ('tfowa', 'cwpyr', 5), ('xnqvr', 'qxnik', 5), ('clmgj', 'ihdwk', 5)], 
[('wiink', 'rdpcy', 6), ('benyt', 'swlpp', 6), ('lphzn', 'dbyxa', 6), ('pgjlk', 'xlfei', 6), ('yhuhn', 'dotmn', 6), ('ofpyx', 'vkuqy', 6), ('xxtug', 'ykosp', 6), ('zuehf', 'dqgfb', 6), ('oevmk', 'pjmwx', 6), ('xjkyz', 'ueosz', 6)], 
[('fzvxi', 'xrhdw', 7), ('fesih', 'aspsv', 7), ('jlvhy', 'ozdua', 7), ('pbnan', 'wtfew', 7), ('ceyll', 'ypagh', 7), ('qgwai', 'xnuwe', 7), ('vvvzy', 'zldsz', 7), ('lesiv', 'chluw', 7), ('mknvq', 'tgvjh', 7), ('tbsdv', 'unwdo', 7)], 
[('krffq', 'esydo', 8), ('foyzp', 'qcnaw', 8), ('ookdc', 'lcswu', 8), ('ekecn', 'norrc', 8), ('xrmhe', 'qlkuq', 8), ('rmvkx', 'oigfu', 8), ('tveoz', 'sfzgt', 8), ('vwaxr', 'xqtcn', 8), ('cyejo', 'babla', 8), ('lmlxg', 'nquwc', 8)], 
[('pxawo', 'wtdmi', 9), ('teeah', 'gbccn', 9), ('hzwdh', 'slbvx', 9), ('eugqi', 'filjb', 9), ('elgot', 'ckyee', 9), ('txaxj', 'owetf', 9), ('komye', 'jbzsl', 9), ('jjrpy', 'acqbz', 9), ('nbpzu', 'ijvlf', 9), ('aiebv', 'ygyge', 9)]]

for Row in CollidingKeys:
    for Column in Row:
        Node1 = Node(Column[0],random.randint(1000,5000))
        Node2 = Node(Column[1],random.randint(1000,5000))
        Table.Insert(Node1)
        Table.Insert(Node2)


for Tree in Table.Table:
    print("\n")
    Tree.printTree()
    print("\n")

print(Table.Find('igyoo'))