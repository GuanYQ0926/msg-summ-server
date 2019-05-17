import MeCab
import collections


def seperate_sentence(message_list):
    mt = MeCab.Tagger()
    mt.parse('')
    word_count = collections.defaultdict(int)
    for message in message_list:
        node = mt.parseToNode(message)
        while node:
            fields = node.feature.split(',')
            # and fields[2] == '一般'
            if fields[0] == '名詞' or\
                    fields[1] == '動詞' or fields[1] == '形容詞':
                word = node.surface
                word_count[word] += 10
            else:
                pass
            node = node.next
    return word_count
