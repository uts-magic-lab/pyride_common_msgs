#!/usr/bin/env python

import os
import rospy
import json
from pyride_common_msgs.msg import NodeStatus, NodeMessage

class PyRideLoopbackMsgRouter( object ):
    def __init__( self ):
        self.sub = rospy.Subscriber("/pyride/node_message", NodeMessage, self.input_cb)
        self.pub = rospy.Publisher("/pyride/node_status", NodeStatus, queue_size=2)

    def input_cb( self, input_msg ):
        if input_msg.node_id != 'message_router':
            return
        try:
            message = json.loads(input_msg.command)
        except:
            rospy.logerr("invalid message format for PyRIDE message router")
            return
        if not isinstance(message, dict) or 'node_id' not in message or 'command' not in message:
            rospy.logerr("invalid message format for PyRIDE message router")
            return

        msg = NodeStatus()
        msg.node_id = message['node_id']
        msg.header = input_msg.header
        msg.status_text = message['command']
        msg.for_console = False
        self.pub.publish( msg )

def main():
    rospy.init_node('pyride_msg_loopback_router')

    la = PyRideLoopbackMsgRouter()
    rospy.spin()

if __name__ == '__main__':
    main()
