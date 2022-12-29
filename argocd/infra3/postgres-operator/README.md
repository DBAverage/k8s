# Notes

- Huge pages needs to be disabled on host, or at least properly working with kubernetes
- Connection details are stored in a secret named \<clusterName>-pguser-\<userName>
    <br/>`kubectl get secret -n postgres-operator <clusterName>-pguser-<userName> -o json | jq '.data | map_values(@base64d)'`
- Added postgres traefik entrypoint to use ingressroutes    
- To connect either change service to NodePort, use ingressroute, or a temporary port forward
    <br/> `kubectl port-forward pod/<clusterName>-instance1-<podsuffix> 5432:5432`


# Example Cluster Spec

```apiVersion: postgres-operator.crunchydata.com/v1beta1
kind: PostgresCluster
metadata:
  name: awx-postgres
  namespace: awx
spec:
  image: registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi8-14.6-0
  postgresVersion: 14
  instances:
    - name: instance1
      dataVolumeClaimSpec:
        accessModes:
        - "ReadWriteOnce"
        resources:
          requests:
            storage: 8Gi
  backups:
    pgbackrest:
      image: registry.developers.crunchydata.com/crunchydata/crunchy-pgbackrest:ubi8-2.41-0
      repos:
      - name: repo1
        volume:
          volumeClaimSpec:
            accessModes:
            - "ReadWriteOnce"
            resources:
              requests:
                storage: 8Gi
```


# Force reset an unknown password

  - connect to pod shell
  - `sed -ibak 's/^\([^#]*\)md5/\1trust/g' /opt/bitnami/postgresql/conf/pg_hba.conf`
  - `pg_ctl reload`
  - ```
    psql -U postgres
    alter user postgres with password 'NEW_PASSWORD';
    \q
    ```
  - `sed -i 's/^\([^#]*\)trust/\1md5/g' /opt/bitnami/postgresql/conf/pg_hba.conf`
  - `pg_ctl reload`