# Kubernetes - Infrastructure As Code

This repo is intented for my personal use managing the kubernetes setup in my home lab. If you come accross this repo, be aware that it's configuration will be highly dependant on my internal environment.


# Kubernetes Installation
- Talos Linux
- Installed on VMWare
- 3 master node2
- 3 worker nodes


# Persistence Layer
- Rook Ceph
    - https://rook.io/
- NFS Subdir External Provisioner
    - https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner.git
    - NFS being served by synology NAS

# Load Balancing
- MetalLB
- https://github.com/metallb/metallb.git


# Ingress - Reverse Proxy
- Traefik
- https://github.com/traefik/traefik.git


# IaC/CD
- ArgoCD
- https://argoproj.github.io/cd/


# Pre-Requisites / External Dependencies
- NAS Server
- VMWare ESXi with VCenter
