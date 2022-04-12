ZMQ for short, is a high-performance asynchronous message passing library used in distributed systems.
However, ZeroMQ specifically focuses on high throughput and low latency applications — which is exactly how you can frame live video streaming.

PyZMQ provides python bindings for ØMQ and allows you to leverage in python applications. It has two primary packages for serializing objects: json and pickle, for sending and receiving objects serialized with these modules. 

A socket has the methods send_pyobj(), which correspond to sending an object over the wire after serializing with pickle, and any object sent via this method can be reconstructed with the recv_pyobj() method.
