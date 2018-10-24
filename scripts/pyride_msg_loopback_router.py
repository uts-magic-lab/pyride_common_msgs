#!/usr/bin/env python

import os
import rospy
from pyride_common_msgs.msg import NodeStatus, NodeMessage

class PyRideLoopbackMsgRouter( object ):
    def __init__( self ):
        self.sub = rospy.Subscriber("/pyride/node_message", NodeMessage, self.input_cb)
        self.pub = rospy.Publisher("/pyride/node_status", NodeStatus,queue_size=2)

    def input_cb( self, input_msg ):
    	msg = NodeStatus()
    	msg.node_id = input_msg.node_id
	msg.header = input_msg.header
    	msg.status_text = input_msg.command
    	msg.for_console = False
    	self.pub.publish( msg )

def main():
    rospy.init_node('pyride_msg_loopback_router')

    la = PyRideLoopbackMsgRouter()
    rospy.spin()

if __name__ == '__main__':
    main()
