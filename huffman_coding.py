from collections import Counter

string = "BCAADDDCCACACAC"

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)
    
# Function to decode a message using a given huffman tree
def huffman_decode(encoded_string, huffman_tree):
    decoded_string = ''
    current_node = huffman_tree
    for bit in encoded_string:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if isinstance(current_node, str):
            decoded_string += current_node
            current_node = huffman_tree
    return decoded_string

# Function to create a huffman tree
def huffman_tree(node, binary=''):
    if isinstance(node, str):
        return {node: binary}
    (left, right) = node.children()
    d = dict()
    d.update(huffman_tree(left, binary + '0'))
    d.update(huffman_tree(right, binary + '1'))
    return d

freq = Counter(list(string)).most_common()

nodes = freq

while len(nodes) > 1:
    # Remove last two elements
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]

    # Append new one with summed frequency
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    # Sort by most common again
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffman_code = huffman_tree(nodes[0][0])

print('Char | Huffman code')
print('-------------------')
for (char, frequency) in freq:
    print('%r  |  %s' % (char, huffman_code[char]))

encoded_string = ''.join([huffman_code[x] for x in string])

print(encoded_string)

decoded_string = huffman_decode(encoded_string, nodes[0][0])

print(decoded_string)
