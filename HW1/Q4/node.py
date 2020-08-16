import json
import threading
import sys
from stream import Stream


class Node:
    def __init__(self,uid=None,next=None):

        ''' Network Variables '''
        self.stream = Stream()
        self.address = (self.stream.ip, self.stream.port)

        ''' Algorithm Variables '''
        self.uid = uid
        print('node', uid, 'initialized successfully with address:', self.address)
        self.leader_selected = False
        self.leader = 0

    def run(self):
        self.send_message("m" + str(self.uid))
        while True:
            stream_in_buff = self.stream.read_in_buf()
            for message in stream_in_buff:
                self.handle_message(message)

    def handle_message(self, message):







        m = str(message)
        m = int(m[3:])
        x=int(m[:3]);


        if x.decode()=="m":   #LCR algorithm


            if m == self.uid:#if message is equal to uid,we have found the Leader ^_____^

                self.leader_selected = True

                self.leader = m

                print ("I'm node " + str(self.uid) + " and I say node " + str(m) + " is our Leader!!")

                self.send_message("t" + m.decode())


            if m > self.uid:#if message is greater than uid,pass the message

                self.send_message("m" + m.decode())

            else:#if message is smaller than uid,nothing happens

                pass



        elif (x.decode()=="t")and(self.leader_selected == False):#we send that leader that leader have been found ^____^

            self.leader_selected = True

            self.leader = m

            self.send_message("t" + m.decode())

            print("I'm node " + str(self.uid) + " and I say node " + str(m) + " is our Leader!!")


    def send_message(self, msg):
        self.stream.add_message_to_out_buff(msg)
        self.stream.send_messages()