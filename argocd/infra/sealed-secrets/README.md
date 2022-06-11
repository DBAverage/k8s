# sealed-secrets

- install kubeseal 

        https://github.com/bitnami-labs/sealed-secrets/releases
        
- get public key

        kubeseal --fetch-cert \
        --controller-name=sealed-secrets-controller \
        --controller-namespace=sealed-secrets \
        > pub-sealed-secrets.pem

- generate secret manifest

        kubectl -n default create secret generic basic-auth \
        --from-literal=user=admin \
        --from-literal=password=change-me \
        --dry-run=client \
        -o yaml > basic-auth.yaml

- encrypt with kubeseal

        kubeseal --format=yaml --cert=pub-sealed-secrets.pem \
        < basic-auth.yaml > basic-auth-sealed.yaml

- delete plaintext secret manifest

        rm basic-auth.yaml