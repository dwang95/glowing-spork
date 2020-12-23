CS598 Final Project FA20
Tianlu (David) Wang
Yuchen Wang
Yinfei Zu

This is a framework built off the OpenLTH framework, modified to run specific lottery ticket experiments, based on the Frankle & Carbin 2018 paper.

A neural network model can be chosen (LeNet, ResNet, ect.) to be trained and then iteratively pruned
 based on MNSIT handwriting data. The number of iterations can be chosen, as well as the pruning rate. 
A mask of 0 and 1 is used to simulate the removal of neurons. The pruned model can then be used as a 
sparse network, in order to decrease compuational and storage resources. Further experiments can be done 
on the resulting Lottery Tickets, such as analyzing their weight distribution, average connections, untrained performance on datasets,
and trained performance on new datasets. 
