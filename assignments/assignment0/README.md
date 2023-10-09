# Assignment 0

**Released:** October 9th, 2023  
**Due Date:** October 13th, 2023

**Note**: This is not a graded assignment. But, it is strongly recommended that you finish this assignment before the discussion section on Friday (October 13). 

## Tasks
1. Create a GitHub account
2. Create your own SSH keys
3. Upload key to your account
4. Submit your GitHub user ID  and wait for Access
5. Verify your connectivity to lab servers
6. Start jupyter notebook
7. Setup tunneling for Jupyter notebook
8. Execute example notebook

## Task 1: Create a Github Account
Assignments will be distributed using https://github.com for this course. 

If you don't already have a Github account, create one using just the free plan. Please make sure to add your @ucsb.edu email address if you created your account using a personal email address (Settings > Emails > Add email address)

## Task 2: Create your own SSH Keys
If you do not already have personal SSH keys, you will need to create a key pair to be used for authenticating into our lab servers where you will complete your assignments. 

Using a terminal that supports the `ssh-keygen` command, create a private key (kept secret) and a public key (upload to GitHub account).  

```ssh-keygen -t rsa -b 4096 -C "your_email@example.com"```

`-t` specifies the key type (RSA encryption)  
`-b` specifies the key's bit length  
`-c` is a comment to help identify the key (change to your email address)  

You will then be prompted to choose the location to save the SSH keys. The default location is usually `~/.ssh/id_rsa` for the private key and `~/.ssh/id_rsa.pub` for the public key. Feel free to use the default location or specify a different one if needed.

You will then be prompted to enter a passphrase as an extra layer of security to your private key when you use it to authenticate. This is optional, and you can simply press return twice if you would like to skip setting a password. 

The `ssh-keygen` tool will now generate your SSH key pair. Once the command completes, verify that your keys exist using `ls ~/.ssh` or the directory you specified when saving your SSH keys. 

## Task 3: Upload key to your account
Now you will upload your SSH keys to your GitHub account so they can be used for authenticating into our lab servers.

Log into your GitHub account and navigate to SSH and GPG keys (Settings > SSH and GPG keys) in the sidebar. Select "New SSH Key" and add your public key you just generated (ends with `.pub`), and use the title field to name this key anything you want.

Once you successfully add this SSH key to your GitHub account, you should see it listed on the SSH and GPG keys page.

## Task 4: Submit your Github ID

Fill out this [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSeKAvschvWi8uHTyJ_d_pMxv9IJ6A5xDgq4Xd5splXzwpdjhQ/viewform?usp=sf_link) to specify your UCSB Net ID and your GitHub ID so that we can provision you access to our lab servers where you will be able to work on your assignments.

Wait to be provisioned access. Please be patient, as this may take up to a day. We will notify you via email once your account has been provisioned.

## Task 5: Verify Connectivity to Lab Servers

Once your account has been provisioned, you should be able to SSH into the lab servers using your `<ucsb_net_id>` and the `<location>` of your SSH private key. Make sure to substitute these values into the command below.

```ssh -i <location> <ucsb_net_id>@snl-server-5.cs.ucsb.edu```

`-i` specifies the identity file you are using to authenticate with (private key)

If you set a password for your SSH key, you will be prompted to enter it now. If your account has been provisioned, you should successfully be able to log in to the lab servers.

## Task 6: Start Jupyter notebook

First, you should clone the course GitHub repository into your home directory (`~/` a.k.a. `/home/<ucsb_net_id>`).

```
git clone https://github.com/SNL-UCSB/cs190n-fall-2023.git
```

You may need to set up a personal access token (PAT) to authenticate to your GitHub account if you clone via HTTPS. This can be done in Github under the Developer Settings of your account in the sidebar. (Settings > Developer Settings > Personal Access Tokens > Tokens)

Additionally, you can use `scp` to copy your keys over to the server and store them in your `~/.ssh` folder on the server. Then you will be able to clone the repo via SSH.

```
git clone git@github.com:SNL-UCSB/cs190n-fall-2023.git
```

Once you clone the repository, navigate to `cs190n-fall-2023/assignments/assignment0/`. Run `ls` and you should see `example_notebook.ipynb` and this readme file.

You may choose any available `<port>` to expose your Kupyter notebook, preferably between 10000 and 50000. First, check if your port is available using `netstat`. 

```
netstat -nl | grep <port>
```

If this command produces no output for your chosen port, then that means it should be available. Once you find an available port, try to reuse the same port number in the future for your notebooks to avoid collisions with other students.

Then you can start your Jupyter notebook on this port with the following command, substituting `<port>` with the available port that you chose in the previous step:

```
jupyter-notebook --no-browser --port=<port>
```

This will start a Jupyter session on this server that we will connect to using an SSH tunnel and your local browser. This command will generate a token in one of the URLs, as shown below:

```
http://localhost:<port>/?token=<token>
```

Make sure to keep track of `<token>` as you may need to enter it as authentication in your browser when connecting to this Jupyter session.

## Task 7: Setup Tunneling for Jupyter Notebook

Now that we have a Jupyter session running on the lab server on your chosen `<port>`, we will create an SSH tunnel from your local machine to this port to access the Jupyter notebook in your browser. 

Using a new terminal on your local machine, start an SSH tunnel from your local machine to the lab servers. For this command, we are choosing a local port of `8888`, which is just an example. Any available port on your local machine can be chosen, but be sure to use this port when connecting to the notebook in your browser. Again you will provide the `<location>` of your private key to use for authentication.

```
ssh -L 8888:127.0.0.1:<port> -i <location> <ucsb_net_id>@snl-server-5.cs.ucsb.edu
```

Now open your browser and navigate to http://localhost:8888 or whichever local port you chose in the previous step when starting your SSH tunnel. 

If required, enter the `<token>` from the previous task that you received when starting the Jupyter session.

This should bring you to the Jupyter home page, which will display the file system from where you started your Jupyter session on the remote server. You should see again see the `example_notebook.ipynb` and this readme.

## Task 8: Execute Example Notebook

Open the example notebook by clicking on `example_notebook.ipynb` from the jupyter home page you just connected to. This should open up the notebook and allow you to interact with the cells. Make sure that you can execute and evaluate all the cells. 
