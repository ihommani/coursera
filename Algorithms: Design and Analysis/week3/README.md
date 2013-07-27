**Few explanation** 

This algorithm allow to find the optimal cut for a graph.
Given an input which represent the adjacent list of a 200 nodes list.
The first step is to compute the adjacent list into a python dict (hashTable). Key: Node, Value: list of neighbours
i compute the contraction algorithm until it left two nodes. Contraction is like a fusion. When i fuse node A with node B, node A doesn't exist anymore under the name A but B. Moreover they now share their neighbors. Also the node is deleted from the adjacent list.


The good thing in the way i implement the algo is that i never reconstruct the adjacent list (i.e the graph)
Once i fused two nodes, i keep a reference to the deleted node and its new name via a python dict.
{fusedNode: node}. This way i can choose two nodes to fuse without choosing a node that doesn't exist anymore or that is the same. 
This is allowed by the recursive method *fusedNodeAlias* which literally sniff the true identity (i.e which node is the node foo among the existing one. foo has previouly been fuse) of the node thanks to the dict _removedItems_ .

Finally, it left me two nodes in the adjacent list. 
The number of cut is given by the number of neighbours different from the entry node. They should represent the second node...
