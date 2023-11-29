# Assignment 3

## Due Date: December 8th

Submit a text/pdf/markdown PDF to the [Canvas submission](https://ucsb.instructure.com/courses/15801/assignments/185659) that has answers to the tasks described within this [notebook](./training_a_classifier.ipynb).

### Task 1a
The client IP in these packet captures is 172.17.0.2, discard the background traffic and retain only the packets with a source or destination IP equal to 172.17.0.2. 

### Task 1b
Now we will filter these dataframes to only include TCP traffic (protocol 6), and calculate the TCP payload length. This new column will be called `tcp_len` which represents the length of the TCP payload. This is important because it helps us differentiate packets carrying data from the acknowledgement packets. The TCP length can be calculated as the difference between the IP Packet Length and the sum of the IP Header Length and TCP Header Length.

### Task 1c
We will only consider TCP flows with at least 30 inbound OR outbound packets with a TCP length greater than 0 within the flow and discard packets from the remaining flows.  

### Task 2
Compute these features for each flow. You'll want to use the groupby function to group each flow and the agg function to compute these metrics aggregated over each group. We've provided you with the functions to use to calculate inter-packet delay, and you should be able to use `count` and `sum` to compute the total packets and bytes per flow.

### Task 3
Now we will label our flows as twitch or vimeo. We included the `file` column above which has a label for the specific file the packet is from. You can use this field to label each flow as twitch or vimeo.

### Task 4
Now that we have selected our features and labelled our data, we can train a simple classifier. Choose a classifier from [python-scikit](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning). 

### Task 5
You will likely observe a very high if not perfect precision/recall because we are using a small amount of data and we are training / testing using the same dataset. This means that we were able to fit a model that can classify all of our training data correctly. Now we will generate a report from Trustee as well as visualize our model to understand which features are being used to classify our data.
