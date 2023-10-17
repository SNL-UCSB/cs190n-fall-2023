# Assignment 1

Submit a text/pdf/markdown PDF to the [Canvas submission](https://ucsb.instructure.com/courses/15801/assignments/174698) that has answers to the 6 tasks described within this [notebook](./exploratory_data_analysis.ipynb).

### Task 1
Report the number of TCP/UDP/total packets contained within both files `pcaps/sample_speed_test.pcap` and `pcaps/speed_test.pcap`. Report the time it takes to read each pcap using the `scapy` library. 

### Task 2
Measure the time it takes to convert the file `pcaps/sample_speed_test.pcap` to a Pandas DataFrame. Estimate the time it will take to convert the file `pcaps/speed_test.pcap` to a Pandas DataFrame.

### Task 3
Report the number of unique 5-tuples, within `pcaps/speed_test.pcap`. 

### Task 4
Report the top 5 server IP(s) that send the most inbound data to the local client (192.168.0.203) in `pcaps/speed_test.pcap`.

### Task 5
Visualize the number of inbound and outbound bytes observed every second **over all flows** between the local IP (192.168.0.203) and the server IPs you identified in the previous task. Given the results of your graph, estimate the download / upload achieved throughput by this speedtest.

### Task 6
Visualize the number of inbound and outbound bytes observed every second between the server IPs you identified in Task 4 and the local IP (192.168.0.203). Do you observe similar throughput across different flows? Why do you think this speed test opens multiple connections instead of a single connection to measure the available bandwidth?
