# Notes

Had to disable hugepages on the worker nodes for postgres instance to start successfully.
This is likely a symptom of issues with huge pages in the cluster.

To disable hugepages update the talos config for each worker node.

talosctl -n $worker_node_ip patch machineconfig -p '[{"op": "add", "path": "/machine/sysctls/vm.nr_hugepages", "value": "0"}]'