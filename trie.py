# Python program for delete operation 
# in a Trie 

class TrieNode(object): 
	''' 
	Trie node class 
	'''
	def __init__(self): 
		self.children = [None]*26

		# non zero if leaf 
		self.value = 0

	def leafNode(self): 
		''' 
		Check if node is leaf node or not 
		'''
		return self.value != 0

	def isItFreeNode(self): 
		''' 
		If node have no children then it is free 
		If node have children return False else True 
		'''
		for c in self.children: 
			if c:return False
		return True


class Trie(object): 
	''' 
	Trie data structure class 
	'''
	def __init__(self): 
		self.root = self.getNode() 

		# keep count on number of keys 
		# inserted in trie 
		self.count = 0

	def _Index(self,ch): 
		''' 
		private helper function 
		Converts key current character into index 
		use only 'a' through 'z' and lower case 
		'''
		return ord(ch)-ord('a') 

	def getNode(self): 
		''' 
		Returns new trie node (initialized to NULLs) 
		'''
		return TrieNode() 

	def insert(self,key): 
		''' 
		If not present, inserts key into trie 
		If the key is prefix of trie node,mark 
		it as leaf(non zero) 
		'''
		length = len(key) 
		pCrawl = self.root 
		self.count += 1

		for level in range(length): 
			index = self._Index(key[level]) 

			if pCrawl.children[index]: 
				# skip current node 
				pCrawl = pCrawl.children[index] 
			else: 
				# add new node 
				pCrawl.children[index] = self.getNode() 
				pCrawl = pCrawl.children[index] 

		# mark last node as leaf (non zero) 
		pCrawl.value = self.count 

	def search(self, key): 
		''' 
		Search key in the trie 
		Returns true if key presents in trie, else false 
		'''
		length = len(key) 
		pCrawl = self.root 
		for level in range(length): 
			index = self._Index(key[level]) 
			if not pCrawl.children[index]: 
				return False
			pCrawl = pCrawl.children[index] 

		return pCrawl != None and pCrawl.value != 0


	def _deleteHelper(self,pNode,key,level,length): 
		''' 
		Helper function for deleting key from trie 
		'''
		if pNode: 
			# Base case 
			if level == length: 
				if pNode.value: 
					# unmark leaf node 
					pNode.value = 0

				# if empty, node to be deleted 
				return pNode.isItFreeNode() 

			# recursive case 
			else: 
				index = self._Index(key[level]) 
				if self._deleteHelper(pNode.children[index], key, level+1, length): 
					# last node marked,delete it 
					del pNode.children[index] 

					# recursively climb up and delete 
					# eligible nodes 
					return (not pNode.leafNode() and pNode.isItFreeNode()) 

		return False

	def deleteKey(self,key): 
		''' 
		Delete key from trie 
		'''
		length = len(key) 
		if length > 0: 
			self._deleteHelper(self.root,key,0,length)	 


def main(): 
	keys = ["she","sells","sea","shore","the","by","sheer"] 
	trie = Trie() 
	for key in keys: 
		trie.insert(key) 

	trie.deleteKey(keys[0]) 

	print("{} {}".format(keys[0], "Present in trie" if trie.search(keys[0]) else "Not present in trie")) 

	print("{} {}".format(keys[6], "Present in trie" if trie.search(keys[6]) else "Not present in trie"))	 

if __name__ == '__main__': 
	main() 