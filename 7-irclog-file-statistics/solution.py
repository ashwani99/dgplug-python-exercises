"""Take the whole file as a string in triple quotes from https://dgplug.org/irclogs/2017/Logs-2017-06-18-13-41.txt. 
Write a program which will tell the following:

1. How many different nicks were present in that log
2. Who spoke how many lines
3. And how many words"""

# The following string contains the log
log = """----BEGIN CLASS----
[13:27] <kushal> #startclass
[13:28] <ikshitij> kushal: ok
[13:28] <kushal> Roll Call
[13:28] <jasonbraganza> Jason Braganza
[13:28] <ashwanig> Ashwani Kumar Gupta
[13:28] <anuGupta> Anu kumari Gupta
[13:28] <bhavin192> Bhavin Gandhi
[13:28] <asraisingh> Abhishek Singh
[13:28] <ikshitij> Kshitij
[13:28] <kvy> ashwanig thanks for suggestion
[13:28] <pr97> Priyanka Sharma
[13:28] <soumam007> Soumam Banerjee
[13:29] <imack> Mahendra Yadav
[13:29] <sitlanigaurav[m]> Gaurav Sitlani
[13:29] <saptaks> Saptak Sengupta
[13:29] <schubisu> Robin Schubert
[13:30] <yurii> Yurii Pylypchuk
[13:30] <kushal> Okay, questions on strings chapter?
[13:31] <kushal> Any questions?
[13:31] <jasonbraganza> for once I understood
[13:31] <jasonbraganza> thatâ€™s
[13:32] <mdbk> Roll call: Onyinye Madubuko
[13:32] <yurii> !
[13:32] <jasonbraganza> thatâ€™ll obviously be tested once I have to solve a problem though :)
[13:32] <kushal> Which method to call to break a string in different parts?
[13:32] <sitlanigaurav[m]> kushal: split()
[13:32] <kushal> :)
[13:32] <ashwanig> kushal split()
[13:32] <kushal> next
[13:32] <asraisingh> split()
[13:33] <ikshitij> split()
[13:33] <yurii> Where can I find more information about %s and %d in -- print("%s 's  total marks %d" % (x, total))
[13:33] <kushal> yurii, wait, providing
[13:34] <kushal> yurii, though better to use .format and f-strings
[13:34] <kushal> I will have to update the book for that.
[13:35] <skarpy> Roll: Akash pathak
[13:35] <skarpy> !
[13:35] <san-D> Roll: Sandesh Patel
[13:35] <knrai1> Roll: Krishnanand Rai
[13:36] <kushal> yurii, https://docs.python.org/3/library/stdtypes.html#old-string-formatting
[13:36] <kushal> next
[13:37] <kvy> ashwanig which part of my code is difficult ? and i lost connection after roll call please pass me logs.
[13:37] <kushal> kvy, discuss it after the session please.
[13:37] <kvy> kushal ok sorry
[13:37] <skarpy> Did my first pull today, small GUI for kshitij's dice game :)
[13:38] <kushal> skarpy, If you can not see, there is a session going on.
[13:38] <kushal> skarpy, otherwise, congratulations.
[13:38] <skarpy> Oops. Sorry.
[13:38] <kushal> skarpy, Was that the question?
[13:38] <kushal> Sorry, but now  I am totally confused.
[13:39] <kushal> skarpy, Just finish the message as <eom> or something so that we know :)
[13:40] <kushal> Anyone else, any questions?
[13:40] <kushal> Today's problem, to be solved during the session
[13:40] <kushal> lines = \"""MemTotal:        7858500 kB
[13:40] <kushal> MemFree:          647000 kB
[13:40] <kushal> MemAvailable:    2487576 kB
[13:40] <kushal> Buffers:          244416 kB
[13:40] <kushal> \"""
[13:41] <kushal> Tell me the free memory, total memory, and available memory in MB
[13:41] <kushal> :)
[13:42] <ikshitij> kushal: we have to read these information from lines?
[13:42] <kushal> https://paste.fedoraproject.org/paste/MIJBk0P3N7wAVkJ7Dnp~fA
[13:42] <kushal> there is a variable already
[13:43] <kushal> copy paste
[13:58] <poojaencoded> session is going or not?
[13:58] <schubisu> poojaencoded: https://paste.fedoraproject.org/paste/MIJBk0P3N7wAVkJ7Dnp~fA task is to print kB in MB
[13:59] <kvy> My connection is lost someone please pass me the logs till now.
[14:00] <asraisingh> https://notebooks.azure.com/n/9vUasNwt1yg/notebooks/summertraining.ipynb
[14:01] <asraisingh> kushal: done.
[14:03] <kushal> asraisingh, now do free -m in terminal
[14:04] <ashwanig> kushal, https://paste.fedoraproject.org/paste/Ou3v59Msl5bkMwZoRmzLmg
[14:04] <kushal> does it say 7674.31640625 ?
[14:04] <asraisingh> kushal: done
[14:04] <kushal> people try out your own answers first, and then think, and then only show us
[14:04] <asraisingh> sorry, i have to use int for it.
[14:05] <ikshitij> kushal: https://notebooks.azure.com/kshitiz/libraries/dgplug/html/summertraining.ipynb
[14:05] <ikshitij> I want to store word in dictionary
[14:05] <ikshitij> But it's throwing error
[14:05] <ikshitij> Index out of range
[14:07] <kushal> ikshitij, yes, the last line is an empty line :)
[14:07] <ikshitij> Oo
[14:07] <ashwanig> kushal, https://paste.fedoraproject.org/paste/f9UiCO6OxKlj5jQrzie2Pw
[14:08] <kushal> ashwanig, yes, checked
[14:08] <kushal> ashwanig, those print function calls look bad
[14:08] <asraisingh> kushal: error corrected, https://notebooks.azure.com/n/9vUasNwt1yg/notebooks/summertraining.ipynb
[14:08] <kushal> You can make them better
[14:08] <ashwanig> kushal, ok should I use .format() ?
[14:09] <kushal> ashwanig, yes, better
[14:09] <kushal> asraisingh, not correct answer, I can see some random numbers
[14:10] <kushal> asraisingh, You will have to give an output which makes sense.
[14:10] <kushal> Here I don't know which line is what.
[14:11] <kushal> brb in 15 minutes
[14:11] <deepika_> Roll Call:Deepika Upadhyay
[14:11] <ashwanig> done. https://paste.fedoraproject.org/paste/8t~V9y918KBUL2iJEM2OUw
[14:12] <knrai1> https://notebooks.azure.com/n/hyeu6kOvr2M/notebooks/summertraining.ipynb
[14:14] <ikshitij> https://notebooks.azure.com/kshitiz/libraries/dgplug/html/summertraining.ipynb
[14:14] <ikshitij> Done
[14:15] <ashwanig> knrai1, the results will be integers not float
[14:16] <ashwanig> ikshitij, We have to convert the memory values into MBs
[14:21] <championshuttler> https://notebooks.azure.com/n/9vUasNwt1yg/notebooks/summertraining.ipynb how to convert this data to an array , i am getting error
[14:22] <ikshitij> kushal: Working https://notebooks.azure.com/kshitiz/libraries/dgplug/html/summertraining.ipynb
[14:23] <bhavin192> https://notebooks.azure.com/bhavin192/libraries/dgplug/html/summertraining.ipynb
[14:23] <knrai1> ashwanig: okay
[14:23] <kushal> championshuttler, we don'
[14:23] <kushal> championshuttler, we don't have normal array in Python
[14:24] <championshuttler> kushal: ok i am trying to do but getting error, is there anyway?
[14:24] <jasonbraganza> for once, I think I got something running
[14:24] <jasonbraganza> please check - https://notebooks.azure.com/jasonbraganza/libraries/dgplug/html/summertraining.ipynb
[14:25] <deepika_> https://notebooks.azure.com/n/nlnVjJirBnQ/notebooks/summertraining.ipynb
[14:26] <ikshitij> kushal: https://notebooks.azure.com/kshitiz/libraries/dgplug/html/summertraining.ipynb Corrected again
[14:27] <kushal> jasonbraganza, total_memory = (split_lines[0])  you can just write total_memory = split_lines[0]
[14:27] <kushal> Now for a line like
[14:27] <kushal> "MemTotal:        7858500 kB"
[14:27] <jasonbraganza> i donâ€™t know why i keep doing that. sorry. will go fix
[14:28] <kushal> what is the best way to split?
[14:28] <kushal> People please discuss
[14:28] <jasonbraganza> i couldnâ€™t quite figure out so I mashed last timeâ€™s expression :)
[14:29] <ashwanig> kushal, for that we can use line.split(':')
[14:30] <ikshitij> split("\n")
[14:30] <ashwanig> ikshitij, Won't that return the original line itself?
[14:30] <kushal> ikshitij, where do you find the "\n"
[14:30] <kushal> ashwanig, :D
[14:31] <yurii> I think the same  -- line.split(':')
[14:31] <jasonbraganza> ashwanig - yes! i forogot!
[14:31] <jasonbraganza> s /forogot /forgot
[14:31] <ikshitij> That was an example
[14:31] <ikshitij> :)
[14:33] <ashwanig> !
[14:33] <schubisu> that would have been my solution https://paste.fedoraproject.org/paste/znTvZfC09w4F-KaCvmLTVw
[14:34] <bhavin192> I did lines.split() and then checked the words
[14:35] <ashwanig> sorry asking out of turn, Is there any function to remove those spaces from the middle without splitting?
[14:35] <ikshitij> kushal: I stored lines in word by line.split(":") and then replaced all spaces by using replace(" ","")
[14:36] <ikshitij> Then stored word and size in Dictionary as key and value respectively
[14:36] <ikshitij> Is this okay
[14:39] <kushal> ikshitij, there can be different ways
[14:39] <ashwanig> ikshitij, nice method :)
[14:40] <kushal> schubisu, alao print what is what
[14:40] <ikshitij> kushal: okay
[14:41] <bhavin192> Using indexes directly makes reading the code a little hard, like word[0]; what do you think guys?
[14:41] <ashwanig> bhavin192, yes, I also have this doubt
[14:41] <anuGupta> https://notebooks.azure.com/n/MBHpc8gojiM/notebooks/summertraining.ipynb
[14:43] <ikshitij> bhavin192: but what, when we have two values only in list, running loop unnecessarily is also not a good idea
[14:43] <ikshitij> I am in doubt for this
[14:44] <bhavin192> ikshitij, you can always add comments or new variables may be like some_index = number
[14:44] <bhavin192> I'm not sure though
[14:44] <kushal> bhavin192, if you know the data, you can do that
[14:44] <kushal> with comments
[14:45] <kushal> Just use index numbers but with comments
[14:47] <ashwanig> kushal, next problem?
[14:47] <bhavin192> kushal, what do you think about this the `buffer_index` https://notebooks.azure.com/bhavin192/libraries/dgplug/html/summertraining.ipynb
[14:47] <schubisu> kushal: sorry, what do you mean with print what is what? Add comments?
[14:47] <kushal> Is anyone have any other questions?
[14:48] <kushal> schubisu, like what output is the free memory
[14:48] <kushal> "Free memory"
[14:48] <anuGupta> Is mine correct?
[14:48] <bhavin192> anuGupta, you are missing spaces around operators
[14:49] <kushal> anuGupta, and also the code looks scary
[14:49] <anuGupta> Split is not splitting ":"
[14:49] <kushal> anuGupta, example?
[14:49] <bhavin192> listing=lines.split() <- anuGupta
[14:49] <schubisu> kushal: it should be in there. Sorry for not posting in a notebook so you can't see on one glance.
[14:50] <anuGupta> Example "me mTotal:" is one of the element of the list
[14:50] <kushal> schubisu, Okay
[14:50] <ashwanig> bhavin192, if you are extracting the substring before the for loop, then what is the need for this `if word.find(":") != -1:` ?
[14:50] <kushal> Every
[14:50] <kushal> Everyone, try not to use a loop
[14:50] <kushal> as this is a fixed data
[14:51] <bhavin192> ashwanig, I'm removing the buffers part only
[14:51] <anuGupta> Kushal, What exactly is scary? I hear this in my every code.
[14:51] <bhavin192> ashwanig, then checking if the word has ":"
[14:52] <bhavin192> anuGupta, have you read my message?
[14:52] <anuGupta> bhavin192, I am using .split() only
[14:52] <bhavin192> <bhavin192> anuGupta, you are missing spaces around operators <bhavin192> listing=lines.split() <- anuGupta
[14:53] <ikshitij> anuGupta: you should give space after operator
[14:53] <ashwanig> bhavin192, Every combination has that, then why checking?
[14:53] <ikshitij> x == 7 not x==7
[14:53] <ikshitij> anuGupta:
[14:53] <anuGupta> Ooh
[14:53] <bhavin192> ashwanig, I'm splitting with .split(), so I have kB as well
[14:54] <bhavin192> ashwanig, to avoid that
[14:54] <anuGupta> Thank you
[14:54] <ashwanig> bhavin192, Oh got it
[14:55] <deepika_> https://notebooks.azure.com/n/nlnVjJirBnQ/notebooks/summertraining.ipynb
[14:56] <ikshitij> ashwanig: how to pass multiple argument in .replace()
[14:56] <ashwanig> ikshitij, what will it do?
[14:57] <ikshitij> https://notebooks.azure.com/n/TB0RRLB9wtM/notebooks/stringProblem.ipynb
[14:57] <kushal> laptop crashed, will take 2 minutes
[14:57] <ikshitij> Check comment with line 1 and line 2 written
[14:57] <kushal> anuGupta, I will answer you
[14:57] <kushal> anuGupta, for example
[14:57] <kushal> if(listing[i].isdigit()==True):
[14:58] <kushal> if statement does not need ()
[14:58] <kushal> so that statement becomes if listing[i].isdigit()==True :
[14:58] <kushal> now
[14:58] <kushal> anuGupta, if you remember https://pymbook.readthedocs.io/en/latest/ifelse.html#truth-value-testing
[14:58] <kushal> that line can now become
[14:58] <kushal> if listing[i].isdigit():
[14:59] <kushal> anuGupta, Isn't that cleaner?
[14:59] <anuGupta> Yes kushal
[14:59] <anuGupta> Understood
[14:59] <kushal> listing[i]=str(round(int(listing[i])/1024)) + "  "
[14:59] <kushal> I can only imagine what it is doing
[14:59] <kushal> anuGupta, remove the loop
[14:59] <kushal> don't use any loop
[14:59] <kushal> and then try to rewrite that oce
[14:59] <kushal> code
[14:59] <anuGupta> Ook correcting
[15:00] <anuGupta> S/ook/ok
[15:00] <kushal> anuGupta, your code is correct, but looks like C than python
[15:00] <ikshitij> kushal I think this code is converting list item into integer then again to string after division
[15:00] <ikshitij> Am I right ?
[15:00] <anuGupta> Yes ikshitij
[15:01] <kushal> Tonight problem
[15:01] <ikshitij> why string again ? We can store integer into list also @anuGupta
[15:01] <kushal> Take the whole file as a string in triple quotes from https://dgplug.org/irclogs/2017/Logs-2017-06-18-13-41.txt
[15:02] <kushal> and then write a code, which will tell me, 1. How many total different nicks were present in that log
[15:02] <anuGupta> When I am joining back to string , it requires all the elements to be string
[15:02] <kushal> who spoke how many lines
[15:02] <kushal> and how many words
[15:02] <kushal> 3 things
[15:02] <kushal> roll call
[15:02] <kvy> ikshitij we have something more strong then link-list.
[15:02] <anuGupta> Anu kumari Gupta
[15:02] <jasonbraganza> Jason Braganza
[15:02] <schubisu> Robin Schubert
[15:02] <devesh__verma> devesh verma
[15:02] <kvy> kumar vipin yadav
[15:02] <ikshitij> Kshitij
[15:02] <asraisingh> Abhishek Singh
[15:03] <bhavin192> Bhavin Gandhi
[15:03] <ashwanig> Ashwani Kumar Gupta
[15:03] <kushal> Solve this problem, who ever is doing this first, mail the link to the notebook to the mailing list
[15:03] <pr97> Priyanka Sharma
----END CLASS----"""


# A dictionary to contain nicks and the number of lines and words spoken by them
nicks = {}

for line in log.split('\n'):
    parts = line.split()
    if len(parts) < 3:
        continue
    
    current_nick = parts[1].strip('<>')
    words_spoken = parts[2:]

    if current_nick in nicks:
        # Update the number of lines spoken by the nick
        nicks[current_nick][0] += 1
        # Update the number of words spoken by the nick
        nicks[current_nick][1] += len(words_spoken)
    else:
        # Create a new nick entry
        nicks[current_nick] = []
        nicks[current_nick].append(1)
        nicks[current_nick].append(len(words_spoken))

print('There were {} different nicks present in the log'.format(len(nicks)))
print('\nDetailed overview:')
print('------------------')
for current_nick in nicks:
    print('{} spoke {} lines and {} words.'.format(current_nick, nicks[current_nick][0], nicks[current_nick][1]))