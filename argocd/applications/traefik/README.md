# To create a dashboard user

- create user data

        htpasswd -nb user password | openssl base64

- save it to secret manifest file (secret.yaml)

      apiVersion: v1
      kind: Secret
      metadata:
        name: dashboard-auth
        namespace: traefik
      type: kubernetes.io/basic-auth
      data:
        username: dXNlcg== # username: user
        password: cGFzc3dvcmQ= # password: password

- seal it as a sealed-secret

    kubeseal --format=yaml --cert=pub-sealed-secrets.pem \
    < dashboard-auth.yaml > dashboard-auth-sealed.yaml
