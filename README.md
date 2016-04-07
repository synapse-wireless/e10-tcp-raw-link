[![](https://cloud.githubusercontent.com/assets/1317406/12406044/32cd9916-be0f-11e5-9b18-1547f284f878.png)](http://www.synapse-wireless.com/)

# E10 SNAPconnect Example - TCP Raw Link

This example application allows the E10 to be used as a terminal-server style IP gateway for applications in a network of "SNAP Link" wireless serial devices. 
It accepts TCP connections like telnet and broadcasts the stream.

## Setting Up the E10 Gateway

First, copy this example's .py files to your E10. For this example we put them in the directory `/root/tcpraw`.
You can use ssh/scp, mount a flash drive, or use any other method copy the files over. 
If you put the files in a directory other than `/root/tcpraw`, you must change the paths in the accompanying `S999snap` file to match.

You will need to make sure that the latest SNAPconnect package is installed on your gateway:

```bash
pip install --extra-index-url https://update.synapse-wireless.com/pypi snapconnect
```

Additionally, copy the `S999snap` shell script to the `/etc/init.d` directory if you want this application to start automatically when the E10 powers on.

## Running This Example

The example as provided accepts connections on TCP port 3000. Change variable `TCP_PORT` in [tcpRawLink.py](tcpRawLink.py) to change this port.

Once everything has been set up, simply run the following command to test it:

```bash
python tcpRawLink.py
```

This will show debug on the console when data is transferred.

Test the "daemonized" version by running:

```bash
python remote_daemon.py start
```

The application should start at boot if configured per above instructions.

Use Portal to set the channel of your E10's bridge node, and if desired you can
upload the "e10bridge.py" SNAPpy script to it for status LED support.

## License

Copyright © 2016 [Synapse Wireless](http://www.synapse-wireless.com/), licensed under the [Apache License v2.0](LICENSE.md).

<!-- meta-tags: vvv-e10, vvv-snapconnect, vvv-python, vvv-example -->
