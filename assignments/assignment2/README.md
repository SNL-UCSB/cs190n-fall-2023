# Assignment 2

## Due Date: November 15th

Submit a text/pdf/markdown PDF to the [Canvas submission](https://ucsb.instructure.com/courses/15801/assignments/180681) that has answers to the tasks described within this [notebook](./latency_under_load.ipynb).

### Task 1
Create a pipeline to collect latency data to Google's public DNS (8.8.8.8) from your working node using the [Ping](https://github.com/netunicorn/netunicorn-library/blob/main/tasks/measurements/ping.py) task.   
Report the average latency over 5 ICMP probes to the address 8.8.8.8

### Task 2
Now we will define a new task, StartBackgroundPing that behaves similar to the Ping task, however it starts the process in the background, so further tasks in the pipeline will execute in parallel with our latency measurements.  
Implement the **run()** function in the **StartBackgroundPingLinuxImplementation** class

### Task 3
Now we will define a new task, GetFileContents that will output the results that we wrote to a file in the StartBackgroundPing task. This task simply prints the content of a file to stdout.
Implement the **run()** function in the **GetFileContents** class

### Task 4
Collect latency samples to 8.8.8.8 using the new tasks we've defined. The pipeline has already been defined for you below, but requires that the StartBackgroundPing and GetFileContents tasks are implemented correctly. Plot the results. The x-axis should be the ICMP sequence number (icmp_seq), and the y-axis should the latency in milliseconds. You should observe similar values to what you observed from Task 1.

### Task 5
Now we will use the SpeedTest task to induce extra load on the network, and simultaneously collect our lateny samples. The pipeline has already been defined for you below, but requires that the StartBackgroundPing and GetFileContents tasks are implemented correctly. Plot the results alongside the results from Task 4. The x-axis should be the ICMP sequence number (icmp_seq), and the y-axis should the latency in milliseconds.

### Task 6
Do you observe a difference in latencies between Task 4 and Task 5? If so, what is the reason that we observe an increased latency when we are simultaneously running a speedtest?
